import requests

link = 'https://last-airbender-api.fly.dev/api/v1/characters'

requisicao = requests.get(link)
print(requisicao.json())
