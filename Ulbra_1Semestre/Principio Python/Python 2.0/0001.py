#Você está desenvolvendo um programa para calcular a corrente elétrica em um circuito elétrico. O
#usuário deve informar a resistência elétrica e a tensão elétrica do circuito. Escreva um algoritmo que
#calcule e imprima a corrente elétrica do circuito, de acordo com a lei de Ohm.

#Entrada de dados
Resistência_elétrica = float(input("Qual resistência elétrica:"))
Tensão_elétrica = float(input("Tensão elétrica do circuito: "))

#Processamento de dados
Corrente_elétrica = (Tensão_elétrica / Resistência_elétrica)

#Sáida de dados
print("Sua corrente elétrica é: ", round(Corrente_elétrica, 2), "Volts")