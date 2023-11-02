#4. Escreva um programa que receba uma lista de números do usuário e calcule a
#média de todos os números presentes na lista.

lista = []

while True:
    numero = int(input("Digite os números que deseja calcular:"))
    lista.append(numero)

    soma = sum(lista)
    print(soma)

    contagem = len(lista)
    media = soma / contagem

    print(media)

