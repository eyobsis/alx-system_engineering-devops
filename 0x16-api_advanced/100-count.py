#!/usr/bin/python3
"""
Countoccurrences of specified words in the titles of hot articles on Reddit.
"""
import requests


def update_word_counts(response, target_words, word_counts, after):
    """Update word counts from the titles in the Reddit API response."""
    titles = response.json().get("data").get("children")
    for title_info in titles:
        title = title_info.get("data").get("title")
        if title:
            words_in_title = title.split()
            for word_title in words_in_title:
                for target_word in target_words:
                    if target_word.lower() == word_title.lower():
                        word_counts[target_word] += 1

    if not after:
        for word, count in sorted(word_counts.items(),
                                  key=lambda item: (item[1], item[0]),
                                  reverse=True):
            if count != 0:
                print("{}: {}".format(word, count))


def count_words(subreddit, target_words, after=None, word_counts={}):
    """
    Recursively query the Reddit API, parse titles of hot articles, and
    print a sorted count of given keywords.
    """
    headers = {'User-Agent': 'DiegoOrejuela'}
    params = {"limit": 100, 'after': after}
    response = requests.get("https://www.reddit.com/r/{}/hot/.json".
                            format(subreddit), headers=headers, params=params)

    if not word_counts:
        word_counts = {word: 0 for word in target_words}

    if response.status_code == 200:
        after_response = response.json().get("data").get("after")
        if after_response:
            count_words(subreddit, target_words,
                        after=after_response, word_counts=word_counts)
            update_word_counts(response, target_words, word_counts, after)
            return word_counts
        else:
            update_word_counts(response, target_words, word_counts, after)
            return word_counts
    else:
        return None
