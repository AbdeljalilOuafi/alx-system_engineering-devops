#!/usr/bin/python3
"""Top ten subreddit posts API Call"""
import requests


def top_ten(subreddit):
    """Fetch top 10 posts from a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Linux x86_64) Edge109.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print("None")
        return

    response_json = response.json()
    for post in response_json["data"]["children"]:
        print(i, post["data"]["title"])
