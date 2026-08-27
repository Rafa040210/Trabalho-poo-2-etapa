
class Boletim():
        def __init__(self, notas):
              self.notas = notas

        def ver_situacao(self):
                if self.notas >= 60 and self.notas <= 100:
                        print("Você está aprovado(a) :) com nota:", self.notas)
                elif self.notas >= 0 and self.notas <= 59:
                        print("Essa nota", self.notas, "não está no paramêtro de aprovação, logo VOCÊ está reprovado.")
                else:
                        print("Essa nota não existe no sistema")