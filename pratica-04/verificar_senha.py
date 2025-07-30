def senha_forte(senha):
    tem_numero = False

    for caractere in senha:
        if caractere in "0123456789":
            tem_numero = True
            break

    if len(senha) >= 8 and tem_numero:
        return True
    else:
        return False

while True:
    senha = input("Digite uma senha forte ou digite 'sair' para encerrar o programa: ")

    if senha.lower() == 'sair':
        print("Programa encerrado.")
        break

    if senha_forte(senha):
        print("Senha forte registrada com sucesso!")
        break
    else:
        print("Senha fraca. Ela deve ter pelo menos 8 caracteres e conter pelo menos um número.\n")