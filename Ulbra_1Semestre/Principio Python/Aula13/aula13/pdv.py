#Faça um algoritmo que receba 
pedido = []
descricao = []

#Menu

print("O que deseja comprar hoje?")
print("1-café | 2-água | 3- refri | 4-bolo | 5-finalizar compra | 6-sair")
opcao = int(input("Digite o número do produto: "))

lista = ["café, água, refri, bolo"]

lista2 = [4.50, 3.00, 3.50, 6.00]

if opcao == 1:
    pedido.append(4.00)
    descricao.append("café - R$ 4,00")
elif opcao == 2:
    pedido.append(3.00)
    descricao.append("água - R$ 3,00")
elif opcao ==3:
    pedido.append(5.00)
    descricao.append("refri - R$ 5,00")
elif opcao == 4:
    pedido.append(8.00)
    descricao.append("bolo - R$ 8,00")
elif opcao == 5:
    pedido.append(5.00)
    descricao.append("água - R$ 3,00")
else:
    print("Digite uma opção válida!")