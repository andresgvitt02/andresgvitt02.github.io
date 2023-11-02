#2. Escreva um programa que receba uma lista de nomes do usuário e imprima cada
#nome em uma linha separada.

lista = []
while True:
    nome = input("Digite um nome:")
#Lower serve para aceitar nomes com letra maiúscula e minúscula
    if nome.lower() == "sair":
        break

    else:
        lista.append(nome)

#Imprimir item por item da lista um em cima do outro
for item in lista:
    print(item)
