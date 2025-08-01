def calcular_desconto(preco, desconto_percentual):
    desconto = preco * (desconto_percentual / 100)
    preco_final = preco - desconto
    return preco_final

while True:
    try:
        preco_original = float(input("Informe o preço do produto (exemplo: 340.75): "))
        percentual_desconto = float(input("Informe o percentual de desconto (exemplo: 10): "))

        if preco_original < 0 or percentual_desconto < 0:
            print("ERRO: O preço e o desconto precisam ser positivos.")
            continue
        break

    except ValueError:
        print("Por favor, insira um valor numérico: ")

preco_final = calcular_desconto(preco_original, percentual_desconto)

print(f"Preço final com desconto: R$ {preco_final:.2f}")