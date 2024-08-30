import requests
from getpass import getpass

api_url = "https://api.github.com/"

username = input("Nome de usuário do GitHub: ")
token = getpass("Token de acesso pessoal do GitHub: ")

headers = {
    "Authorization": f"token {token}"
}

response = requests.get(api_url + "user", headers=headers)

if response.status_code == 200:
    print("Autenticação bem-sucedida!")
else:
    print(f"Falha na autenticação: {response.status_code}")
    exit()

def listar_seguidores():
    response = requests.get(f"{api_url}user/followers", headers=headers)
    if response.status_code == 200:
        seguidores = response.json()
        print("Seguidores:")
        for seguidor in seguidores:
            print(seguidor["login"])
        return [seguidor["login"] for seguidor in seguidores]
    else:
        print(f"Falha ao recuperar seguidores: {response.status_code}")
        return []


def verifica_segue_usuario(usuario):
    response = requests.get(f"{api_url}user/following/{usuario}", headers=headers)
    if response.status_code == 204:
        return True
    elif response.status_code == 404:
        return False
    else:
        print(f"Erro ao verificar o status de seguir: {response.status_code}")
        return False


def seguir_usuario(usuario_para_seguir):
    if verifica_segue_usuario(usuario_para_seguir):
        print(f"Já está seguindo {usuario_para_seguir}.")
        return
    
    response = requests.put(f"{api_url}user/following/{usuario_para_seguir}", headers=headers)
    if response.status_code == 204:
        print(f"Agora você está seguindo {usuario_para_seguir}")
    else:
        print(f"Falha ao seguir {usuario_para_seguir}: {response.status_code}")


def parar_de_seguir_usuario(usuario_para_parar):
    if not verifica_segue_usuario(usuario_para_parar):
        print(f"Você não está seguindo {usuario_para_parar}.")
        return
    
    response = requests.delete(f"{api_url}user/following/{usuario_para_parar}", headers=headers)
    if response.status_code == 204:
        print(f"Você parou de seguir {usuario_para_parar}")
    else:
        print(f"Falha ao parar de seguir {usuario_para_parar}: {response.status_code}")

def menu():
    while True:
        print("\nOpções:")
        print("1. Listar seguidores")
        print("2. Seguir um usuário")
        print("3. Parar de seguir um usuário")
        print("4. Sair")
        try:
            escolha = input("Selecione uma opção: ")
        except EOFError:
            print("\nErro ao ler. ")
            continue
        if escolha == "1":
            listar_seguidores()
        elif escolha == "2":
            usuario_para_seguir = input("Digite o nome de usuário para seguir: ")
            seguir_usuario(usuario_para_seguir)
        elif escolha == "3":
            usuario_para_parar = input("Digite o nome de usuário para deixar de seguir: ")
            parar_de_seguir_usuario(usuario_para_parar)
        elif escolha == "4":
            break
        else:
            print("Opção inválida.")
menu()
