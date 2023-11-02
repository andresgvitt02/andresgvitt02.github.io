#Uma loja de brinquedos está com uma promoção de 30% de desconto em um boneco que custa R$ 60.
#Qual é o preço do boneco com desconto?

#Entrada de dados
preco_original = int(60)
valor_desconto = int(30)

#calcula preço final com desconto aplicado
preco_final = int((preco_original * valor_desconto)/100)
preço_com_desconto = int(preco_original - preco_final)

#imprime o preco final com desconto aplicado
print("o preco final do produto é: r$ {:2f}".format(preço_com_desconto))
