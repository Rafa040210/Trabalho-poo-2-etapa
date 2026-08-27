from pessoa import Pessoa
from boletim import Boletim

class Aluno(Pessoa):
    def __init__(self, nome, data_na, senha, RA_aluno, notas=0):
        super().__init__(nome, data_na)

        self._senha = senha
        self._RA_aluno = RA_aluno
        self.boletim = Boletim(notas)

    def get_RA_aluno(self):
        return self._RA_aluno

    def get_senha(self):
        return self._senha

    def atuacao(self):
        print(self.nome, "é um aluno que está matriculado na escola Hangar.")#polimorfismo