from turma import Turma
from aluno import Aluno
from professor import Professor


class Sistema():

    def __init__(self): #todas_turmas, todos_alunos, todos_professores
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
            if RA == aluno.RA_aluno:
                aluno.nota = valor #seria boletim.nota = valor?????
                print("O professor deu nota", {valor}, "para o estudate", {aluno.nome}, "de RA", {aluno.RA_aluno}".")#erro aqui

    def ver_alunos(self):
        for aluno in aluno.lista_alunos:
            print("Nome:", aluno.nome, ",", "RA:", aluno.RA_aluno)
            
#def ver_turma(self, codigo): 
     #   for turma in turma.todas_turmas:
      #      if codigo == turma.codigo:
       #         turma.exibir_turma()
        #    else:
         #       print("Turma não encontrada")