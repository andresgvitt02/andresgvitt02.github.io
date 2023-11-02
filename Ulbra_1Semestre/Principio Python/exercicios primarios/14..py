#Um carro faz 12km por litro de gasolina. Se ele percorrer uma distância de 360km, quantos litros de
#gasolina ele gastará?

#Entrada de dados
km_por_litro = 12
distância_percorrida = 360 

#Processamento
litros_gastos_na_viagem = (distância_percorrida / km_por_litro)

#Saída de dados
print("Quantidade gasta de litros na viagem foi de:", round(litros_gastos_na_viagem, 1), "L") 