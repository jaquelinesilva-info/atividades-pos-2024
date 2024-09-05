import requests
from tabulate import tabulate


username = input("Digite sua Matricula: ")
password = input("Digite sua Senha: ") 

auth_url = "https://suap.ifrn.edu.br/api/v2/autenticacao/token/"


response = requests.post(auth_url, data={"username": username, "password": password})

if response.status_code == 200:
    token_data = response.json()
    api_key = token_data.get("access")
    refresh_token = token_data.get("refresh")
    print("Token obtido com sucesso.")
else:
    print("Erro ao obter o token:", response.status_code, response.text)
    exit(1)

