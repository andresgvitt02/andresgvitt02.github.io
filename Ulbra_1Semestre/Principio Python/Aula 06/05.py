#Verificação de número positivo: Escreva um programa que leia um número e verifique se ele
#é positivo ou negativo. Se for positivo, exiba a mensagem "O número é positivo". Caso
#contrário, exiba "O número é negativo".

#Entrada de dados
número = int(input("Digite um número qualquer: "))

#Processamento e sáida de dados
if número < 0:
        print("O número é negativo")
else:
        print("O número é positivo")