#3. Escreva um programa que receba uma lista de números do usuário e calcule a
#soma de todos os números presentes na lista.

lista = []
while True:
    numero = int(input("Digite os núemros que deseja calcular:"))
    lista.append(numero)

    #Sum serve para somar os números
    soma = sum(lista)

    print(soma)

