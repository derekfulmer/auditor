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

def get_creds():
	username = os.getenv('GITHUB_USERNAME')
	token = os.getenv('GITHUB_TOKEN')
	return username token

def fetch_users():
	url = 'https://api.github.com/orgs/ORG/members'
	headers = {'application': 'vnd.github.wyandotte-preview+json'}

	# Basic functionality below to show ability to hit API endpoint.
	r = requests.get(url, headers)

	# Function to fetch GitHub user accounts. Will need to paginate through
	# the api. Can we use HTTP links headers for this?
	# Get all users, parse JSON to return only IDs
	# Return output to function its caller for later use?
	# Write data pulled from API to a file within a context manager?
	pass


