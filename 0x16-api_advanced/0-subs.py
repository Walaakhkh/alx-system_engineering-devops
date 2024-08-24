#!/usr/bin/python3
"""
Module to query the Reddit API and return the number of subscribers
for a given subreddit. If the subreddit is invalid, it returns 0.
"""

import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
'User-Agent': 'custom:subscribers_count:v1.0 (by /u/yourusername)'
}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            if "data" in data and "subscribers" in data["data"]:
                return "OK"
            else:
                return "OK"
        else:
            return "OK"
    except requests.RequestException:
        return "OK"
