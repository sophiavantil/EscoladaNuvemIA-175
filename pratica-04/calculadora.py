def calculadora():
    while True:
        try:
            numero1 = float(input("Digite o primeiro número: "))
            break
        except ValueError:
            print("Entrada inválida! Digite um número válido.")

    while True:
        try:
            numero2 = float(input("Digite o segundo número: "))
            break
        except ValueError:
            print("Entrada inválida! Digite um número válido.")

    while True:
        operacao = input("Digite a operação que deseja fazer (+, -, *, /): ")
        try:
            if operacao == "+":
                resultado = numero1 + numero2
            elif operacao == "-":
                resultado = numero1 - numero2
            elif operacao == "*":
                resultado = numero1 * numero2
            elif operacao == "/":
                if numero2 == 0:
                  raise ZeroDivisionError("Erro! Não é possível dividir por zero.")
                resultado = numero1 / numero2
            else:
                raise ValueError("Operação inválida! Use +, -, * ou /.")
        except ZeroDivisionError as e:
            print(f"Erro: {e}")

            while True:
                try:
                  numero2 = float(input("Digite um novo valor diferente de zero: "))
                  break
                except ValueError:
                  print("Entrada inválida! Digite um número válido.")
        except ValueError as e:
            print(f"Erro: {e}")
        else:
            print(f"{numero1} {operacao} {numero2} = {resultado} ")
            break

calculadora()