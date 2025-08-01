def verificar_palindromo(texto):
    texto = texto.lower()
    texto = ''.join(letra for letra in texto if letra.isalnum())
    
    if texto == texto[::-1]:
        return "Sim"
    else:
        return "Não"

frase = input("Digite uma palavra ou frase para fazer a verificação: ")

resultado = verificar_palindromo(frase)

print(f"A frase {frase} é um Políndromo? {resultado}")
