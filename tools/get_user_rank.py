# -*- coding: utf-8 -*-

import argparse
import asyncio
import sys

import aiohttp


URL = 'https://leetcode.com/contest/api/ranking/' \
      'leetcode-weekly-contest-{}/?pagination={}'


def print_rank(data):
    print('+{0} LeetCode Rank {0}+'.format('-'*15))
    for k, v in data.items():
        print('|{:>15}: {:<28}|'.format(k, str(v)))
    print('+{}+'.format('-'*45))


async def get_user_rank(week, page_id, username):
    async with aiohttp.ClientSession() as session:
        async with session.get(URL.format(week, page_id)) as resp:
            data = await resp.json()
            print('Check rank < {}'.format(page_id * 50))
            for user in data['total_rank']:
                if user['username'] == username:
                    print_rank(user)
                    sys.exit(0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('week', type=int)
    parser.add_argument('username', type=str)
    args = parser.parse_args()

    loop = asyncio.get_event_loop()
    tasks = [get_user_rank(args.week, i, args.username) for i in range(1, 30)]
    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()

