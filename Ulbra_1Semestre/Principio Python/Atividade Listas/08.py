#8. Escreva um programa que receba uma lista de números do usuário e imprima a
#lista em ordem crescente.
# Receber a lista de números do usuário
numeros = input("Digite uma lista de números separados por espaço: ").split()

# Converter os números para inteiros
numeros = [int(num) for num in numeros]

# Ordenar a lista em ordem crescente
numeros.sort()

# Imprimir a lista em ordem crescente
print("Lista em ordem crescente:", numeros)
