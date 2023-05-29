import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def cadFuncionario(ip, nome, tag, enable, grupo1='', grupo2='', grupo3='', grupo4=''):
    url = f'https://{ip}:8090/portaria/v1/bravas/config/user/'
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
                f"{grupo3}",
                f"{grupo4}"
            ],
            "tags": [
                f"{tag}"
            ],
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
