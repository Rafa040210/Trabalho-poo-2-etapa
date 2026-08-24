from pessoa import Pessoa
from aluno import Aluno
from sistema import Sistema
from turma import Turma

class Professor(Pessoa):
    def __init__(self, nome, data_na, formacao, siape, salario, senha):
        super().__init__(nome, data_na)
        self._formacao = formacao
        self.__siape = siape
        self.__senha = senha
        self.salario = salario

    super().exibir_dados()

    def atuacao(self):
        print(self.nome, "está lincenciando no Hangar")

    def dar_nota(self, RA_aluno, valor):
        Aluno.nota = valor
        print("O professor deu nota", {valor}, "para o estudate", {Aluno.nome}, "de RA", {Aluno.RA_aluno})

    def ver_turma(self, Aluno): 
        if not Aluno.lista_alunos:
            print("aluno não se encontra nessa turma")
        for Aluno in Aluno.lista_alunos:
            print("Nome:", Aluno.nome, ",", "RA:", Aluno.RA_aluno)