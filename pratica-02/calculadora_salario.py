numero_funcionario = int(input("Informe o seu número de funcionário: "))
horas_trabalhadas = int(input("Informe as horas trabalhadas: "))
valor_por_hora = float(input("Informe o valor recebido por hora: "))

salario = horas_trabalhadas * valor_por_hora

print(f"Número do funcionário = {numero_funcionario}")
print(f"Salário = R$ {salario:.2f}")