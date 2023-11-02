#Uma pessoa pesa 65kg e mede 1,70m. Qual é o seu índice de massa corporal (IMC)? Considere a
#fórmula IMC = peso / altura².

#Entrada de dados
peso = float(input("quantos quilos você tem? "))
altura = float(input("qual a sua altura? "))

#Processamento de dados
IMC = (peso / (altura*altura))

#Sáida de dados
print("o IMC da pessoa é:", IMC)

