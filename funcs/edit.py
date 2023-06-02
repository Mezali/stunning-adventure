import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def editFuncionario(ip, nome,
                    # cpf, enable,
                    grupo1='', grupo2=''
                    # , grupo3='', grupo4='', grupo5='', grupo6=''
                    ):
    url = f'https://{ip}:8090/portaria/v1/bravas/config/user/'
    out = ''
    payload = {
        "config": {
            "action": "editUser",
            "target": {
                "name": f"{nome}"
            },
            #        "enabled": f"{enable}",
            #        "info": {
            #            "cpf": f"{cpf}"
            #        },
            "groups": [
                f"{grupo1}",
                f"{grupo2}",
                #            f"{grupo3}",
                #            f"{grupo4}",
                #            f"{grupo5}",
                #            f"{grupo6}"
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
