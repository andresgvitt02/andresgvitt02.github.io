#Uma loja de roupas está com uma promoção de 20% de desconto em todos os produtos. Uma blusa
#custava R$ 80, quanto ela custará agora?

#Entrada de dados
preco_original = 80
valor_desconto = 20

#calcula preço final com desconto aplicado
preco_final = ((preco_original * valor_desconto)/100)
preço_com_desconto = (preco_original - preco_final)

#imprime o preco final com desconto aplicado
print("o preco final do produto é: r$", preço_com_desconto)