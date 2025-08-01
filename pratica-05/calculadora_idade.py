from datetime import date

def calcular_idade_dias(ano_nascimento):
    ano_atual = date.today().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365
    return idade_dias

try:
    ano = int(input("Digite o seu ano de nascimento: ")) 
    idade_dias = calcular_idade_dias(ano)
    print(f"Você tem aproximadamente {idade_dias} dias de vida.")

except ValueError:
    print("Entrada inválida! Digite um ano válido.")