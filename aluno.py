from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, data_na, senha, RA_aluno, notas):
        super().__init__(nome, data_na)

        self.__senha = senha
        self.__RA_aluno = RA_aluno
        self.boletim = Boletim(notas)

    def get_RA_aluno(self):#ariely
        return self.__RA_aluno

    def get_senha(self):#ariely
        return self.__senha

    def atuacao(self):
        print(self.nome, "está matriculado na escola Hangar")#polimorfismo