# Solicita ao usuário a temperatura e as escalas de entrada e saída
temperatura = float(input("Digite a temperatura: "))
escala_entrada = input("Digite a escala de temperatura de entrada (C, F ou K): ").upper()
escala_saida = input("Digite a escala de temperatura de saída (C, F ou K): ").upper()

# Converte a temperatura para Celsius 
if escala_entrada == 'F':
    temperatura = (temperatura - 32) * 5 / 9
elif escala_entrada == 'K':
    temperatura = temperatura - 273.15

# Converte a temperatura de Celsius para a escala de saída
if escala_saida == 'F':
    temperatura = temperatura * 9 / 5 + 32
elif escala_saida == 'K':
    temperatura = temperatura + 273.15

# Exibe o resultado
print("A temperatura convertida é:", temperatura, escala_saida)
