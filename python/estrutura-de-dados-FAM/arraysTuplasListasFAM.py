# -*- coding: utf-8 -*-
"""
Integrantes do Grupo:
    RA: 221176 - Camila Pereira de Lira 
    RA: 223993 - Guilherme Viana 
    RA: 198187 - Joao Vitor Sousa
    RA: 226666 - Marcos Dimatheus Andrade Silva 
    RA: 230942 - Pablo de Lima Graça  
    RA: 227100 - Samuel Marcopito    
"""
PRODUTOS = "lista_produtos.txt"
def carregar():
    """
    Retorna uma string dos produtos e seus preços no formato:
        produto1 preco1 produto2 preco2 ... produtoN precoN
    Todas os produtos estão escrito em letras minúsculas.
    O teste do programa será feito com um arquivo com dados
        diferentes
    """
    print("\nCarregando os produtos do arquivo...\n")
    
    # inFile: file
    inFile = open(PRODUTOS, 'r')
    
    # dados: string
    dados = inFile.readline().split(" ")
    
    return dados
aLista = carregar()
def lista_tupla(aLista):
    #range: 0 - início da sequência / len(prod) - lê cada elemento da sequência / 2
- pula de 2 em 2 elementos
    tupla = tuple([(aLista[i], int(aLista[i + 1])) for i in range(0, len(aLista), 
2)])
    return tupla
aTupla = (lista_tupla(aLista))
def get_Produtos(aTupla):
    #maior e menor valor
    maiorValor = max(aTupla, key=lambda e: int(e[1]))
    menorValor = min(aTupla, key=lambda e: int(e[1]))
    #ler quantidade de prod diferentes
    qtd = []
    for produto in aTupla:
        if produto[0] not in qtd:
            qtd.append(produto[0])
    dif = len(qtd)
    return maiorValor, menorValor, dif
maiorValor, menorValor, dif = (get_Produtos(aTupla))
def main():
    menor = print('1. O produto mais Barato:', menorValor)
    maior = print('2. O produto mais caro:', maiorValor)
    qtdDiferente = print('3. Quantidade de Produtos Diferentes:', dif)
    return menor
apresenta = main()
