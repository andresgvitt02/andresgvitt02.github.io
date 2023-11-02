#6. Escreva um programa que receba uma lista de números do usuário e imprima
#apenas os números ímpares presentes na lista.
lista = []

while True:
    numero = int(input("Digite um número:"))
    lista.append(numero)

    for i in lista:
       if i % 2 != 0:
           print(i)
           