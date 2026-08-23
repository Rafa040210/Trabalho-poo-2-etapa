from sistema import Sistema

class Turma():
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.lista_alunos = []
        self.lista_professor = []
    
    def ver_turmas(self, todas_turmas):
        print(Sistema.todas_turmas)

    def ver_alunos(self):
        print(self.lista_alunos)

    def ver_professores(self):
        print("Nessa turma os professores que lincenciam são", {self.lista_professor})

    

