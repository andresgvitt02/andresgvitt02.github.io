numeros = input("Digite uma lista de números separados por espaço: ").split()
numeros = [int(num) for num in numeros]  # Converte os números de strings para inteiros

numero_especifico = int(input("Digite o número específico a ser verificado: "))

if numero_especifico in numeros:
    print("O número", numero_especifico, "está presente na lista.")
else:
    print("O número", numero_especifico, "não está presente na lista.")
