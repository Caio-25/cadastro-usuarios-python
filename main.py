usuarios = []

def menu():
    print("\n=== MENU ===")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Buscar usuário")
    print("4 - Remover usuário")
    print("0 - Sair")

def cadastrar_usuario():
    nome = input("Nome: ")
    idade = input("Idade: ")
    email = input("Email: ")

    usuario = {
        "nome": nome,
        "idade": idade,
        "email": email
    }

    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

def listar_usuarios():
    if len(usuarios) == 0:
        print("Nenhum usuário cadastrado.")
        return

    print("\nLista de usuários:")
    for i, usuario in enumerate(usuarios, start=1):
        print(f"{i}. Nome: {usuario['nome']} | Idade: {usuario['idade']} | Email: {usuario['email']}")

def buscar_usuario():
    nome_busca = input("Digite o nome do usuário: ")

    for usuario in usuarios:
        if usuario["nome"].lower() == nome_busca.lower():
            print(f"Encontrado: {usuario['nome']} - {usuario['email']}")
            return

    print("Usuário não encontrado.")

def remover_usuario():
    nome_remover = input("Digite o nome do usuário para remover: ")

    for usuario in usuarios:
        if usuario["nome"].lower() == nome_remover.lower():
            usuarios.remove(usuario)
            print("Usuário removido com sucesso!")
            return

    print("Usuário não encontrado.")

# Programa principal
while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_usuario()
    elif opcao == "2":
        listar_usuarios()
    elif opcao == "3":
        buscar_usuario()
    elif opcao == "4":
        remover_usuario()
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida!")