#!/usr/bin/env python3

import os
import requests
from dotenv, import load_env

''' 
Rewrite github_audit.sh in Python 3.8.2 using the requests modle to make API calls to GitHub. 
A module to process text similar to the combination of grep/sed/awk.
Store credentials as environment variables and call them from the script
Publish new file to S3 bucket.
'''

# GitHub credentials should be stored externally from script in a secrets.env file or similar.
username = os.getenv('GITHUB_USERNAME')
token = os.getenv('GITHUB_TOKEN')

def fetch_users():
	url = 'https://api.github.com/orgs/ORG/members'
	auth = requests.auth.HTTPBasicAuth(GITHUB_USERNAME, GITHUB_TOKEN)

	# headers = {'application': 'vnd.github.v3+json'} Are these necessary?

    r = requests.get(url, auth=auth)

