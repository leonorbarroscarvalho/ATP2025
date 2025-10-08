import random 
lista=[]
continuar=True

while continuar:
    print("--- MENU ---")
    print("(1) Criar Lista Aleatória")
    print("(2) Ler Lista do Utilizador")
    print("(3) Soma")
    print("(4) Média")
    print("(5) Maior")
    print("(6) Menor")
    print("(7) Ordene por ordem crescente")
    print("(8) Ordene por ordem decrescente")
    print("(9) Procurar um elemento")
    print("(0) Sair")

    função = int(input("Introduza o número da função que quer executar:"))

    if função==0:
        print("Aplicação fechada")
        continuar=False

    elif função==1:
        n= int(input("Quantos elementos pretende gerar?"))
        i=0
        while i<n:
            lista.append(random.randint(0,100))
            i=i+1
        print(lista)

    elif função==2:
        lista.clear()   # limpa a lista anterior antes de ler nova
        numeros = input("Introduza números separados por espaço: ").split()
        for n in numeros:
            lista.append(int(n))
        print(lista)

    elif função==3:
        res=0
        for n in lista:
            res= res+n
        print(res)

    elif função==4:
        res=0
        for n in lista:
            res= res+n
        print(res/len(lista))

    elif função==5:
        res=lista[0]
        for n in lista[1:]:
            if n>res:
                res=n
        print(res)

    elif função==6:
        res=lista[0]
        for n in lista[1:]:
            if n<res:
                res=n
        print(res)

    elif função==7:
        res=[]
        for n in lista:
            lista.sort()
        print(lista)

    elif função==8:
        res=[]
        for n in lista:
            lista.reverse()
        print(lista)

    elif função==9:
        num= int(input("Tntroduza o elemento da lista que quer procurar: "))
        i=0
        p=-1
        for n in lista:
            if n==num and p==-1:
                pos=i
            i=i+1
        print(p)



