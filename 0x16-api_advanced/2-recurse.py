#!/usr/bin/python3
"""Fetches titles of hot posts from a given Reddit subreddit.

This module provides a function to recursively retrieve hot post titles from a Reddit subreddit.
"""

import requests

def recurse(subreddit, hot_list=[], after='', count=0):
    """Return a list of titles of hot posts from a subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list, optional): A list to accumulate post titles. Defaults to an empty list.
        after (str, optional): Token used for pagination. Defaults to an empty string.
        count (int, optional): Current count of retrieved posts. Defaults to 0.

    Returns:
        list: A list of post titles from the hot section of the subreddit.
    """
    # Construct the URL for the subreddit's hot posts in JSON format
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # Define headers for the HTTP request, including User-Agent
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # Define parameters for the request, including pagination and limit
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    # Send a GET request to the subreddit's hot posts page
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # Check if the response status code indicates a not-found error (404)
    if response.status_code == 404:
        return None

    # Parse the JSON response and extract relevant data
    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")

    # Append post titles to the hot_list
    for child in results.get("children"):
        hot_list.append(child.get("data").get("title"))

    # If there are more posts to retrieve, recursively call the function
    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    # Return the final list of hot post titles
    return hot_list

