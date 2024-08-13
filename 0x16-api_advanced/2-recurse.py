#!/usr/bin/python3

"""Fetch all hot pages for a subreddit"""
import requests


def recurse(subreddit, after=None, hot_list=None):
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
         AppleWebKit/537.36 (KHTML, like Gecko) \
             Chrome/114.0.5735.199 Safari/537.36'}
    params = {'after': after}
    response = requests.get(url=url, headers=headers, params=params)
    if response.status_code != 200:
        return None

    response_json = response.json()
    after = response_json["data"]["after"]

    for post in response_json["data"]["children"]:
        hot_list.append(post["data"]["title"])

    if after is None:
        return hot_list

    return recurse(subreddit, after, hot_list)
