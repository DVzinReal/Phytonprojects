import requests
'''
buscar dados de uma api
api (interface de programação de aplicações)
permite que diferentes sistemas se comuniquem
'''

resposta = requests.get("https://api.github.com")
print("Status code: ", resposta.status_code)
print("Conteúdo: ", resposta.json())