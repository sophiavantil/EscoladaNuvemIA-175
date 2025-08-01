def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

valor_total_conta = float(input("Informe o valor total da conta: "))
gorjeta_percentual = float(input("Informe o valor da gorjeta: "))

gorjeta = calcular_gorjeta(valor_total_conta, gorjeta_percentual)

print(f"O valor da gorjeta é: R${gorjeta:.2f}")