import requests


def deleteFunc(nome, ip):
    url = f'https://{ip}:8090/portaria/v1/bravas/config/user/'
    out = ''
    payload = {
        "config": {
            "action": "deleteUser",
            "target": {
                "name": f"{nome}"
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
