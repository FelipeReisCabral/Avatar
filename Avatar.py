import requests

# Define a URL da API que contém informações sobre personagens do Avatar: The Last Airbender
link = 'https://last-airbender-api.fly.dev/api/v1/characters'

# Faz uma requisição HTTP GET para a URL especificada
# A função requests.get() envia uma solicitação para buscar os dados da API
requisicao = requests.get(link)

# Converte a resposta da API para o formato JSON e imprime no console
# O método json() transforma o conteúdo da resposta, que geralmente é em formato texto,
# para um objeto Python que representa um dicionário JSON.
print(requisicao.json())
