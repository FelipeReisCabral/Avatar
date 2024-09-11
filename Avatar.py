import requests
from googletrans import Translator

# Este script busca informações de personagens da série Avatar: The Last Airbender em uma API,
# traduz os nomes e afiliações para o português e imprime os resultados.


def traduzir(texto, src='en', dest='pt'):
    """
    -> Traduz o texto de inglês para Portugues
    :param texto: Texto a ser traduzido
    :param src: idioma original (padrão Ingles)
    :param dest: idioma de origem (padrão Portugues)
    :return: testo traduzido
    """
    try:
        translator = Translator()
        return translator.translate(texto, src=src, dest=dest).text
    except Exception as e:
        print(f'Erro ao traduzir: {e}')
        return 'Erro na tradução'


# URL da API que contém informações sobre personagens de Avatar: The Last Airbender
# Faz a requisição à API e obtém a resposta em formato JSON
resposta = requests.get('https://last-airbender-api.fly.dev/api/v1/characters').json()

# Itera sobre cada personagem e imprime as informações pedidas traduzidas
for personagem in resposta:
    personagem["name"] = traduzir(personagem["name"])
    if 'affiliation' in personagem:
        personagem["affiliation"] = traduzir(personagem["affiliation"])
    else:
        personagem["affiliation"] = 'personagem sem nação'
    print(f'''{'-'*30}
    Nome: {personagem["name"]}
    Nação: {personagem["affiliation"]}''')
