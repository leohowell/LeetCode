# -*- coding: utf-8 -*-

import argparse

import requests


URL = 'https://leetcode.com/contest/api/ranking/' \
      'leetcode-weekly-contest-{}/?pagination={}'


def print_rank(data):
    print('+{0} LeetCode Rank {0}+'.format('-'*15))
    for k, v in data.items():
        print('|{:>15}: {:<28}|'.format(k, str(v)))
    print('+{}+'.format('-'*45))


def get_user_rank(week, username):
    for i in range(1, 20):
        url = URL.format(week, i)
        data = requests.get(url).json()
        for user in data['total_rank']:
            if user['username'] == username:
                print_rank(user)
                return
        print("Rank out of {}".format(i * 50))
    print("It's no need show the rest result.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('week', type=int)
    parser.add_argument('username', type=str)
    args = parser.parse_args()
    get_user_rank(args.week, args.username)
