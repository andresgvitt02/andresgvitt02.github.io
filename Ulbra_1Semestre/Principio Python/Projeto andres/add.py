# Criando uma lista de produtos
produtos = [
    {"nome": "Camiseta", "preco": 29.99},
    {"nome": "Calça jeans", "preco": 59.99},
    {"nome": "Tênis", "preco": 99.99},
    {"nome": "Meias", "preco": 9.99},
    {"nome": "Boné", "preco": 19.99}
]

# Exibindo os produtos disponíveis
print("Produtos disponíveis:")
for produto in produtos:
    print(f"{produto['nome']}: R${produto['preco']:.2f}")

# Pedindo ao usuário que escolha um produto
escolha = int(input("Digite o número do produto desejado: ")) - 1

# Verificando se a escolha é válida
if escolha < 0 or escolha >= len(produtos):
    print("Escolha inválida!")
else:
    produto_escolhido = produtos[escolha]
    print(f"Produto escolhido: {produto_escolhido['nome']}")

    # Realizando o pagamento
    pagamento = float(input("Digite o valor do pagamento: "))

    if pagamento >= produto_escolhido['preco']:
        troco = pagamento - produto_escolhido['preco']
        print(f"Troco: R${troco:.2f}")
    else:
        falta = produto_escolhido['preco'] - pagamento
        print(f"Falta: R${falta:.2f}")
