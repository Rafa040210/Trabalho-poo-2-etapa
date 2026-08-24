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

    def atuacao(self):
        print(self.nome, "está lincenciando no Hangar")

   