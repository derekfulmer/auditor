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

url = 'https://api.github.com/orgs/ORG/members'

def fetch_logins(url):
    auth = requests.auth.HTTPBasicAuth(username, token)
    r = requests.get(url, auth=auth)
	
	members = []

	# Make a GET request on page 1 and parse the JSON response.	    
	# Make a GET request on page 2 and parse the JSON response.	    
	# Make a GET request on page 3 and parse the JSON response.	    
	# Make a GET request on page 4 and parse the JSON response.	    
	# Make a GET request on page 5 and parse the JSON response.	    

if __name__ == '__main__':
    fetch_logins(url)
