def encontrar_maior_numero(lista):
    if len(lista) == 0:
        return None

    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero

    return maior

# Obter a entrada do usuário
entrada = input("Digite uma lista de números separados por espaços: ")
numeros = [int(numero) for numero in entrada.split()]

# Chamar a função para encontrar o maior número
maior_numero = encontrar_maior_numero(numeros)

# Verificar se a lista não está vazia
if maior_numero is not None:
    print("O maior número é:", maior_numero)
else:
    print("A lista está vazia.")
