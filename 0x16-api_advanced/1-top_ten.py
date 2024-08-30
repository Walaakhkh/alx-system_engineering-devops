#!/usr/bin/python3
"""  function that queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit."""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    # Define the URL for the hot posts of the subreddit
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    
    # Set the User-Agent header to avoid Too Many Requests errors
    headers = {
        'User-Agent': 'python:subreddit.hot.posts:v1.0 (by /u/yourusername)'
    }

    try:
        # Make the GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the response status is 200 (OK)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            posts = data.get('data', {}).get('children', [])

            # Print the titles of the first 10 hot posts
            for post in posts:
                print(post['data'].get('title'))
        else:
            # If not a valid subreddit, print None
            print(None)
    except requests.RequestException:
        # If there is any network-related error, print None
        print(None)
