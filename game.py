import random
import aux_modules

def pvp():
    tabuleiro = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
    vez = random.randint(0,1)

    while True:
        resultado = aux_modules.condicao_vitoria(tabuleiro)
        if resultado == 0:
            print("BOLA VENCE A PARTIDA. ESTÁ IMPLACÁVEL!")
            break
        elif resultado ==1:
            print("XIS VENCE A PARTIDA. ESTÁ LENDÁRIO!!")
            break
        elif resultado == "EMPATE":
            print("EMPATOOOOOU!!! DOIS NOOBS JOGANDO! LIXOS!")
            break
        else:
            print("VEZ DE %i"%(vez))
            posicao = int(input(">>> "))
            if posicao>=0 and posicao <=8 and tabuleiro[posicao]==-1:
                tabuleiro[posicao] = vez
            else:
                print("Jogada incorreta. Perdeu, pai")
            aux_modules.printarTabuleiro(tabuleiro)
            if vez == 0:
                vez = 1
            else:
                vez = 0
        
        
        
        
                      
        
