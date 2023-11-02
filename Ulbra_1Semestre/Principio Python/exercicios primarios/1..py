# Uma pessoa foi a um restaurante que está com um prato do dia que custa R$ 35, mas no horário do
#almoço ele é vendido por R$ 25. Quantos reais uma pessoa economizaria pedindo o prato do dia no horário
#do almoço?


#Entrada de dados
Preço_prato_do_dia = int(input("digite o preco prato do dia: "))
Preço_meio_dia = int(input("digite o preço prato meio dia: "))

#Processamento de dados
desconto = (Preço_prato_do_dia -Preço_meio_dia)

#Sáida de dados
print("o desconto é:" ,desconto)

