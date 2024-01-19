#!/usr/bin/python3
"""
prints the titles of the first 10 hot posts listed
for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts
    listed for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json?show="all"&limit=10'.format(
        subreddit)
    headers = {'User-Agent': 'Python/1.0(alx School 0x16)'}
    response = requests.get(url, headers=headers)
    try:
        top_ten = response.json()['data']['children']
        for post in top_ten:
            print(post['data']['title'])
    except KeyError:
        print("None")
