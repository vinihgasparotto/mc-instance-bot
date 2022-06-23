# lets_cloud.py
import os

import requests
import json
from dotenv import load_dotenv

load_dotenv()
LETS_CLOUD_TOKEN = os.getenv('LETS_CLOUD_TOKEN')
INSTANCE_ID = os.getenv('INSTANCE_ID')

def instance_details():
    url = 'https://core.letscloud.io/api/instances/' + INSTANCE_ID
    headers = {
        "api-token": LETS_CLOUD_TOKEN,
        "Content-Type": "application/json"
    }
    response = requests.get(url=url, headers=headers, verify=False)
    return response

def instance_power_on():
    url = 'https://core.letscloud.io/api/instances/' + INSTANCE_ID + '/power-on'
    headers = {
        "api-token": LETS_CLOUD_TOKEN,
        "Content-Type": "application/json"
    }
    response = requests.put(url=url, headers=headers, verify=False)
    return response

def instance_power_off():
    url = 'https://core.letscloud.io/api/instances/' + INSTANCE_ID + '/power-off'
    headers = {
        "api-token": LETS_CLOUD_TOKEN,
        "Content-Type": "application/json"
    }
    response = requests.put(url=url, headers=headers, verify=False)
    return response

def instance_reboot():
    url = 'https://core.letscloud.io/api/instances/' + INSTANCE_ID + '/reboot'
    headers = {
        "api-token": LETS_CLOUD_TOKEN,
        "Content-Type": "application/json"
    }
    response = requests.put(url=url, headers=headers, verify=False)
    return response