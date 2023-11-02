lista = []
cont = 0
pares = []
while True:
    num = int(input("Digite um número:"))

    if num == 0:
        break
    else:
        lista.append(num)

for item in lista:
    if item % 2 == 0:
        cont = cont + 1
        print(lista)

print(f"O total de números pares é: {cont}")
