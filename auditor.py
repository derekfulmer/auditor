#!/usr/bin/env python3

import os
import json
import logging
import requests
from copy import copy
from dotenv import load_dotenv  # Commented out because not in use yet


''' 
Rewrite github_audit.sh in Python 3.8.2 using the requests model to make API calls to GitHub. 
A module to process text similar to the combination of grep/sed/awk.
Store credentials as environment variables and call them from the script
'''
logging.basicConfig()  # Added so I can set logging to debug.
log = logging.getLogger('auditor')
log.setLevel(logging.INFO)

HEADERS = {'accept': 'application/vnd.github.v3+json'}  # Docs recommend passing this in the headers


def fetch_logins(url, username, token, headers={}, per_page=30):
    """
    :param url: The API URL endpoint
    :param username: your GitHub username
    :param token: Your API token (https://github.com/settings/tokens)
    :param headers: Any additional headers to include
    :param per_page: The maximum number of results to request from GitHub at a time (max 100, note 'all' in return val)
    :return: List of ALL members that are 'Users'
    """
    # auth = requests.auth.HTTPBasicAuth(username, token)  # `requests` lib was updated so you can just pass a tuple
    combined_headers = copy(HEADERS)  # copy() to avoid an indirect update of HEADERS
    combined_headers.update(headers)

    page = 1  # They don't number from 0 because they hate conventions apparently.
    members = []
    member_data = True
    while member_data:
        # Setting per_page to 5 to force pagination because I'm not a member of an org with > 100 people.
        # TODO: exception handling for failed 'get' request.
        r = requests.get(url, auth=(username, token), headers=combined_headers,
                         params={'per_page': per_page, 'page': page})

        # TODO: check for non-2XX status code and bail out and/or backoff retry
        log.debug('Request status code: %s' % r.status_code)
        log.debug(json.dumps(r.json(), indent=2))

        # TODO (maybe): Handle response that isn't valid json
        member_data = r.json()

        # TODO: GitHub has the power to change what the keys are. We should bail out if they're not found
        # and they should be treated as constant variables so all uses can be updated in a single place
        just_users = filter(lambda d: d['type'] == 'User', member_data)
        members += [d['login'] for d in just_users]
        page += 1
        log.debug(members)

        all_members =  '\n'.join(members)

    return all_members


def main():
    load_dotenv()  # Consider providing an absolute path.
    username = os.getenv('GITHUB_USERNAME')
    token = os.getenv('GITHUB_TOKEN')
    organization = os.getenv('GITHUB_ORGANIZATION')
    log.debug('User: %s' % username)
    log.debug('Org: %s' % organization)

    if not all([username, token, organization]):
        log.critical('ERROR: Have your GitHub credentials and target ORG been exported as environment variables? '
                     'You need your GitHub username and a Personal Access Token which acts as your password.')
        exit(1)

    url = 'https://api.github.com/orgs/{ORG}/members'.format(ORG=organization)
    members = fetch_logins(url, username, token)
    
    with open('all_members.txt', 'w') as f:
        f.write(members)

    # TODO: Add some error checking to validate the print() statement below 
    print('All members of your organization have been to a file in the current working directory.')

if __name__ == '__main__':
    main()
