from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, data_na, formacao, siape):
        super().__init__(nome, data_na)
        self.formacao = formacao
        self.__siape = siape

    
