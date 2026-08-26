from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, data_na, senha, RA_aluno, notas=0):
        super().__init__(nome, data_na)

        self.__senha = senha
        self.__RA_aluno = RA_aluno
        self.boletim = Boletim(notas)

    def get__RA_aluno(self):
        return self.__RA_aluno

    def get__senha(self):
        return self.__senha

    def atuacao(self):
        print(self.nome, "é um aluno que está matriculado na escola Hangar.")#polimorfismo