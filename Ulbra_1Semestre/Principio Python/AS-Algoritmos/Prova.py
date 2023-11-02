while True:
    print("1 - Converter Celsius para Fahrenheit")
    print("2 - Converter Celsius para Kelvin")
    print("3 - Converter converter Fahrenheit para Celsius")
    print("4 - Converter converter Fahrenheit para Kelvin")
    print("5 - Converter converter Kelvin para Celsius")
    print("6 - Converter converter Kelvin para Fahrenheit")
    print("7 - para SAIR")


    codigo = float(input("Digite código da conversão que deseja fazer:"))
    temperatura = float(input("Digite a temperatura desejada:"))
    
    #Entrada e processamento de dados
    if codigo == 1:
        temperatura_certa = (temperatura * 9 / 5) + 32
        break
    elif codigo == 2:
        temperatura_certa = (temperatura + 273)
        break
    elif codigo == 3:
        temperatura_certa = (temperatura - 32) * 5 / 9
        break
    elif codigo == 4:
        temperatura_certa = (temperatura + 459.67) * 5 / 9
        break
    elif codigo == 5:
         temperatura_certa = (temperatura - 273.15)
         break
    elif codigo == 6:
        temperatura_certa = (temperatura * 9/5) - 459.67
        break
    elif codigo == 7:
        break

#Saída de dados
print(f"A temperatura que você deseja saber é: {temperatura_certa}")

    


