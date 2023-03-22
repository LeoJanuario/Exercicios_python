#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input('Digite o valor da sua hora trabalhada: '))
hora_mes = int(input('Quantas horas você trabalha por mês? '))

salario = valor_hora * hora_mes

print(f'O valor do seu salario por mês será de: {salario}')
