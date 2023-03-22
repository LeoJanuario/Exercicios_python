#Tendo como dado de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

altura = float(input("Digite a altura em metros: "))
sexo = input("Digite o sexo (m/f): ")

if sexo == "m":
    peso_ideal = (72.7 * altura) - 58
    print("O peso ideal para um homem de altura", altura, "m é:", peso_ideal, "kg.")
elif sexo == "f":
    peso_ideal = (62.1 * altura) - 44.7
    print("O peso ideal para uma mulher de altura", altura, "m é:", peso_ideal, "kg.")
else:
    print("Sexo inválido.")
