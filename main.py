#from datetime
from turma import Turma
from sistema import Sistema
from aluno import Aluno
from professor import Professor


print("Sistema Educacional de Escola de Hangar")#colocar cor

Sistema = Sistema(todas_turmas= [], todos_alunos= [], todos_professores= [])

#Sistema.cadastrar_professor(passar os parametros)



#Fazendo a lógica do fatiamento da turma
#acho melhor fazer no main

#Primeiro fazer a lógica de colocar os alunos na lista

Sistema.todas_turma = []
turma_atual = Turma("Turma 1", "1")
B = 1
#for Aluno in Sistema.todos_alunos:
    #if len(turma_atual.alunos) == 5:
        #Sistema.todas_turma.append(turma_atual)
        #A = len(Sistema.todas_turma) + 1
        #B += 1
        #turma_atual = Turma(f"Turma {A}", B)


    #turma_atual.alunos.append(Aluno)

#if len(turma_atual.alunos) > 0:
    #Sistema.todas_turma.append(turma_atual)