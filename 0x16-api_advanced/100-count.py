def count_words(subreddit, word_list, count_dict=None, after=None):
    """
    Queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords.
    """
    import requests

    if count_dict is None:
        count_dict = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data')
        after = data.get('after')
        children = data.get('children')

        for child in children:
            title = child.get('data').get('title').lower()

            for word in word_list:
                if word.lower() in title:
                    if word in count_dict:
                        count_dict[word] += 1
                    else:
                        count_dict[word] = 1

        if after is not None:
            count_words(subreddit, word_list, count_dict, after)

        else:
            sorted_words = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_words:
                print(f"{word}: {count}")

    else:
        print("None")

