lista = []
while True:
    nome = input("Digite um nome: ")
    if nome == "sair":
        break
    else:
        lista.append(nome)

teste = 0
maior = []
for item in lista:
    if len(item) >= teste:
        teste = len(item)
        maior.append(item)

print (lista)
