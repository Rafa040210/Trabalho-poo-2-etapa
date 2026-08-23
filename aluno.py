from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, data_na, senha, RA_aluno, nota):
        super().__init__(nome, data_na)

        self.__senha = senha
        self.__RA_aluno = RA_aluno
        self.nota = nota

    def atuacao(self):
        print(self.nome, "está na escola Hangar")