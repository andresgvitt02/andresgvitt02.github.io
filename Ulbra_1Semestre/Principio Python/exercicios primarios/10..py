#Um jardineiro está plantando uma cerca viva que tem 25 metros de comprimento. Se ele precisa
#plantar uma muda a cada 50 centímetros, quantas mudas ele precisará?

#Entrada de dados
comprimento = int(25*100)
distância_mudas = int(50)

#Processamento de dados
quantidade_de_mudas = (comprimento / distância_mudas)

#Sáida de dados
print("A quantidade de mudas que ele precisará é:", round(quantidade_de_mudas, 1), "mudas ")
