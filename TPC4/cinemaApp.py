from cinema import *

def menu(cinema):
    ativo = True
    while ativo:
        print("\n=== Gestão de Cinema ===")
        print("1. Listar filmes")
        print("2. Verificar disponibilidade")
        print("3. Vender bilhete")
        print("4. Listar disponibilidades")
        print("5. Inserir sala")
        print("6. Remover sala")
        print("7. Total de vendas")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar(cinema)

        elif opcao == "2":
            filme = input("Filme: ")
            lugar = int(input("Lugar: "))
            if disponivel(cinema, filme, lugar):
                print("Lugar disponível")
            else:
                print("Lugar ocupado ou inválido")

        elif opcao == "3":
            filme = input("Filme: ")
            lugar = int(input("Lugar: "))
            if disponivel(cinema, filme, lugar):
                cinema = vendebilhete(cinema, filme, lugar)   
                print("Bilhete vendido com sucesso")
            else:
                print("Não foi possível vender. Lugar indisponível")

        elif opcao == "4":
            listardisponibilidades(cinema)

        elif opcao == "5":
            filme = input("Filme: ")
            nlugares = int(input("Número de lugares: "))
            nova_sala = (nlugares, [], filme)
            cinema = inserirSala(cinema, nova_sala)
            print("Sala inserida")

        elif opcao == "6":
            filme = input("Filme a remover: ")
            cinema = removerSala(cinema, filme)
            print("Sala removida")

        elif opcao == "7":
            print(f"Total de bilhetes vendidos: {totalVendas(cinema)}")

        elif opcao == "0":
            print("A sair...")
            ativo = False

        else:
            print("Opção inválida. Tente novamente.")


def main():
    sala1 = (150, [], "Twilight")
    sala2 = (200, [], "Hannibal")
    cinema = []
    cinema = inserirSala(cinema, sala1)
    cinema = inserirSala(cinema, sala2)
    menu(cinema)


if __name__ == "__main__":
    main()
