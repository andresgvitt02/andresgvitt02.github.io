#Ana é uma professora de matemática que está desenvolvendo um programa para calcular a média
#aritmética de uma lista de números. Ela sabe que, para calcular a média, é necessário somar todos
#os números da lista e dividir pelo total de números. Ana quer desenvolver um programa em Python
#que possa ser utilizado por seus alunos para facilitar esse processo. Escreva um algoritmo que ajude
#Ana a calcular a média aritmética de uma lista de números.

#Entrada de dados
nota1 = float(input("digite a nota 1:"))
nota2 = float(input("digite a nota 2:"))
nota3 = float(input("digite a nota 3:"))

#Processamento
media = (nota1 + nota2 + nota3)/3

#Saída
print(f"A media das três notas é {media}")
