# -*- coding: utf-8 -*-

import argparse
import asyncio
import functools
import importlib
import json
import sys
import time
import multiprocessing

import aiohttp
import gevent
import requests
import tornado.ioloop
import uvloop
from tornado import gen
from tornado.httpclient import AsyncHTTPClient


PAGE_LIST = range(1, 30)
BASE_URI = 'https://leetcode.com/contest/api'
WEEK_URL = BASE_URI + '/list/'
RANK_URL = BASE_URI + '/ranking/leetcode-weekly-contest-{}/?pagination={}'

START = time.time()


def print_rank(data):
    print('\n\n+{0} LeetCode Rank {0}+'.format('-'*15))
    for k, v in data.items():
        print('|{:>15}: {:<28}|'.format(k, str(v)))
    print('+{}+'.format('-'*45))


def search_username_rank(data, username, sys_exit=True):
    for user in data['total_rank']:
        if user['username'] == username:
            print_rank(user)
            if sys_exit:
                print('Finished in {:.3f}s'.format(time.time() - START))
                sys.exit(0)
            else:
                return True


#######################
# asyncio async/await #
#######################

async def get_user_rank(week, page_id, username):
    async with aiohttp.ClientSession() as session:
        async with session.get(RANK_URL.format(week, page_id)) as resp:
            data = await resp.json()
            print('{} | '.format(page_id * 50), end='', flush=True)
            search_username_rank(data, username)


#####################
# asyncio coroutine #
#####################

@asyncio.coroutine
def get_user_rank_by_async_coroutine(week, page_id, username):
    with aiohttp.ClientSession() as session:
        resp = yield from session.get(RANK_URL.format(week, page_id))
        data = yield from resp.json()
        print('{} | '.format(page_id * 50), end='', flush=True)
        search_username_rank(data, username)


def asyncio_entry(func, week, username):
    loop = asyncio.get_event_loop()
    tasks = [func(week, i, username) for i in PAGE_LIST]
    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()


#######################
# asyncio with uvloop #
#######################

def asyncio_with_uvloop_entry(week, username):
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    asyncio_entry(get_user_rank, week, username)


###########
# tornado #
###########

@gen.coroutine
def fetch_and_parse(week, page_id, username):
    client = AsyncHTTPClient()
    resp = yield client.fetch(RANK_URL.format(week, page_id))
    print('{} | '.format(page_id * 50), end='', flush=True)
    data = json.loads(resp.body)
    search_username_rank(data, username)


@gen.coroutine
def get_user_rank_tornado(week, username):
    yield [fetch_and_parse(week, i, username) for i in PAGE_LIST]


def tornado_entry(week, username):
    io_loop = tornado.ioloop.IOLoop.current()
    func = functools.partial(get_user_rank_tornado, week, username)
    io_loop.run_sync(func)


###################
# multiprocessing #
###################

def fetch_and_parse_multi_processing(week, page_id, username, event):
    if not event.is_set():
        print('{} | '.format(page_id * 50), end='', flush=True)
        data = requests.get(RANK_URL.format(week, page_id)).json()
        if search_username_rank(data, username, sys_exit=False):
            event.set()


def get_user_rank_by_multiprocessing(week, username):
    cpu_count = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(cpu_count)
    event = multiprocessing.Manager().Event()

    for page_id in PAGE_LIST:
        pool.apply_async(fetch_and_parse_multi_processing,
                         args=(week, page_id, username, event))

    pool.close()
    event.wait()
    pool.terminate()


##########
# gevent #
##########

def fetch_and_parse_gevent(week, page_id, username):
    print('{} | '.format(page_id * 50), end='', flush=True)
    data = requests.get(RANK_URL.format(week, page_id)).json()
    search_username_rank(data, username)


def get_user_rank_by_gevent(week, username):
    from gevent import monkey
    monkey.patch_all()
    importlib.reload(requests)

    jobs = [gevent.spawn(fetch_and_parse_gevent, week, page_id, username)
            for page_id in PAGE_LIST]
    gevent.joinall(jobs, timeout=10)


REGISTRY = {
    'aio': functools.partial(asyncio_entry, get_user_rank),
    'aioco': functools.partial(asyncio_entry, get_user_rank_by_async_coroutine),
    'uvloop': asyncio_with_uvloop_entry,
    'tornado': tornado_entry,
    'process': get_user_rank_by_multiprocessing,
    'gevent': get_user_rank_by_gevent,
}


if __name__ == '__main__':
    start_time = time.time()
    week_list = requests.get(WEEK_URL).json()
    latest_week = week_list['contests'][0]['title'].split(' ')[-1]
    print('LeetCode Weekly Contest {} (fetch in {:.3f}s)\n'.format(
        latest_week, time.time() - start_time)
    )

    parser = argparse.ArgumentParser()
    parser.add_argument('--user', type=str, default='leohowell')
    parser.add_argument('--week', type=int, default=latest_week)
    parser.add_argument('--engine', type=str, default='uvloop', required=False)
    cli_args = parser.parse_args()

    if cli_args.engine in REGISTRY:
        REGISTRY[cli_args.engine](cli_args.week,cli_args.user)
        print('Finished in {:.3f}s'.format(time.time() - START))
    else:
        print('[error] --core argument: {}'.format(cli_args.engine))
