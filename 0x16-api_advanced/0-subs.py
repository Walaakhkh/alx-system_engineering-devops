#!/usr/bin/python3
""" function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit. If an invalid
subreddit is given, the function should return 0"""

import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers for a given subreddit."""
    # Define the URL for the subreddit
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Set the User-Agent header to avoid Too Many Requests errors
    headers = {
        'User-Agent': 'python:subreddit.subscriber.counter:v1.0 (by /u/yourusername)'
    }

    try:
        # Make the GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the response status is 200 (OK)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Return the number of subscribers
            return data['data'].get('subscribers', 0)
        else:
            # If not a valid subreddit, return 0
            return 0
    except requests.RequestException:
        # If there is any network-related error, return 0
        return 0
