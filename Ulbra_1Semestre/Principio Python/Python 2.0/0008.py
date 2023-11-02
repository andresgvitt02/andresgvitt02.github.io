#Maria é uma estudante de física que está desenvolvendo um programa para converter uma
#temperatura de Celsius para Fahrenheit. Ela sabe que muitas vezes precisa realizar essa conversão
#em seus estudos, mas a fórmula matemática pode ser confusa. Por isso, ela está desenvolvendo um
#programa em Python que simplifica esse processo. Escreva um algoritmo que ajude Maria a
#converter uma temperatura de Celsius para Fahrenheit.

#Entrada de dados
graus_celsius = float(input("Quantos graus celsius:"))

#Processamento de dados
fahrenheit = (graus_celsius * (9 / 5))+32

#Sáida de dados
print("temperatura em fahrenheit:", round(fahrenheit, 2), "") 