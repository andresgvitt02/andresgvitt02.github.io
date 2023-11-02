print("1- VERIFICAR APROVAÇÃO")
print("0- SAIR")

while True:
    codigo = float(input("Digite o código que solicite seu desejo:"))
    if codigo == 1:
            ap1 = float(input("Digite a nota:"))
            ap2 = float(input("Digite a nota:"))
            As = float(input("Digite a nota:"))
            As = (ap1 + ap2 + As)
            taxa_presenca = int(input("Número de faltas do aluno de 1 a 24:"))
            if As >= 6 and taxa_presenca <= 5:
                    print("o aluno está aprovado")
                    continue
            elif As < 6 or taxa_presenca <= 5:
                    print("o aluno deverá fazer a Avaliação Final (AF)")
                    continue
            elif taxa_presenca > 5:
                    print("O aluno está reprovado")
                    continue
    elif codigo == 0:
        continue