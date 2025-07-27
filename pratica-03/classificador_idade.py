idade = int(input("Digite a sua idade: "))

if idade <= 12: 
    print("Você é criança.")

elif 13 <= idade <= 17: 
    print("Você é adolescente.")

elif 18 <= idade <= 59:
    print("Você é adulto.")
    
else:
    print("Você é idoso.")