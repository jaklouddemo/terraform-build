#!/usr/bin/env python3

import json
import requests
from requests.exceptions import HTTPError

token_file = '../jaklouddemo-api-tokens.json'

def import_json(json_file):
    with open(json_file, 'r') as f:
        json_data = json.load(f)
    return json_data

auth_data = import_json(token_file)
token = auth_data['terraform_cloud']

headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/vnd.api+json'
    }

json_str = """
{
    "data": {
        "attributes": {
            "name": "workspace-3"
        },
    "type": "workspaces"
  }    
}
"""


def get_endpoint(endpoint_path):
    api_base_url = 'https://app.terraform.io/api/v2/'
    endpoint = api_base_url + endpoint_path
    return endpoint

def send_api_request(endpoint_url, request_method):
    json_data = json.loads(json_str)
    try:
        if request_method == 'GET':
            response = requests.get(endpoint_url, headers=headers)
        elif request_method == 'POST':
            response = requests.post(endpoint_url, json=json_data, headers=headers)
        else:
            return 'Invalid request_method, exiting'
            exit()
        response.raise_for_status()
    except HTTPError as http_err:
        return f'HTTP error occurred: {http_err}'
    except Exception as err:
        return f'Other error occurred: {err}'
    else:
        return json.loads(response.text)

request_method = 'GET'
endpoint_url = get_endpoint('organizations/jaklouddemo/workspaces')
result = send_api_request(endpoint_url, request_method)

for i in result['data']:
    print(i['attributes']['name'])