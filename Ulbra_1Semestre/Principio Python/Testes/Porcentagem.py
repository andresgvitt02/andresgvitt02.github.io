# Vamos pedir o valor original do produto
valor_original = float( input("Valor original: R$ ") )

# Desconto que será concedido
desconto = float( input("Desconto (em %) para esse produto: ") )

# Transformando a porcentagem em número decimal
desconto = desconto / 100

# Exibindo tudo
print('Valor original:     R$', valor_original)
print('Desconto ganho:     R$', valor_original * desconto)
print('Valor com desconto: R$', valor_original * (1-desconto) )
