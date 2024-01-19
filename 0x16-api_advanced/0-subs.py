#!/usr/bin/python3
"""
Queries Reddit API and returns the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries Reddit API and returns number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: number of subscribers, or 0 if the subreddit is invalids.
    """
    url = f'http://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'CustomUserAgent/1.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()

        if response.status_code == 200:
            return response.json().get('data').get('subscribers', 0)
        else:
            return 0

    except requests.exceptions.RequestException as error:
        print(f"Error: {error}")
        return 0


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        subscribers_count = number_of_subscribers(subreddit_name)
        print(subscribers_count)
