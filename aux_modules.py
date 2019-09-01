def condicao_vitoria(tabuleiro):
    '''
    Esta função recebe uma lista que representa um tabuleiro, com tamanho 8, e retorna o valor do vencedor. Caso não haja vencedor, esta retorna "false". 
    '''
    if (tabuleiro[0] == tabuleiro[1] and tabuleiro[1] == tabuleiro[2]) and tabuleiro[0]!= -1:
        return tabuleiro[0]
    elif (tabuleiro[3] == tabuleiro[4] and tabuleiro[4] == tabuleiro[5]) and tabuleiro[3]!= -1:
        return tabuleiro[3]
    elif (tabuleiro[6] == tabuleiro[7] and tabuleiro[7]==tabuleiro[8]) and tabuleiro[6]!=-1:
        return tabuleiro[6]
    elif (tabuleiro[0]==tabuleiro[3] and tabuleiro[3]==tabuleiro[6]) and tabuleiro[0]!=-1:
        return tabuleiro[0]
    elif (tabuleiro[1]==tabuleiro[4] and tabuleiro[4]==tabuleiro[7]) and tabuleiro[1]!=-1:
        return tabuleiro[1]
    elif (tabuleiro[2]==tabuleiro[5] and tabuleiro[5]==tabuleiro[8]) and tabuleiro[2]!=-1:
        return tabuleiro[2]
    elif (tabuleiro[0]==tabuleiro[4] and tabuleiro[4]==tabuleiro[8]) and tabuleiro[0]!=-1:
        return tabuleiro[0]
    elif (tabuleiro[2]==tabuleiro[4] and tabuleiro[4]==tabuleiro[6]) and tabuleiro[2]!=-1:
        return tabuleiro[2]
    else:
        if (-1 in tabuleiro) == False:
            return "EMPATE"
        else:
            return "CONTINUAR"

def printarTabuleiro(tabuleiro):
    lista = []
    for casa in tabuleiro:
        if casa==-1:
            lista.append(" ")
        elif casa==0:
            lista.append("O")
        elif casa==1:
            lista.append("X")
    print(lista[0]+"|"+lista[1]+"|"+lista[2])
    print("------")
    print(lista[3]+"|"+lista[4]+"|"+lista[5])
    print("------")
    print(lista[6]+"|"+lista[7]+"|"+lista[8])
