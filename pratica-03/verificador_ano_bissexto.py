ano = int(input("Insira um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é Bissexto.")
    
else:
    print(f"O ano {ano} não é Bissexto.")