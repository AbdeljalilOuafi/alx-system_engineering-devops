#!/usr/bin/python3

import requests

def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=9".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Linux x86_64) Edge109.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None
    try:
        response_json = response.json()
    except Exception:
        return None
    for post in response_json["data"]["children"]:
        print(i, post["data"]["title"])
