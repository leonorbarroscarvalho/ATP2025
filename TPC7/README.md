#1 a)
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]  
ncomuns = []
for elem in lista1:
    if elem not in lista2:
        ncomuns.append(elem)
for elem in lista2:
    if elem not in lista1:
        ncomuns.append(elem)    
print(ncomuns)

#1 b)
texto = """Vivia há já não poucos anos algures num concelho do Ribatejo 
    um pequeno lavrador e negociante de gado chamado Manuel Peres Vigário"""
lista = []
for palavra in texto.split():
    if len(palavra)>3:
        lista.append(palavra)
print(lista)

#1 c)
lista = ['anaconda', 'burro', 'cavalo', 'macaco']
listaRes = [...]
pares = list(enumerate(lista))
print(pares)

#2 a)
def strCount(s, subs):
    count=0
    i=0
    while i<=len(s)-len(subs):
        if s[i:i+len(subs)]==subs:
            count+=1
            i+= len(subs)
        else:
            i+=1
    return count

#2 b)
def produtoM3(lista):
    lista_ordenada=sorted(lista)
    a,b,c=lista_ordenada[:3]
    produto=a*b*c
    return produto
    
#2 c)
def reduxInt(n):
    while n>=10:
        soma=0
        while n>0:
            soma+= n%10
            n//=10
        n=soma
    return n
    
#2 d)
def myIndexOf(s1, s2):
    for i in range (len(s1)- len(s2)+1):
        if s1[i:i+len(s2)]==s2:
            return i
    return -1

#3 a)
def quantosPost(redeSocial):
    return len(redeSocial)

#3 b)
def postsAutor(redeSocial, autor):
    posts=[]
    for post in redeSocial:
        if post['autor']==autor:
            posts.append(post)
    return posts

#3 c)
def autores(redeSocial):
    lista_autores=[]
    for post in redeSocial:
        if post['autor'] not in lista_autores:
            lista_autores.append(post['autor'])
    lista_autores.sort()
    return lista_autores
#3 d)
def insPost(redeSocial, conteudo, autor, dataCriacao, comentarios):
    if len(redeSocial) == 0:
        novo_id = 'p1'
    else:
        ultimos_ids = [int(post['id'][1:]) for post in redeSocial]
        proximo_num = max(ultimos_ids) + 1
        novo_id = f"p{proximo_num}"
    novo_post = {
        'id': novo_id,
        'conteudo': conteudo,
        'autor': autor,
        'dataCriacao': dataCriacao,
        'comentarios': []
    }
    redeSocial.append(novo_post)
    return redeSocial

#3 e)
def remPost(rede, idPost):
    rede = [post for post in rede if post['id'] != idPost]
    return rede

#3 f)
def postsPorAutor(redeSocial):
    distribuicao = {}
    for post in redeSocial:
        autor = post['autor']
        if autor in distribuicao:
            distribuicao[autor] += 1
        else:
            distribuicao[autor] = 1
    return distribuicao

#3 g)
def comentadoPor(redeSocial, autor):
    lista = []
    for post in redeSocial:
        for comentario in post['comentarios']:
            if comentario['autor'] == autor:
                lista.append(post) 
                break
    return lista
