import requests
from tabulate import tabulate
from getpass import getpass

matricula = input("Informe sua Matrícula: ")
senha = getpass("Informe sua Senha: ")

url_autenticacao = "https://suap.ifrn.edu.br/api/v2/autenticacao/token/"
autenticacao_resposta = requests.post(url_autenticacao, data={"username": matricula, "password": senha})

if autenticacao_resposta.status_code == 200:
    dados_token = autenticacao_resposta.json()
    chave_api = dados_token["access"]
    token_atualizacao = dados_token["refresh"]
    print("Autenticação realizada com sucesso!")
else:
    print(f"Falha na autenticação. Erro em: {autenticacao_resposta.status_code}: {autenticacao_resposta.text}")
    exit()

def atualizar_token():
    url_atualizacao = "https://suap.ifrn.edu.br/api/v2/autenticacao/token/refresh/"
    resposta = requests.post(url_atualizacao, data={"refresh": token_atualizacao})

    if resposta.status_code == 200:
        novo_token = resposta.json()["access"]
        return novo_token
    else:
        print(f"Erro ao atualizar o token: {resposta.status_code}")
        return None

def buscar_boletim(ano, periodo):
    global chave_api
    headers = {"Authorization": f"Bearer {chave_api}"}
    url_boletim = f"https://suap.ifrn.edu.br/api/v2/minhas-informacoes/boletim/{ano}/{periodo}/"

    resposta = requests.get(url_boletim, headers=headers)
    
    if resposta.status_code == 401:
        chave_api = atualizar_token()
        if chave_api:
            headers["Authorization"] = f"Bearer {chave_api}"
            resposta = requests.get(url_boletim, headers=headers)
    
    if resposta.status_code == 200:
        return resposta.json()
    else:
        print(f"Erro ao acessar o boletim: {resposta.status_code}")
        return None

def exibir_boletim(dados_boletim):
    if not dados_boletim:
        print("Boletim não encontrado. ")
        return
    
    tabela = []
    for disciplina in dados_boletim:
        tabela.append([
            disciplina.get("disciplina", "Indisponível"),
            disciplina.get("nota_etapa_1", "-"),
            disciplina.get("nota_etapa_2", "-"),
            disciplina.get("nota_etapa_3", "-"),
            disciplina.get("nota_etapa_4", "-"),
            disciplina.get("media_disciplina", "-")
        ])
    
    print(tabulate(tabela, headers=["Disciplina", " NOTA 1", "NOTA 2", "NOTA 3", "NOTA 4", "MÉDIA"], tablefmt="fancy_grid"))

ano = int(input("Ano Letivo: "))
periodo = 1 # define o período como 1, primeiro semestre

dados_boletim = buscar_boletim(ano, periodo) # busca o boletim
if dados_boletim:
    exibir_boletim(dados_boletim)
else:
    print("Não foi possível procurar o boletim.")
