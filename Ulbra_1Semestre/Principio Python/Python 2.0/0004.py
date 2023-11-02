#Você está desenvolvendo um programa para calcular a altura máxima e o tempo de queda de um
#objeto em um lançamento vertical. O usuário deve informar a altura inicial do objeto. Assuma que a
#aceleração da gravidade é igual a 9,81 m/s². Escreva um algoritmo que calcule e imprima a altura
#máxima e o tempo de queda do objeto.

#Entrada de dados
altura_inicial = int(input("Digite a altura inicial do objeto: "))
aceleração_da_gravidade = int(input("Digite a aceleração da gravidade: "))

tempo_de_subida = altura_inicial / aceleração_da_gravidade
