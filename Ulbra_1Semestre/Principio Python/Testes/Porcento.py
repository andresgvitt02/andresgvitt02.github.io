preco_original = float(input('Valor inicial: '))
desconto_10 = float(preco_original * 0.9)
desconto_20 = float(preco_original * 0.8)
desconto_30 = float(preco_original * 0.7)

desconto = input('Qual o percentual de desconto? ')
if desconto == 10:
    print(f'Você ganhou 10% de desconto (R$ {preco_original * 0.1}) e pagará apenas {desconto_10}')
elif desconto == 20:
    print(f'Você ganhou 20% de desconto (R$ {preco_original * 0.2}) e pagará apenas {desconto_20}')
elif desconto == 30:
    print(f'Você ganhou 30% de desconto (R$ {preco_original * 0.3}) e pagará apenas {desconto_30}')
else:
    print('Desconto não permitido, apenas 10, 20 ou 30% de desconto')