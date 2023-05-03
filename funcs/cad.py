import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def cadFuncionario(nome, tag, enable, grupo1, grupo2=''):
    url = 'https://192.168.1.99:8090/portaria/v1/bravas/config/user/'
    out = ''
    payload = {
        "config": {
            "action": "addUser",
            "name": f"{nome}",
            "uuid": f"{tag}",
            "enabled": f"{enable}",
            "groups": [
                f"{grupo1}",
                f"{grupo2}",
                "portaria"
            ],
            "tags": [
                f"{tag}"
            ],
            "picture": {
                "type": "binary",
                #   "data": f"{foto}"  # base64 encoded data
            },
            "readers": [
                "ALL"
            ]
        }
    }
    headers = {
        'Content-type': 'application/vnd.api+json',
        'Accept': 'application/vnd.api+json'
    }
    response = requests.post(url, json=payload, headers=headers, verify=False)
    if response.status_code == 200:
        out += '✅'
    else:
        out += '❌'
        print(response.text)
    return out
