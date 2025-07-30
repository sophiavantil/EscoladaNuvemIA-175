def registrar_notas_alunos():
    notas = []

    while True:
        entrada = input("Digite a nota do aluno ou 'fim' para encerrar: ")

        if entrada.lower() == 'fim':
            break

        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                nota.append(nota)
            else:
                print("Nota inválida! Digite um valor de 0 a 10.")
        except ValueError:
            print("Erro! Digite um número ou 'fim' para encerrar.")

    if notas:
        media = sum(notas) / len(notas)
        print(f"\nMédia da turma: {media:.2f}")
    else:
        print("\nNenhuma nota válida foi registrada.")
        print("Fim do programa.")

registrar_notas_alunos()