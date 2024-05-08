#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers (not active
    users, total subscribers) for a given subreddit.

    Args:
        subreddit (str): The subreddit to query subscribers for.

    Returns:
        int: The total number of subscribers for the given subreddit. If the
        request fails or the subreddit does not exist, returns 0.

    Raises:
        Exception: If an error occurs during the API request.

    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Chrome 121"}

    try:
        r = requests.get(url, headers=headers, allow_redirects=False)
        if r.status_code == 200:
            data = r.json()
            return data['data']['subscribers']
        return 0
    except Exception as e:
        return 0
