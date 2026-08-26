from aluno import Aluno
from professor import Professor
from turma import Turma


class Sistema():

    def __init__(self):
        self.todas_turmas = []
        self.todos_alunos = []
        self.todos_professores = []

    def cadastrar_aluno(self, aluno):
        self.todos_alunos.append(aluno)

    def cadastrar_professor(self, Professor):
        self.todos_professores.append(Professor)

    def cadastrar_turma(self, Turma):
        self.todas_turmas.append(Turma)

    def buscar_turmas(self, codigo):#método para encontrar uma turma no sistema
        for turma in self.todas_turmas:
            if turma.codigo == codigo:
                return turma.exibir_turma()
            else:
                print("Turma não encontrada!")

    def dar_nota(self, RA, valor):
        for aluno in self.todos_alunos:
            if RA == aluno.get__RA_aluno:
                boletim.notas = valor 
                print("O professor deu nota", {valor}, "para o estudante", {aluno.nome}, "de RA", {aluno.get__RA_aluno},".")
            else:
                print("RA não encontrado")

    def ver_alunos(self):
        for aluno in aluno.todos_alunos: #todos_alunos
            print("Nome:", aluno.nome, ",", "RA:", aluno.get__RA_aluno)
            
