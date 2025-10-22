# gestao_alunos.py

# Estrutura:
# aluno = (nome, id, [notaTPC, notaProj, notaTeste])
# turma = [aluno]

def criar_turma():
    return []

def inserir_aluno(turma):
    print("\n== Inserir aluno ==")
    nome = input("Nome: ")
    id_aluno = input("ID: ")
    notaTPC = float(input("Nota TPC: "))
    notaProj = float(input("Nota Projeto: "))
    notaTeste = float(input("Nota Teste: "))

    aluno = (nome, id_aluno, [notaTPC, notaProj, notaTeste])
    turma.append(aluno)
    print("Aluno inserido com sucesso!")

def listar_turma(turma):
    print("\n== Listar turma ==")
    if len(turma) == 0:
        print("Turma vazia.")
    else:
        print("ID      Nome                 TPC   Proj  Teste  Média")
        print("-----------------------------------------------------")
        i = 0
        while i < len(turma):
            (nome, id_aluno, notas) = turma[i]
            tpc = notas[0]
            proj = notas[1]
            teste = notas[2]
            media = (tpc + proj + teste) / 3
            espacos_nome = " " * (20 - len(nome))
            print(id_aluno, " ", nome, espacos_nome, 
                  str(round(tpc, 1)).ljust(5),
                  str(round(proj, 1)).ljust(5),
                  str(round(teste, 1)).ljust(5),
                  str(round(media, 1)).ljust(5))
            i = i + 1


def consultar_aluno_por_id(turma):
    alvo = input("\nID do aluno a consultar: ")
    i = 0
    while i < len(turma):
        (nome, id_aluno, notas) = turma[i]
        if id_aluno == alvo:
            print("\n== Ficha do aluno ==")
            print("ID:", id_aluno)
            print("Nome:", nome)
            print("TPC:", notas[0])
            print("Projeto:", notas[1])
            print("Teste:", notas[2])
            media = (notas[0] + notas[1] + notas[2]) / 3
            print("Média:", round(media, 2))
            return
        i = i + 1
    print("Aluno não encontrado.")


def guardar_turma_em_ficheiro(turma):
    f = open("algoritmos/ficheiros/atp2024.txt", "w")

    i = 0
    while i < len(turma):
        (nome, id_aluno, notas) = turma[i]
        linha = nome + "::" + id_aluno + "::" + str(notas[0]) + "::" + str(notas[1]) + "::" + str(notas[2]) + "\n"
        f.write(linha)
        i = i + 1

    f.close()
    print("Turma guardada em algoritmos/ficheiros/atp2024.txt")

def carregar_turma_de_ficheiro():
    turma = []
    f = open("algoritmos/ficheiros/atp2024.txt", "r")

    for linha in f:
        linha = linha.strip()       
        campos = linha.split("::")  
        nome = campos[0]
        id_aluno = campos[1]
        tpc = float(campos[2])
        proj = float(campos[3])
        teste = float(campos[4])
        aluno = (nome, id_aluno, [tpc, proj, teste])
        turma.append(aluno)

    f.close()
    print("Turma carregada de algoritmos/ficheiros/atp2024.txt")
    return turma


def menu():
    print("\n===== Gestão de Alunos =====")
    print("1: Criar uma turma")
    print("2: Inserir um aluno na turma")
    print("3: Listar a turma")
    print("4: Consultar um aluno por id")
    print("5: Guardar a turma em ficheiro")
    print("6: Carregar uma turma dum ficheiro")
    print("0: Sair da aplicação")

def main():
    turma = []
    while True:
        menu()
        op = input("Opção: ")
        if op == "1":
            turma = criar_turma()
            print("Turma criada.")
        elif op == "2":
            inserir_aluno(turma)
        elif op == "3":
            listar_turma(turma)
        elif op == "4":
            consultar_aluno_por_id(turma)
        elif op == "5":
            guardar_turma_em_ficheiro(turma)
        elif op == "6":
            turma = carregar_turma_de_ficheiro()
        elif op == "0":
            print("Até já!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
