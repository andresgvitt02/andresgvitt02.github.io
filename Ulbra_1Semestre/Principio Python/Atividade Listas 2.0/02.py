lista = []
while True:
    num = int(input("Digite um número: "))

    if num == 0:
        break

    else:
        lista.append(num)

valor = lista[0]
#Procura em toda lista o item
for item in lista:
    if item < valor:
        valor = item
        print(valor)


print(lista)
print(valor)
print(min(lista))



