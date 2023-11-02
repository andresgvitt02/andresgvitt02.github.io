#Cálculo de imposto: Escreva um programa que leia o salário de um funcionário e calcule o
#valor do imposto a ser pago, considerando as seguintes faixas salariais: até R$ 1.000,00,
#isento de imposto; de R$ 1.000,00 a R$ 2.000,00, 10% de imposto; acima de R$ 2.000,00,
#20% de imposto.

#Entrada de dados
Salário_do_funcionário = float(input("digite o salário do funcionário:"))

if Salário_do_funcionário > 1.000 < 2.000:
    desconto = ((Salário_do_funcionário * 10))/100
    salario_final = (Salário_do_funcionário - desconto)

elif Salário_do_funcionário > 2.000:
    
#Sáida de dados
print()