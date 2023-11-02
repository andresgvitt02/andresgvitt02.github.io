#Cálculo de média: Escreva um programa que leia três notas e calcule a média do aluno. Se a
#média for maior ou igual a 7, exiba a mensagem "Aprovado". Caso contrário, exiba
#"Reprovado".

#Entrada de dados
nota1 = float(input("digite a nota 1:"))
nota2 = float(input("digite a nota 2:"))
nota3 = float(input("digite a nota 3:"))

#Processamento
media = (nota1 + nota2 + nota3)/3

#Saída
print("A média do aluno é:", round(media, 1), "") 

if media >= 7.0:
    print("Aprovado")

else:
    print("Reprovado")