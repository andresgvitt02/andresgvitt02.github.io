#7. Escreva um programa que receba uma lista de números do usuário e imprima
#apenas os números que são múltiplos de 3 e 5 simultaneamente.
numeros = input("Digite uma lista de números separados por vírgula: ").split()

for numero in numeros:
    numero = int(numero)
    if numero % 3 == 0 and numero % 5 == 0:
        print(numero)


