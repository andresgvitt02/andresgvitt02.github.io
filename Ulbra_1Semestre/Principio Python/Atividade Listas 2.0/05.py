entrada = input("Digite uma lista de números separados por espaço: ")
numeros = [int(numero) for numero in entrada.split()]

quantidade_pares = 0
for numero in numeros:
    if numero % 2 == 0:
        quantidade_pares += 1

print("A quantidade de números pares na lista é:", quantidade_pares)

