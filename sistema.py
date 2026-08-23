from turma import Turma
from aluno import Aluno
from professor import Professor


class Sistema():

    def __init__(self, todas_turmas, todos_alunos, todos_professores):
        self.todas_turmas = []
        self.todos_alunos = []
        self.todos_professores = []

    def cadastrar_aluno(self, Aluno):
        self.todos_alunos.append(Aluno)

    def cadastrar_professor(self, Professor):
        self.todos_professores.append(Professor)

    def cadastrar_turma(self, Turma):
        self.todas_turmas.append(Turma)

    #método para encontrar uma turma no sistema

    def buscar_turmas(self, codigo):
        for Turma in self.todas_turmas:
            if Turma.codigo == codigo:
                return Turma
            else:
                print("Turma não encontrada!")