from pessoa import Pessoa
from aluno import Aluno
from sistema import Sistema
from turma import Turma

class Professor(Pessoa):
    def __init__(self, nome, data_na, formacao, siape, salario, senha):
        super().__init__(nome, data_na)
        self.formacao = formacao
        self.__siape = siape
        self.__senha = senha
        self.salario = salario

    def imprimir_dados(self):
        print(f"O professor {self.nome} possui formação em {self.formacao} cujo o salário é R${self.salario}.")

    def atuacao(self):
        print(self.nome, "está lincenciando no Hangar")#polimorfismo
        
    def get_siape(self):#Ariely
        return self.__siape

        #como q chama em outras classes usa "aluno.get_RA_aluno()"???????

    def get_senha(self):#Ariely
        return self.__senha