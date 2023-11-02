nome = str(input("Insira seu nome:"))
sexo = str(input("Insira seu gênero:"))
if sexo == "feminino":
    idade=int(input("Digite a sua idade:"))
    if idade >= 55:
        tempo_de_contribuição = int(input("digite seu tempo de contribuição:"))
        if tempo_de_contribuição >= 30:
            print("Aprovado")

else:
    idade=int(input("Digite a sua idade:"))
    if idade >= 60:
        tempo_de_contribuição = int(input("digite seu tempo de contribuição:"))
        if tempo_de_contribuição >= 35:
            print("Desaprovado")