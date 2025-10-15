def listar(cinema):
    if not cinema:
        print("Não existem filmes em exibição.")
    else:
        i = 0
        while i < len(cinema):
            nlugares, vendidos, filme = cinema[i]
            print(f"{filme}")
            i = i + 1
    return None


def disponivel(cinema, filme, lugar):
    i = 0
    resultado = False
    while i < len(cinema):
        nlugares, vendidos, f = cinema[i]
        if f.lower().strip() == filme.lower().strip():
            if 1 <= lugar <= nlugares and lugar not in vendidos:
                resultado = True
        i = i + 1
    return resultado

def vendebilhete(cinema, filme, lugar):
    novo_cinema = []
    i = 0
    while i < len(cinema):
        nlugares, vendidos, f = cinema[i]
        if f.lower().strip() == filme.lower().strip():
            if 1 <= lugar <= nlugares and (lugar not in vendidos):
                nova_lista = vendidos + [lugar]
                nova_sala = (nlugares, nova_lista, f)
                novo_cinema = novo_cinema + [nova_sala]
            else:
                novo_cinema = novo_cinema + [cinema[i]]
        else:
            novo_cinema = novo_cinema + [cinema[i]]
        i = i + 1
    return novo_cinema

def listardisponibilidades(cinema):
    if not cinema:
        print("Não existem filmes em exibição.")
    else:
        i = 0
        while i < len(cinema):
            nlugares, vendidos, filme = cinema[i]
            livres = nlugares - len(vendidos)
            if livres <= 0:
                print(f"{filme}: não há disponibilidade")
            else:
                print(f"{filme}: {livres} lugares disponíveis")
            i = i + 1



def inserirSala(cinema, sala):
    nlugares_novo, vendidos_novo, filme_novo = sala
    i = 0
    existe = False
    while i < len(cinema):
        nlugares, vendidos, filme = cinema[i]
        if filme == filme_novo:
            existe = True
        i = i + 1
    if not existe:
        cinema = cinema + [sala]
    return cinema


def removerSala(cinema, filme):
    novo = []
    i = 0
    while i < len(cinema):
        nlugares, vendidos, f = cinema[i]
        if f != filme:
            novo = novo + [cinema[i]]
        i = i + 1
    return novo


def totalVendas(cinema):
    i = 0
    total = 0
    while i < len(cinema):
        nlugares, vendidos, filme = cinema[i]
        total = total + len(vendidos)
        i = i + 1
    return total
