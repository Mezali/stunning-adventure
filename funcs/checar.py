import requests
import urllib3
import json
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def checar():
    url = 'https://192.168.1.99:8090/portaria/v1/bravas/biometric'
    payload = {
        "biometric": {
            "command": "status"
        }
    }

    headers = {
        'Content-type': 'application/vnd.api+json',
        'Accept': 'application/vnd.api+json'
    }

    response = requests.post(url, json=payload, headers=headers, verify=False)
    data = json.loads(response.text)
    status = data["biometric"]["info"]["status"]

    return status
