def solicitador_numeros_inteiros():
    pares = 0
    impares = 0

    while True:
        entrada = input("Digite um número inteiro ou digite 'Sair' para encerrar o programa: ")

        if entrada.lower() == 'sair':
            break
          
        try:
           numero_inteiro = int(entrada)
        except ValueError:
           print("Erro! Digite um número inteiro.") 
           continue

        if numero_inteiro % 2 == 0:
          pares += 1
          print(f"O número {numero_inteiro} é par!")
        else:
          impares += 1
          print(f"O número {numero_inteiro} é ímpar!")

    print(f"\nVocê digitou {pares} número(s) par(es) e {impares} número(s) ímpar(es).")
    print("Programa encerrado!")

solicitador_numeros_inteiros()