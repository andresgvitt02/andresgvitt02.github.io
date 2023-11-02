#Uma pessoa tem R$ 500 em sua conta corrente e precisa pagar uma conta de R$ 150 e
#outra de R$ 300. Qual é o saldo final da conta corrente?

#Entrada de dados
saldo_conta = 500
conta1 = 150
conta2 = 300

#Processamento
Saldo_final = (saldo_conta - conta1 - conta2)

#Saída de dados
print("O saldo final da conta é:", round(Saldo_final, 1), "$")