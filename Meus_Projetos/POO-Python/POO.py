class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura

    def passar_canal(self, botao):
        if botao == "+":
            print("Aumentar o Canal")
        elif botao == "-":
            print("Diminuir o canal")

controle_remoto = ControleRemoto("preto", "10cm", "2cm", "2cm")

controle_remoto2 = ControleRemoto("azul", "5cm", "3cm", "2cm")


controle_remoto.passar_canal("-")
