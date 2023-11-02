#Crie um algoritmo que receba o nome, sexo, idade e tempo de trabalho (contribuição).
#Com base nos seguintes requisitos para aposentadoria: 
#Mulheres - 30 anos de contribuição e 55 anos de idade
#Homens - 35 anos de contribuição e 60 anos
#Diga se as pessoas consultadas podem ou não requerer a aposentadoria.
#Armazene as informações de quantas pessoas foram consultadas, por exemplo: esta é a consulta número XX.
#Necessário MENU com interface para usuário (no terminal, não é tela gráfica!).


#Entrada de dados
contador = 1
print("Programa para consultar aposentadoria!")

while True:
    print(f"Avaliação número: {contador}")
    print("A escolha se o avaliado é 1-mulher ou 2-homem")
    opcao = int(input("Digite a opção desejada:"))
    contador = contador + 1
    if opcao == 1:
            nome = input("Digite o nome da avaliada:")
            idade = int(input("Digite a idade da avaliada:"))
            tempo = int(input("Digite o tempo de contribuição da avaliada:"))
            if idade >= 55 and tempo >=30:
                print(f"Parabéns {nome} pode solicitar sua aposentadoria")
            else:
                print("O brasil precisa de você ainda!")
    elif opcao == 2:
            nome = input("Digite o nome do avaliado:")
            idade = int(input("Digite a idade da avaliado:"))
            tempo = int(input("Digite o tempo de contribuição da avaliado:"))
            if idade >= 60 and tempo >=35:
                print(f"Parabéns {nome} pode solicitar sua aposentadoria")
            else:
                print("O brasil precisa de você ainda!")
    elif opcao == 3:
        print("|Saindo do programa")
        break
    else:
          print("Digite uma opção válida!")
       





        
    

