import re
import os

def criar_login():
    login = input("Crie o nome de login: ")
    return login

def criar_senha():
    while True:
        senha = input("A senha deve conter no mínimo:\n- 8 caracteres\n- 1 letra maiúscula\n- 1 caractere especial\n- 1 número\nDigite a senha: ")
        if len(senha) < 8 or not re.search(r"\d", senha) or not re.search(r"[A-Z]", senha) or not re.search(r"[!@#$%^&*().]", senha):
            print("A senha deve conter pelo menos 8 caracteres, 1 letra maiúscula, 1 caractere especial e 1 número.")
            continue
        break
    return senha

def banco_de_dados(login, senha):
    with open("banco_de_dados.txt", "a") as arquivo:
        arquivo.write(f"Nome de login: {login}\n")
        arquivo.write(f"Senha: {senha}\n")
        arquivo.write("-------------------------\n")
    print("Sucesso! Usuário e senha salvos com sucesso")
    os.system('cls')  # Limpa o terminal (apenas para Windows)

def fazer_login():
    while True:
        login = input("Digite o nome de login: ")
        senha = input("Digite a senha: ")
        with open("banco_de_dados.txt", "r") as arquivo:
            conteudo = arquivo.read()
            if f"Nome de login: {login}\n" in conteudo and f"Senha: {senha}\n" in conteudo:
                print("Login bem-sucedido!")
                return  # Retorna para encerrar a função quando o login é válido
            else:
                print("Nome de login ou senha incorretos")

escolha = input("Deseja criar uma conta (c) ou fazer login (l)? ").lower()

if escolha == "c":
    nome_login = criar_login()
    senha = criar_senha()
    banco_de_dados(nome_login, senha)
    print("Sua conta foi criada")

    while True:
        resposta = input("Deseja fazer login? (s/n): ").lower()

        if resposta in ['s', 'sim', 'yes']:
            fazer_login()
            print ("Obrigado por ter feito login em nosso sistema!!!")
            break
        elif resposta in ['n', 'nao', 'no']:
            print("Ok, encerrando o programa...")
            break
        else:
            print("Resposta inválida. Por favor, responda com 's' para sim ou 'n' para não.")

elif escolha == "l":
    fazer_login()
    os.system('cls')
    print ("Obrigado por ter feito login em nosso sistema!!!")
else:
    print("Escolha inválida. Encerrando o programa.")
