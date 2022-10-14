"""
Integrantes do Grupo:
    RA: 221176 - Camila Pereira de Lira 
    RA: 223993 - Guilherme Viana Araujo 
    RA: 198187 - Joao Vitor Sousa
    RA: 226666 - Marcos Dimatheus Andrade Silva 
    RA: 230942 - Pablo de Lima Graça  
    RA: 227100 - Samuel Marcopito    
"""

#Criar variável com o nome de cada arquivo pra facilitar puxa-las abaixo
musicOne = "ghost.txt"
musicTwo = "29.txt"
musicThree = "scientist.txt"

#Abrir os arquivos como "read"
music_1 = open(musicOne, 'r') 
music_2 = open(musicTwo, 'r')    
music_3 = open(musicThree, 'r')  

#Ler os arquivos
ghost = music_1.readline()
twentyNine = music_2.readline()
scientist = music_3.readline()

#Cria variavel com nome das musicas
ghostJustin = "Ghost - Justin Bieber"
demi29 = "29 - Demi Lovato"
scientistCold = "The Scientist - Coldplay"

def converteTexto(texto):
    #Esta função pega caracteres especiais (pontuacao)
    #novo_texto = com join, copia os caracteres e lower para converter todas as palavras/letras em minúsculo
    #lista = separamos a nova string em elementos de uma lista
    pontuacao = ['.', ',', ':', ';', '!', '?', '"', '(', ')', '-']
    novo_texto = ''.join(c for c in texto if c not in pontuacao).lower()
    lista = novo_texto.split()

    return lista


def palavras(texto):
    #contagem = criamos um dicionário vazio
    #depois faremos a contagem das palavras do texto, assim incluindo no dicionário
    contagem = dict()
    
    for palavra in texto:
        contagem[palavra] = contagem.get(palavra, 0) + 1
        
    return(contagem)

# utiizamos as duas funções acima para cada arquivo
ghost = palavras(converteTexto(ghost))
twentyNine = palavras(converteTexto(twentyNine))
scientist = palavras(converteTexto(scientist))


def maisUtilizadas(texto):
    #frequencias = valores do dicionário
    #maior = pega o maior valor do dicionário pela variável frequencias atribuida acima desta
    
    #cria uma lista vazia para palavras
    #para cada chave no texto, verifica qual chave é maior e adiciona na lista de palavras
    #retorna a palavra mais utilizada
    
    frequencias = texto.values()
    maior = max(frequencias)

    palavras = []
    for chave in texto:
        if texto[chave] == maior:
            palavras.append(chave)

    return (palavras, maior)

print("A palavra mais utilizada em", ghostJustin, "é:", maisUtilizadas(ghost))
print("A palavra mais utilizada em", demi29, "é:", maisUtilizadas(twentyNine))
print("A palavra mais utilizada em", scientistCold, "é:", maisUtilizadas(scientist))

print()
print()
print("1. Verificar qual música/estilo tem mais palavras")
print()
#cria uma lista com todas as musicas
#(maiorMusica) faz a leitura de qual musica possui mais palavras
#(nomeMaiorMusica) apresenta a maior musica
listaMusicas = [ghost, twentyNine, scientist]
maiorMusica = len(max(listaMusicas, key=len))
nomeMaiorMusica = max(listaMusicas, key=len)
print('A maior música possui', maiorMusica, 'palavras.')
print(nomeMaiorMusica)
print()
print()

def palavrasMaisFrequentes(texto, min_vezes):
    '''Parameters
        - Texto: dict = Dicionário com todas as palavras do texto e suas frequências 
        - min_vezes: int = Qual o mínimo de vezes que uma palavra deve aparecer no texto
        Returns
        - Resultado: list
        cada elemento é uma dupla que contém
        - todas as palavras que aparecem no texto um numero mínimo de vezes
        - o numero de vezes que a palavra aparece
        While
        - irá repetir a analise desejada enquanto houverem palavras com o tamanho mínimo no dicionário '''
    resultado = []
    fim = False

    while not fim:
        temp = maisUtilizadas(texto)
        if temp[1] >= min_vezes:
            resultado.append(temp)
            for palavra in temp[0]:
                del(texto[palavra])
        else:
            fim = True

    return resultado


print("As palavras mais frequentes de", ghostJustin, "é:", palavrasMaisFrequentes(ghost, 10))
print("As palavras mais frequentes de", demi29, "é:", palavrasMaisFrequentes(twentyNine, 10))
print("As palavras mais frequentes de", scientistCold, "é:", palavrasMaisFrequentes(scientist, 10))
print()
print()

#v = variavel que define o numero desejado de values do dicionario
v = 1
def palavrasDiferentes(texto):
    '''
    dif = variavel para diferença com valor zerado
    loop = para cada chave no texto(dicionario/musica), se na chave do dicionario o valor dele for 1, ira imprimir
    e assim sucessivamente com dif + 1
    retorna uma string com a variavel dif
    '''
    dif = 0
    
    for key in texto:
        if texto[key] == v:
            dif = dif + 1
    return(str(dif))    



print("2. Verificar qual música/estilo tem mais palavras diferentes")
difGhost = print("Existem", palavrasDiferentes(ghost), "palavras diferentes na música", ghostJustin)
dif29 = print("Existem", palavrasDiferentes(twentyNine), "palavras diferentes na música", demi29)
difScientist = print("Existem", palavrasDiferentes(scientist), "palavras diferentes na música", scientistCold)

diferentes = [palavrasDiferentes(ghost), palavrasDiferentes(twentyNine), palavrasDiferentes(scientist)]
print("Dentre as 3 músicas, a que possui palavras mais diferentes tem", (max(diferentes)), "palavras.")
print()
print()


print("3. Verificar qual música/estilo tem as maiores palavras")
def maiorPalavra(texto):  
    '''
    maiorPalavra = faz a leitura e pega o maior em texto(dicionario)
    retorna a variavel acima
    '''
    maiorPalavra =  max(texto, key=len)
    return maiorPalavra

maiorGhost = print("A maior palavra na música Ghost é:", maiorPalavra(ghost))
maior29 = print("A maior palavra na música 29 é:", maiorPalavra(twentyNine))
maiorScientist = print("A maior palavra na música The Scientist é:", maiorPalavra(scientist))
maior = [maiorPalavra(ghost), maiorPalavra(twentyNine), maiorPalavra(scientist)]
print()
print("Dentre as 3 músicas, a maior palavra entre elas é:", (max(maior, key=len)), "da qual possui", len(max(maior, key=len)), "letras.")

