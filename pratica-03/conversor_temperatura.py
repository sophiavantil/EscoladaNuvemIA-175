temperatura = float(input("Informe a temperatura somente com números: "))
unidade_origem = input("Informe a unidade de origem: ")
unidade_conversao = input("Informe a unidade para qual deseja converter: ")

if unidade_origem == unidade_conversao:
    print("A temperatura continua a mesma.")
    
elif unidade_origem == "C" and unidade_conversao == "F":
    resultado = (temperatura * 9/5) + 32
    print(f"A temperatura em Fahrenheit é: {resultado:.2f}°F")

elif unidade_origem == "C" and unidade_conversao == "K":
    resultado = temperatura + 273.15
    print(f"A temperatura em Kelvin é: {resultado:.2f}K")

elif unidade_origem == "F" and unidade_conversao == "C":
    resultado = (temperatura - 32) * 5/9
    print(f"A temperatura em Celsius é: {resultado:.2f}°C")

elif unidade_origem == "F" and unidade_conversao == "K":
    resultado = (temperatura - 32) * 5/9 + 273.15
    print(f"A temperatura em Kelvin é: {resultado:.2f}K")

elif unidade_origem == "K" and unidade_conversao == "C":
    resultado = temperatura - 273.15
    print(f"A temperatura em Celsius é: {resultado:.2f}°C")

elif unidade_origem == "K" and unidade_conversao == "F":
    resultado = (temperatura - 273.15) * 9/5 + 32
    print(f" A temperatura em Fahrenheit é: {resultado:.2f}°F")

else:
    print("Unidade inválida!!! Use somente C, F ou K.")