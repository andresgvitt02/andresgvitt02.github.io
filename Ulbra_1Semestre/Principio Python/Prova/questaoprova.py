
#Círculo: straight A equals straight pi. straight r squared
#Quadrado:
#A equals L squaredRetângulo:
#A equals b a s e. a l t u r a

while True:
#entrada
    print("Qual forma geométrica você deseja calcular a área?")
    print("Digite: 1-Círculo | 2-Quadrado | 3- Retângulo | 4-Sair")

    opcao = int(input("Digite a opção desejada: "))
    #Círculo
    if opcao == 1:
        pi = 3.14
        raio = int(input("Digite o Raio do círculo: "))
        area = pi * raio ** 2
        print(f"A área do círculo é {area}")
#Quadrado
    elif opcao == 2:
        lado = int(input("Digite o lado do quadrado: "))
        area = lado ** 2
        print(f"A área do quadrado é {area}")
#Retângulo
    elif opcao == 3:
        base = int(input("Digite o base do retângulo: "))
        altura = int(input("Digite a altura do retângulo: "))
        area = base * altura
        print(f"A área do retângulo é {area}")
    else:
        print("Saindo...")
        break
