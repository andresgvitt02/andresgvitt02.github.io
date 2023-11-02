#Verificação de números pares: Escreva um programa que leia um número inteiro e verifique
#se ele é par ou ímpar. Se for par, exiba a mensagem "O número é par". Caso contrário, exiba
#"O número é ímpar".

#Entrada de dados
número = int(input("Digite um número qualquer: "))

#Processamento e sáida de dados
if número % 2 != 0:
        print("O número é ímpar")
else:
        print("O número é par")