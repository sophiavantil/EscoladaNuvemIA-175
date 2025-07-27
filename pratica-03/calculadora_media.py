N1 = float(input())
N2 = float(input())
N3 = float(input())
N4 = float(input())

media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10
print(f"Média: {media:.1f}")

if media >= 7.0: 
    print("Aluno aprovado!")

elif media < 5.0:
    print("Aluno reprovado!")

else:
    print("Aluno em exame.")

    nota_exame = float(input("Digite a nota do exame: "))
    print(f"Nota do exame: {nota_exame:.1f}")

    resultado_final = media + nota_exame / 2

    if resultado_final >= 5.0:
        print("Aluno aprovado!")

    else:
        print("Aluno reprovado!")

    print(f"Média final: {resultado_final:.1f}")
    