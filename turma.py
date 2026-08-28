
from aluno import Aluno
class Turma():
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.lista_alunos = []
                     

    def exibir_turma(self):
        print("O Nome da sua turma é:", self.nome, ",", " e o código da turma é:", self.codigo)

    def ver_alunos_turma(self, RA):
        for aluno in self.lista_alunos:
            if RA == aluno.RA_aluno:
                print("Nome:", aluno.nome, ",", "RA:", aluno.RA_aluno)
            else:
                break
                