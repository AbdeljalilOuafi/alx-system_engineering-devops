#!/usr/bin/python3

import sys
import json

if __name__ == '__main__':
    recurse = __import__('2-recurse').recurse
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            with open("HollowKnight_hot_posts", mode='x') as f:
                json.dump(result, f)
        else:
            print("None")
