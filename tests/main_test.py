import requests
import json

url = "http://127.0.0.1:5000"

endpoints = {
    '1': {
            'url': '/consulta_id/',
            'params': {'id': 2},
            'help': 'consulta dados de uma usina pelo id',
            'status': '',
        },
    '2': {
        'url': '/consulta_condicao/',
        'params': {'condicao': 'id < 10'},
        'help': 'consulta dados de uma usina por condição',
        'status': '',
    },
}

def consultas(url: str):
    for key, value in endpoints.items():
        url_ext = url + value['url']
        response = requests.request("POST", url_ext, params=value['params'])
        value['status'] = response.status_code
        print(response.json())

consultas(url)

for key, value in endpoints.items():
    print(f'{key}:')
    print(f'{value}')
    print('------------------------------------------')
# def consulta_id(url: str):
#     url_ext = url + '/consulta_id/'
#     response = requests.request("POST", url_ext, headers=headers, data=json.dumps(payload))
#     return response.json()
# params = {
#     "id": 2
# }
#
# response = requests.request("POST", url, params=params)
#
# metodos = ['apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url']
# # print(dir(response))
# for metodo in metodos:
#     print(f'{metodo}:')
#     print(f'{getattr(response, metodo)}')
#     print('------------------------------------------')