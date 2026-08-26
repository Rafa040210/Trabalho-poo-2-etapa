import datetime
from sistema import Sistema
from pessoa import Pessoa
from boletim import Boletim
from turma import Turma
from aluno import Aluno
from professor import Professor

sistema = Sistema()

print("Bem - Vindo(a) ao Sistema Educacional de Escola de Hangar!")#colocar cor
login = int(input("Faça seu login: \n1)Aluno(a) \n2)Professor(a)")) 
if login == 1:#criando aluno
    quant_aluno = int(input("Informe a quantidade de alunos que você deseja cadastrar:"))
    for i in range(0, quant_aluno):
        nome = input("Informe seu nome:")

        dia = int(input("Informe sua data de nascimento(dd/mm/aaaa):\n-Informe o dia:"))
        mes = int(input("-Informe o mês:"))
        ano = int(input("-Informe o ano:"))
        data_na = datetime.date(ano, mes, dia)

        ra = input("Informe seu RA:")

        senha = input("Crie uma senha:")

        obj_aluno = Aluno(nome, data_na, senha, ra)
        sistema.cadastrar_aluno(obj_aluno)
        sistema.pessoa.append(obj_aluno)
        print("Login feito com sucesso!")#colocar cor

elif login == 2:#criando professor
    quant_prof = int(input("Informe a quantidade de professores que você deseja cadastrar:"))
    for i in range(0, quant_prof):
        nome = input("Informe seu nome:")

        dia = int(input("Informe sua data de nascimento(dd/mm/aaaa):\n-Informe o dia:"))
        mes = int(input("-Informe o mês:"))
        ano = int(input("-Informe o ano:"))
        data_na = datetime.date(ano, mes, dia)

        formacao = input("Informe sua formação:")

        siape = input("Informe seu SIAPE:")

        salario = input("Informe seu salário:")

        senha = input("Crie uma senha:")

        obj_prof = Professor(nome, data_na, formacao, siape, salario, senha)
        sistema.cadastrar_professor(obj_prof)
        sistema.pessoas.append(obj_prof)
        print("Login feito com sucesso!")#colocar cor    

else:
    print("Valor inválido!")

for pessoa in sistema.pessoas:
    pessoa.atuacao()#polimorfismo

#Criando turmas
turma = Turma("Turma 1", "1")
B = 1
for aluno in sistema.todos_alunos:
    if len(turma.lista_alunos) == 5:
        sistema.todas_turma.append(turma)
        A = len(sistema.todas_turma) + 1
        B += 1
        turma = Turma(f"Turma {A}", B)

    turma.alunos.append(Aluno)

if len(turma.lista_alunos) > 0:
    sistema.todas_turma.append(turma)
    turma.exibir_turma()#permite o usuário ver o código da turma para usar depois
    


while True:
    confirmacao = input("Deseja ir para a sua aba do site? (s/n)")
    if confirmacao == "s":
        tipo_usuario = int(input("Você é: \n1)aluno \n2)professor"))

        if tipo_usuario == 1:#para aluno
            print("O que você deseja fazer?")
            opcao_aluno = int(input("Opções para alunos: \n 1)Encontrar a sua turma\n 2)Ver situação do seu boletim"))
        
            if opcao_aluno == 1:

                sistema.buscar_turmas(int(input("Informe cod:")))

            elif opcao_aluno == 2:

                obj_aluno.boletim.ver_situacao()

            else:
                print("Valor inválido!")

        elif tipo_usuario == 2:#para professor
            print("O que você deseja fazer?")
            opcao_prof = int(input("Opções para professores: \n 1)Encontrar a sua turma \n 2)Ver seus dados\n 3)Ver alunos \n4)Dar nota para aluno"))

            if opcao_prof == 1:

                sistema.buscar_turmas(int(input("Informe cod:")))

            elif opcao_prof == 2:

                obj_prof.imprimir_dados()

            elif opcao_prof == 3:

                tipo = int(input("Deseja ver: \n1)todos os alunos da sua turma \n2)todos os alunos da escola"))
                if tipo == 1:

                    turma.ver_alunos()

                elif tipo == 2:

                    sistema.ver_alunos()

                else:
                    print("Valor inválido!")

            elif opcao_prof == 4:

                sistema.dar_nota()

            else:
                print("Valor inválido!")
    else:    
        break