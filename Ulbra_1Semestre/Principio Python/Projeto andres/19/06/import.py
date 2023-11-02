import datetime

def calcula_imc(peso, altura):
    imc = peso / altura

nome = input("Digite seu nome:")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite a sua altura: "))

data_atual = datetime.datetime.now()

imc = peso / pow(altura,2)

if imc < 18.5:
    
    










print(f"Olá {nome}!")
print(f"Seu IMC é : {imc}")
print(classificacao)
