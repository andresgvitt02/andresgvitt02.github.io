
while True:
    numeros = input("Digite uma lista de números separados por espaço: ").split()
    numeros = [int(num) for num in numeros]
    
    print(min(numeros))
