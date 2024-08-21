import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_user_input(prompt):
    return input(prompt)

def listar_usuarios():
    response = requests.get(f"{BASE_URL}/users")
    if response.status_code == 200:
        usuarios = response.json()
        for usuario in usuarios:
            print(f"{usuario['id']}: {usuario['name']} ({usuario['username']}) - {usuario['email']}")
    else:
        print("Erro ao listar usuários.")

def listar_tarefas_usuario():
    user_id = get_user_input("Digite o ID do usuário, por favor: ")
    response = requests.get(f"{BASE_URL}/users/{user_id}/todos")
    if response.status_code == 200:
        tarefas = response.json()
        for tarefa in tarefas:
            status = "OK" if tarefa['completed'] else "X"
            print(f"[{status}] {tarefa['title']}")
    else:
        print("Erro ao listar as tarefas do usuário.")


def criar_usuario():
    nome = get_user_input("Digite o nome: ")
    username = get_user_input("Digite o sobrenome do usuário: ")
    email = get_user_input("Digite o e-mail: ")

    dados_usuario = {
        "name": nome,
        "username": username,
        "email": email
    }

    response = requests.post(f"{BASE_URL}/users", json=dados_usuario)
    if response.status_code == 201:
        print("Usuário criado com sucesso!", response.json())
    else:
        print("Erro ao criar usuário.")

def ler_usuario():
    user_id = get_user_input("Digite o ID do usuário: ")
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    if response.status_code == 200:
        usuario = response.json()
        print(usuario)
    else:
        print("Usuário não encontrado.")

def atualizar_usuario():
    user_id = get_user_input("Digite o ID do usuário: ")
    nome = get_user_input("Digite o novo nome: ")
    username = get_user_input("Digite o novo sobrenome de usuário: ")
    email = get_user_input("Digite o novo e-mail: ")

    dados_usuario = {
        "name": nome,
        "username": username,
        "email": email
    }

    response = requests.put(f"{BASE_URL}/users/{user_id}", json=dados_usuario)
    if response.status_code == 200:
        print("Usuário atualizado com sucesso!", response.json())
    else:
        print("Erro ao atualizar usuário.")

def deletar_usuario():
    user_id = get_user_input("Digite o ID do usuário: ")
    response = requests.delete(f"{BASE_URL}/users/{user_id}")
    if response.status_code == 200:
        print(f"Usuário com ID {user_id} deletado com sucesso!")
    else:
        print("Erro ao deletar usuário.")

def main():
    acoes = {
        "1": listar_usuarios,
        "2": listar_tarefas_usuario,
        "3": criar_usuario,
        "4": ler_usuario,
        "5": atualizar_usuario,
        "6": deletar_usuario
    }

    while True:
        ops = get_user_input(
            "\n1. Listar usuários\n2. Listar tarefas\n3. Criar usuário\n4. Ler usuário\n5. Atualizar usuário\n6. Deletar usuário\n7. Sair\nDigite sua opção: "
        )
        if ops == "7":
            print("Você saiu do menu! ")
            break
        elif ops in acoes:
            acoes[ops]()
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
