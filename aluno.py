from pessoa import Pessoa
from boletim import Boletim

class Aluno(Pessoa):
    def __init__(self, nome, data_na, senha, RA_aluno, notas):
        super().__init__(nome, data_na)

        self._senha = senha
        self.RA_aluno = RA_aluno
        self.boletim = Boletim(notas)

    def get_senha(self):
        return self._senha

    def atuacao(self):
        print(self.nome, "é um aluno que está matriculado na escola Hangar.")#polimorfismo