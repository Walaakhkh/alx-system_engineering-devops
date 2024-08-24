#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'custom:subscribers_count:v1.0 (by /u/yourusername)'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            if "data" in data and "subscribers" in data["data"]:
                return data["data"]["subscribers"]
            else:
                return 0
        else:
            return 0
    except requests.RequestException:
        return 0
