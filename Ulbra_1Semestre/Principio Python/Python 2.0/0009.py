#Pedro é um estudante de matemática que está desenvolvendo um programa para calcular o volume
#de uma esfera. Ele sabe que o cálculo pode ser um pouco complicado, mas também é muito
#importante em diversas áreas da matemática e da física. Pedro está animado em desenvolver esse
#programa em Python para ajudar outros estudantes a entenderem melhor a fórmula. Escreva um
#algoritmo que ajude Pedro a calcular o volume de uma esfera.

#Entrada de dados
π = 3.14
raio = float(input("Qual raio da esfera:"))

#Processamento de dados
volume_da_esfera = (4 * π * raio**3)/3

#Sáida de dados
print("O volume da esfera é:", round(volume_da_esfera, 2), "cm³")