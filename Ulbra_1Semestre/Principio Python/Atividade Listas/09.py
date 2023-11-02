numeros = input("Digite uma lista de números separados por espaço: ").split()
numeros = [int(num) for num in numeros]  # Converte os números de strings para inteiros
numeros.sort(reverse=True)  # Ordena a lista em ordem decrescente

print("Lista em ordem decrescente:", numeros)
