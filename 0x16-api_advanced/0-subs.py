#!/usr/bin/python3
"""This module returns the number of subs a subreddit has"""
import requests

def number_of_subscribers(subreddit):
    """Get the number of subscribers for a subreddit."""
    response = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json")
    if (response.status_code != 200):
        return 0
    result = response.json()
    if "data" in result and "subscribers" in result["data"]:
        return result["data"]["subscribers"]
    else:
        return 0
