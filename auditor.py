#!/usr/bin/env python3

import os
import logging
import requests
from dotenv import load_dotenv


''' 
Rewrite github_audit.sh in Python 3.8.2 using the requests modle to make API calls to GitHub. 
A module to process text similar to the combination of grep/sed/awk.
Store credentials as environment variables and call them from the script
'''
log = logging.getLogger('auditor')
log.setLevel(logging.INFO)

try:
    load_dotenv() # Consider providing an absolute path.
    username = os.getenv('GITHUB_USERNAME')
    token = os.getenv('GITHUB_TOKEN')
except:
    logging.critical("ERROR: Have your GitHub credentials been exported as environment variables? You need your GitHub username and a Personal Acces Token which acts as your password.")
    exit(1)


def fetch_users():
    url = 'https://api.github.com/orgs/BLC/members'
    auth = requests.auth.HTTPBasicAuth(username, token)

    r = requests.get(url, auth=auth)
    #response = r.json()
    
    # This works, but only for the first 'page' of users returned in the response.
    # TODO: Paginate through all users using requests 'links' feature between the first and last page. Write it so that you aren't hardcoding the pages to the API call in case the list of pages grows in the future.
    #if r.links['url'] != r.links['last']:
    current_link = r
    last_link = r.links['last']['url']
    
    while current_link != last_link:
        # Do GET requests
        [ i['login'] for i in r.json() ]

def write_user_file():
    # Use the data from fetch_users() to write to a new file.
    with open(fetch_users()) as f:
        pass
    pass

def fetch_repos():
    # Fetch repos by name.
    pass


if __name__ == '__main__':
    fetch_users()
