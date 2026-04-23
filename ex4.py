senha_correta = "Léo Assis."

while True:
    tentativa = input("Digite um número: ")
    if tentativa == senha_correta:
        print("Acesso liberado!")
        break
    else:
        print("Senha incorreta, tente novamente.")