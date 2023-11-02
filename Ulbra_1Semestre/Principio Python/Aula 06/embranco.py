import random 
numero_correto = random.randint(1,100)
tentativas_restantes = 10
print("Tente adivinhar o número escolhido pelo programa: entra 1 e 100")

while tentativas_restantes > 0:
    try:
        palpite = int(input("Digite seu palpite:"))
    except ValueError:
        print("Digite apenas números")
    if palpite == numero_correto:
        print("Parabéns, você acertou!")
        break 
    elif palpite < numero_correto:
        print("Seu palpite é menor que o número correto")
    else:
        print("Seu palpite é maior que o número correto")
    tentativas_restantes -= 1
if tentativas_restantes == 0:
    print(f"Suas tentativas acabaram. O número correto era {numero_correto}.")



        

