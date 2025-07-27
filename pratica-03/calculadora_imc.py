peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = peso / altura ** 2

if imc < 18.5:
    print("Você está abaixo do peso.")

elif 18.5 < imc < 25.0: 
    print("Você está com o peso normal.")

elif 25.0 < imc < 30:
    print("Você está com sobrepeso.")
    
else:
    print("Você está obeso.")