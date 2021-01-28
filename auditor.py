#!/usr/bin/env python3

import os
import logging
import requests
from dotenv import load_dotenv

load_dotenv()

''' 
Rewrite github_audit.sh in Python 3.8.2 using the requests modle to make API calls to GitHub. 
A module to process text similar to the combination of grep/sed/awk.
Store credentials as environment variables and call them from the script
'''
log = logging.getLogger('auditor')
log.setLevel(logging.INFO)

# GitHub credentials should be stored externally from script in a secrets.env file or similar.
try:
    username = os.getenv('GITHUB_USERNAME')
    token = os.getenv('GITHUB_TOKEN')
except:
    logging.critical("ERROR: Have your GitHub credentials been exported as environment variables? You need your GitHub username and a Personal Acces Token which acts as your password.")
    exit(1)

url = 'https://api.github.com/orgs/BLC/members'
auth = requests.auth.HTTPBasicAuth(username, token)

r = requests.get(url, auth=auth)
print(r.json())
