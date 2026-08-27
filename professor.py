from pessoa import Pessoa

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
        print(self.nome, " é um professor que está lincenciando no Hangar.")#polimorfismo
        
    def get_siape(self):#Ariely
        return self._siape


    def get_senha(self):#Ariely
        return self._senha