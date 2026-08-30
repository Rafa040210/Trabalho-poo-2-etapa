from aluno import Aluno
from professor import Professor
from turma import Turma
from pessoa import Pessoa
from boletim import Boletim


class Sistema():
    def __init__(self):
        self.pessoas = []
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
                turma.exibir_turma()
            else:
                print("Turma não encontrada!")

    def dar_nota(self, ra, valor):
        for aluno in self.todos_alunos:
            if ra == aluno.RA_aluno:
                aluno.notas = valor 
                print("O professor deu nota", valor, "para o estudante", aluno.nome, "de RA", aluno.RA_aluno,".")
            else:
                print("RA não encontrado")

    def ver_alunos(self):
        for aluno in self.todos_alunos: #todos_alunos
            print("Nome:", aluno.nome, ",", "RA:", aluno.RA_aluno)

    def ver_situacao(self, ra):
        for aluno in self.todos_alunos:
            if ra == aluno.RA_aluno:
                if aluno.notas >= 60 and aluno.notas <= 100:
                    print("Você está aprovado(a) :) com nota:", aluno.notas)
                elif aluno.notas >= 0 and aluno.notas <= 59:
                        print("Essa nota", aluno.notas, "não está no paramêtro de aprovação, logo VOCÊ está reprovado.")
                else:
                    print("\033[31mEssa nota não existe no sistema\033[m")