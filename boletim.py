from aluno import Aluno 
class Boletim:
        def __init__(self, notas):
              self.nota = nota

        def ver_situacao(self):
                if self.nota >= 60 and self.nota <= 100:
                        print("Você está aprovado(a) :) com nota:", self.nota)
                elif self.nota >= 0 and self.nota <= 59:
                        print("Essa nota", self.nota, "não está no paramêtro de aprovação, logo VOCÊ está reprovado.")
                else:
                        print("Essa nota não existe no sistema")