from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, data_na, senha, RA_aluno, nota):
        super().__init__(nome, data_na)

        self.__senha = senha
        self.__RA_aluno = RA_aluno
        self.nota = nota#boletim

    def get_RA_aluno(self):#ariely
        return self.__RA_aluno

    def get_senha(self):#ariely
        return self.__senha

    def atuacao(self):
        print(self.nome, "está matriculado na escola Hangar")#polimorfismo

    def ver_situacao(self):
        if self.nota >= 60 and self.nota <= 100:
            print(self.nome, "aprovado(a) :) com nota:", self.nota)
        elif self.nota >= 0 and self.nota <= 59:
             print("Essa nota", self.nota, "não está no paramêtro de aprovação, logo o aluno", self.nome, "está  reprovado.")
        else:
            print("Essa nota não existe no sistema")