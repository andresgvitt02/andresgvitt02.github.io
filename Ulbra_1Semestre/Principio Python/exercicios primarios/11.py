preco_original = float(input("digite o preco original do produto: "))
valor_desconto = float(input("digite a porcentagem de desconto: "))

#calcula o valor do desconto

#calcula preço final com desconto aplicado
preco_final = preco_original - valor_desconto

#imprime o preco final com desconto aplicado
print("o preco final do produto é: r$ {:2f}".format(preco_final))