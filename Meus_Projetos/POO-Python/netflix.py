class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ["basic", "premium"]
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception("Plano inválido")
        
    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            ("Plano inválido")

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print("Ver filme{filme}")
        elif self.plano == "premium":
            print("Ver filme{filme}")
        elif self.plano == "basic" and plano_filme == "premium":
            print("Faça upgrade para premium para assistir esse filme")
        else:
            print("Plano inválido")

Cliente = Cliente("Andres G. Vitt", "Andres@", "basic")
print(Cliente.plano)
Cliente.ver_filme("Harry potter", "premium")

# botão upgrade
Cliente.mudar_plano("basic")
print(Cliente.plano)

