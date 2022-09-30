# Jogo da Forca - Hangman
"""
Integrantes do Grupo:
    RA: 221176 - Camila Pereira de Lira 
    RA: 223993 - Guilherme Viana Araujo
    RA: 198187 - Joao Vitor Sousa
    RA: 226666 - Marcos Dimatheus Andrade Silva 
    RA: 230942 - Pablo de Lima Graça  
    RA: 227100 - Samuel Marcopito    
"""
# -----------------------------------
# Código de Apoio
# Você não precisa entender este código auxiliar,
# mas deverá saber como usar as funções
# (lembre-se de ler todas as instruções com atennção)
import random
from string import ascii_lowercase
from unittest import result

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Fim do Código auxiliar
# -----------------------------------
# Carrega a lista de palavras na variável wordlist
# para que possa ser acessado de qualquer lugar do programa

wordlist = loadWords()

def acertouAPalavra(palavraSecreta, palpite):
    '''
    palavraSecreta: string, palavra que o usuário tenta adivinhar
    palpite: list, letras que o usuário usosu até aqui
    returns: boolean, True se todas as letras de palavraSecreta estão em palpite;
      False caso contrário
    '''
    total = len(palavraSecreta)
    x = 0
    for letra in palavraSecreta:
      if letra in palpite:
        x += 1
    return total == x

def getPalavraPalpite(palavraSecreta, palpite):
    '''
    palavraSecreta: string, palavra que o usuário tenta adivinhar
    palpite: list, letras que o usuário usou até aqui
    returns: string, composto por letras e sublinhados que representam 
quais letras em (palavraSecreta foram adivinhadas até agora..
    '''
    letras = ''
    for palavra in palavraSecreta:
      if palavra in palpite:
        letras += palavra
      else:
        letras += '_ '
    return letras

def getLetrasDisponiveis(palpite):
    '''
    palpite: lista, quais letras foram usadas até agora
    retorna: string, composta de letras que representam as letras que 
       ainda não foram usadas no palpite.
    '''
    import string
    resultado = ''
    for letra in string.ascii_lowercase:
      if letra not in palpite:
        resultado += letra
    return resultado

def enforca(tentativas):
    '''
    conforme as tentativas forem diminuindo o desenho 
    vai se formando, até enforcar quando não restar mais
    tentativas.
    '''
    if tentativas == 8:
        print()
        print("|----- ")
        print("|    | ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("|      ")
        print()
        
    elif tentativas == 7:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|      ")
        print("|      ")
        print("|      ")
        print()
        
    elif tentativas == 6:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|    | ")
        print("|      ")
        print("|      ")
        print()
        
    elif tentativas == 5:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /| ")
        print("|      ")
        print("|      ")
        print()

    elif tentativas == 4:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\ ")
        print("|      ")
        print("|      ")
        print()
              
    elif tentativas == 3:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\ ")
        print("|    | ")
        print("|   /  ")
        print()

    elif tentativas == 2:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\ ")
        print("|    | ")
        print("|   / \ ")
        print()
              
    elif tentativas == 1:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   --- ")
        print("|   /|\ ")
        print("|    | ")
        print("|   / \ ")
        print()    

def hangman(palavraSecreta):
    '''
     palavraSecreta: string, a palavra secreta a adivinhar.
     Inicia um jogo interativo de forca.
     * No início do jogo, informe ao usuário quantas
       letras que a palavraSecreta contém.
     * Peça ao usuário para fornecer um palpite (ou seja, letra) por rodada.
     * O usuário deve receber feedback imediatamente após cada palpite
       sobre se o palpite dele aparece na palavra do computador.
     * Após cada rodada, você também deve exibir para o usuário o
       palavra adivinhada até agora, bem como letras que o
       usuário ainda não adivinhou.
     Siga as outras limitações detalhadas na redação do problema.
    '''

    print('Bem vindo ao Jogo da Forca!')
    print('A palavra possui', len(palavraSecreta), 'letras.')
    print(' ')

    palpite = []
    faltantes = [] 
    tentativas = 8

    while tentativas > 0:
        print(' ')
        print("Você ainda tem", tentativas, "tentativas.")
        print("Letras disponíveis:", getLetrasDisponiveis(palpite + faltantes))
        adivinha = str(input("Digite uma letra: ")).lower()
        
        if adivinha in palavraSecreta and adivinha not in palpite:
            palpite += adivinha
            if acertouAPalavra(palavraSecreta, palpite) == True:
                print("Você acertou! A palavra é: ", getPalavraPalpite(palavraSecreta, palpite))
                print('')
                print("Parabéns!")
                break
                
            print("Boa tentativa!", getPalavraPalpite(palavraSecreta, palpite))
            print('')
            
        elif adivinha not in palavraSecreta:
            if adivinha in faltantes:
                print("Você já adivinhou essa letra, tente outra.")
                print(f'{getPalavraPalpite(palavraSecreta, palpite)}')
                print('')
            else:
                faltantes += adivinha
                print ("Incorreto, essa letra não existe na palavra.")
                print('')
                enforca(tentativas)
                print(f'{getPalavraPalpite(palavraSecreta, palpite)}')
                tentativas -= 1
        else:
            print("Você já adivinhou essa letra, tente outra: ", getPalavraPalpite(palavraSecreta, palpite))
            print('')
    
    if tentativas <= 0:
        print("Infelizmente você perdeu, a palavra era:", palavraSecreta,".")
    
# Ao concluir a função hangan, remova as duas linhas de comentário abaixo
# e execute este arquivo para testar! (dica: você pode escolher sua própria
# palavra secreta enquanto estiver testando)
palavraSecreta = chooseWord(wordlist).lower()
hangman( palavraSecreta )