#Um ônibus saiu de uma cidade a 300km de distância e foi até outra cidade a uma velocidade média de
#60km/h. Quanto tempo ele levou para chegar ao destino?

#Entrada de dados
distancia_entre_as_cidades = int(input("distancia km:"))
velocidade_media = int(input("velocidade media km/h: "))

#Processamento de dados
tempo_de_viagem = (distancia_entre_as_cidades / velocidade_media)

#Sáida de dados
print("o tempo de viagem é: ", round(tempo_de_viagem, 1), "horas ")

