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
newsOne = "globo.txt"
newsTwo = "terra.txt"
newsThree = "uol.txt"

#Abrir os arquivos como "read"
news_1 = open(newsOne, 'r') 
news_2 = open(newsTwo, 'r')    
news_3 = open(newsThree, 'r')  

#Ler os arquivos
globo = news_1.readline()
terra = news_2.readline()
uol = news_3.readline()

def converteTexto(texto):
    #Esta função pega caracteres especiais (pontuacao)
    #novo_texto = com join, copia os caracteres e lower para converter todas as palavras/letras em minúsculo
    #lista = separamos a nova string em elementos de uma lista
    pontuacao = ['.', ',', ':', ';', '!', '?', '"', '(', ')']
    letras = ['de', 'e', 'do', 'a', 'o', 'que', 'em', 'para', 'é', 'no', 'na', 'da', 'das', 'as', 'os', 'não', 'se', 'um', 'uma', 'com', 'dos', 'são', 'eu', 'há', 'mais']
    novo_texto = ''.join(c for c in texto if c not in pontuacao).lower()
    lista = novo_texto.split()
    lista = [palavra for palavra in lista if palavra not in letras]
    return lista


def palavras(texto):
    #contagem = criamos um dicionário vazio
    #depois faremos a contagem das palavras do texto, assim incluindo no dicionário
    contagem = dict()
    
    for palavra in texto:
        contagem[palavra] = contagem.get(palavra, 0) + 1
        
    return(contagem)

def maisUtilizadas(texto):
    #frequencias = valores do dicionário
    #maior = pega o maior valor do dicionário pela variável frequencias atribuida acima desta
    
    #cria uma lista vazia para palavras
    #para cada chave no texto, verifica qual chave é maior e adiciona na lista de palavras
    #retorna a palavra mais utilizada

    maisFrequentes = sorted(texto, key=texto.get, reverse=True)
    return maisFrequentes

# utiizamos as duas primeiras funções acima para cada arquivo
globo = palavras(converteTexto(globo))
terra = palavras(converteTexto(terra))
uol = palavras(converteTexto(uol))

#------QUESTÃO 1----------
#Usaremos o dict para transformar novamente em dicionário
print("1. Quais as 3 palavras mais utilizadas em cada reportagem?")
print()
globoUti =  maisUtilizadas(globo)[:3]
terraUti = maisUtilizadas(terra)[:3]
uolUti = maisUtilizadas(uol)[:3]
print("3 mais utilizadas em Globo: ", globoUti)
print("3 mais utilizadas em Terra: ", terraUti)
print("3 mais utilizadas em Uol: ", uolUti)


#------QUESTÃO 2----------
#Para essa questão, utilizaremos o .set() para conseguirmos comparar as listas:
print()
print("2. Das 10 palavras mais utilizadas em cada reportagem,")
print("Quantas coincidem com as 10 mais utilizadas das outras reportagens?")
print()

contGlobo = maisUtilizadas(globo)[:10]
contTerra = maisUtilizadas(terra)[:10]
contUol = maisUtilizadas(uol)[:10]

print("10 mais utilizadas em Globo: ", contGlobo)
print("10 mais utilizadas em Terra: ", contTerra)
print("10 mais utilizadas em Uol: ", contUol)
print()

#globo e terra
globoSet = set(contGlobo)
globoInter = globoSet.intersection(contTerra)
print("Entre a reportagem da Globo e da Terra existem", len(globoInter), "mais coincidentes e são elas:", globoInter)

#globo e uol
uolInter = globoSet.intersection(contUol)
print("Entre a reportagem da Globo e da Uol existem", len(uolInter), "mais coincidentes e são elas:", uolInter)

#terra e uol
terraSet = set(contTerra)
terraInter = terraSet.intersection(contUol)
print("Entre a reportagem da Terra e da Uol existem", len(terraInter), "mais coincidentes e são elas:", terraInter)


# globoUol = set(contGlobo)&set(contUol)
# terraUol = set(contTerra)&set(contUol)

# print("Entre a reportagem da Globo e da Terra, existem", len(globoTerra), "das palavras mais utilizadas coincidentes entre as duas.")
# print("Entre a reportagem da Globo e da Uol, existem", len(globoUol), "das palavras mais utilizadas coincidentes entre as duas.")
# print("Entre a reportagem da Terra e da Uol, existem", len(terraUol), "das palavras mais utilizadas coincidentes entre as duas.")