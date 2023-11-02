def contar_numeros_pares(lista):
    quantidade_pares = 0
    for numero in lista:
        if numero % 2 == 0:
            quantidade_pares += 1
    return quantidade_pares

entrada = input("Digite uma lista de números separados por espaço: ")
numeros = [int(numero) for numero in entrada.split()]

quantidade_pares = contar_numeros_pares(numeros)
print("A quantidade de números pares na lista é:", quantidade_pares)
