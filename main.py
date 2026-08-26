from datetime
from turma import Turma
from sistema import Sistema
from aluno import Aluno
from professor import Professor


print("Bem - Vindo(a) ao Sistema Educacional de Escola de Hangar!")#colocar cor

sistema = Sistema()

while True:
    print("O que você deseja fazer?")
    opcao_aluno = ("Opções para alunos: \n 1)Encontrar a sua turma \n 2)Ver seus professores\n 3)Ver situação do seu boletim")#1
    opcao_prof = ("Opções para professores: \n 1)Encontrar a sua turma \n 2)Ver seus professores\n 3)Ver situação do seu boletim")





































Sistema.todas_turma = []
turma_atual = Turma("Turma 1", "1")
B = 1
for aluno in Sistema.todos_alunos:
    if len(turma_atual.alunos) == 5:
        Sistema.todas_turma.append(turma_atual)
        A = len(Sistema.todas_turma) + 1
        B += 1
        turma_atual = Turma(f"Turma {A}", B)


    turma_atual.alunos.append(Aluno)

if len(turma_atual.alunos) > 0:
    Sistema.todas_turma.append(turma_atual)
    #profesor = Professor(...)
#p.ex
#Sistema.cadastrar_professor(professor)