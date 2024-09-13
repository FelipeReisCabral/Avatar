![Sem Título-1](https://github.com/user-attachments/assets/b8d5e450-8365-4f43-8506-924d9d89c61d)
## Consumindo a API do Avatar: The Last Airbender (7daysofcode)

**Descrição:**

Projeto de um script Python que utiliza uma API para buscar informações dos personagens da série **Avatar: The Last Airbender**, traduz seus nomes e afiliações para o português e imprime as informações formatadas no terminal.



## **Projeto do site _#7daysofcode_**
### _"Construindo uma aplicação back-end utilizando o Python conectando com a API do Avatar"_

**Dia 1:** Consumindo a API de Avatar utilizando o método **requests**, e a resposta em **JSON** que será usada nos próximos dias. (_concluido_)

**Dia 2:** Tratando os dados. Você utilizará a biblioteca **Googletrans** para fazer a tradução de alguns atributos retornados pela **API**. (_**concluido**_)

**Dia 3:** Finalmente, você vai dar o primeiro mergulho com o framework Django! Ele é muito usado para o back-end com Python.(12/09)

**Dia 4:** Chegou a hora de brincar com rotas. Além delas, você criará as views, sempre utilizando a arquitetura MVT.(13/09)

**Dia 5:** Nesse dia, você vai começar a usar o Bootstrap junto ao Django, para desenvolver uma tabela para mostrar cada informação vinda da API.(14/09)

**Dia 6:** Chegando quase no final, você precisará gerar um ID automático utilizando o framework Django.(15/09)

**Dia 7:** No sétimo e último dia do desafio, você deverá fazer uma paginação para o projeto. Dessa forma, você conseguirá mostrar mais personagens além dos que aparecem inicialmente.(16/09)


## 🛠 Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada.
- **Requests**: Biblioteca para realizar requisições HTTP.
- **Googletrans**: Biblioteca usada para tradução dos nomes e afiliações dos personagens de inglês para português.

## 💻 Instalação e Execução

Siga os passos abaixo para executar o projeto em seu ambiente local.

### 1. Clone o Repositório

```
git clone https://github.com/seu-usuario/avatar-characters-translator.git
```


### 2. Navegue até o Diretório do Projeto

```
cd avatar-characters-translator
```
### 3. Instale as Dependências
   
Certifique-se de que você tenha o Python instalado (versão 3.x). Para instalar as bibliotecas necessárias, execute:
```
pip install requests googletrans==3.1.0a0.
```
⚠️ Nota: O googletrans pode ter variações de versão. Recomenda-se usar a versão 3.1.0a0. para evitar problemas de compatibilidade.

### 4. Execute o Script
Após a instalação das dependências, você pode executar o script:

```
python main.py
```

### **🔍O que o Script Faz?**

Realiza uma requisição HTTP à API de Avatar: The Last Airbender.
Traduz os nomes e afiliações dos personagens de inglês para português.
Imprime no terminal as informações formatadas de cada personagem:

```
------------------------------
Nome: Aang
Nação: Nômades do Ar
```

### **⚙️Funcionalidades**

API de Personagens: Busca dados diretamente da API pública da série.
Tradução: Utiliza a biblioteca googletrans para traduzir o conteúdo.
Informações Formatadas: Apresenta nome e afiliação de cada personagem no terminal.

### **📋 Exemplo de Saída**

```
------------------------------
Nome: Katara
Nação: Tribo da Água do Sul

------------------------------
Nome: Zuko
Nação: Nação do Fogo
```

### **🚨 Possíveis Erros**
Erro na tradução: Se houver algum problema na tradução, o script exibirá um erro e seguirá a execução normalmente, mostrando Erro na tradução ao invés do nome ou afiliação.

### **🔧 Contribuindo**
Contribuições são bem-vindas! Se você encontrar algum bug ou tiver sugestões de melhoria, fique à vontade para abrir uma issue ou enviar um pull request.

### **📄 Licença**
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais informações.
