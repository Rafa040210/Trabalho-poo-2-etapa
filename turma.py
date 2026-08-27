
from aluno import Aluno
class Turma():
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.lista_alunos = []
                     

    def exibir_turma(self):
        print("Nome turma:", self.nome, ",", "código turma:", self.codigo)