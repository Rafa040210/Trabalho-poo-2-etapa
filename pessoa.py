#feito pela Rafa
class Pessoa():
    def __init__(self, nome, data_na):
        self.nome = nome
        self.data_na = data_na

    def exibir_dados(self):
        print("Nome:", self.nome)
        print("Data de nascimento:", self.data_na)

    def atuacao(self):
        print(self.nome, "está na escola Hangar")