#João é um médico que trabalha em uma clínica especializada em saúde preventiva. Ele está
#desenvolvendo um programa para calcular o IMC (Índice de Massa Corporal) de seus pacientes. O
#IMC é uma medida que relaciona o peso e a altura de uma pessoa e é utilizada para verificar se ela
#está com o peso ideal. João sabe que, para calcular o IMC, ele precisa da altura e do peso do
#paciente. Escreva um algoritmo em Python que ajude João a calcular o IMC de seus pacientes.

#Entrada de dados
peso = float(input("quantos quilos você tem? "))
altura = float(input("qual a sua altura? "))

#Processamento de dados
IMC = (peso / (altura*altura))

#Sáida de dados
print("o IMC da pessoa é:", round(IMC, 3), "") 

