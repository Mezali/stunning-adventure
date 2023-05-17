import requests


def editFuncionario(nome, enable, tag, grupo1, grupo2='', ip='192.168.1.99'):
    url = f'https://{ip}:8090/portaria/v1/bravas/config/user/'
    out = ''
    payload = {
        "config": {
            "action": "editUser",
            "target": {
                "name": f"{nome}"
            },
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
