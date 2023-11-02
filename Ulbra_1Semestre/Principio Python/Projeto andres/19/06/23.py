#Faça um algoritmo que receba números um a um, armazene em uma lista 
#e ao sair armazene e imprima os números pares e os impares em lista separadas

todos = []
pares = []
impares = []

def entreveiro(lista, num):
    lista.append(num)

#Entrada de dados 
while True:
    num = int(input("Digite um número: "))

    if num == 0:
        break
    else:
        entreveiro(todos, num)
    
for item in todos:
    if item % 2 == 0:
        entreveiro(pares, item)
    else:
        entreveiro(impares, item)

print(f"Os números pares são: {pares} e os ìmpares são:{impares}")