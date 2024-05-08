#!/usr/bin/python3
"""
Queries the Reddit API and returns a list containing the titles of all hot
articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Recursively queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit.

    Args:
    - subreddit (str): The subreddit to get titles from.
    - hot_list (list, optional): A list to store the titles of hot articles.
        Defaults to an empty list.
    - after (str, optional): The fullname of an item in the listing to use as
        the anchor point of the slice. Defaults to an empty string.

    Returns:
    - list: A list containing the titles of all hot articles for the given
        subreddit. If the request fails, returns None.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Chrome 121"}

    try:
        response = requests.get(
            url=url,
            headers=headers,
            params={"after": after},
            allow_redirects=False
            )
        if response.status_code == 200:
            data = response.json()
            children = data['data']['children']
            for child in children:
                hot_list.append(child['data']['title'])
            after = data['data']['after']
            if after is not None:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except Exception as e:
        return None
