import random
import aux_modules
from socket import *
def pvp_local():
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
        
def pvp_online():
    escolha = "0"
    while escolha not in ["1","2"]:
        print("Tu és cliente ou servidor?\n1.Cliente\n2.Servidor")
        escolha = input(">>> ")
     
    skt = socket(AF_INET,SOCK_DGRAM)    
    if escolha == "1":
        servidorIP = input("Digite o IP do servidor: ")
        pvp_online_cliente(skt,servidorIP)
    elif escolha == "2":
        skt.bind(("",5001))
        pvp_online_servidor(skt)
    else:
        print("Ocorreu um erro inesperado. Corrige aí, boy.")

        
def pvp_online_servidor(skt):
    print("Esperando conexão do cliente...")
    msg,adr = skt.recvfrom(1024)
    tabuleiro = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
    vez = random.randint(0,1)
    #0 = Vez do servidor;
    #1 = Vez do cliente.
    while True:
        resultado = aux_modules.condicao_vitoria(tabuleiro)
        if resultado == 0:
            print("BOLA VENCE A PARTIDA. ESTÁ IMPLACÁVEL!")
            skt.sendto("LOSER".encode(),adr)
            break
        elif resultado ==1:
            print("XIS VENCE A PARTIDA. ESTÁ LENDÁRIO!!")
            skt.sendto("WINNER".encode(),adr)
            break
        elif resultado == "EMPATE":
            print("EMPATOOOOOU!!! DOIS NOOBS JOGANDO! LIXOS!")
            skt.sendto("DRAW".encode(),adr)
            break
        else:
            # Declara variável de posição da jogada
            posicao = -1

            # Envia o tabuleiro
            skt.sendto(str(tabuleiro).encode(),adr)

            # Caso seja o servidor que vai jogar, posição é definido por input
            if vez == 0:                
                print("SUA VEZ")
                posicao = int(input(">>> "))
            # Caso seja a vez do cliente, posição é definido por recvfrom
            else:
                print("Aguardando jogada do adversário...")
                skt.sendto("YOUR_TURN".encode(),adr)
                msg,adr = skt.recvfrom(1024)
                posicao = int(msg.decode())

            # Verificar se a jogada é válida
            if posicao>=0 and posicao <=8 and tabuleiro[posicao]==-1:
                tabuleiro[posicao] = vez
                # Se a jogada foi do cliente, avisar a ele que deu tudo certo
                # enviando o tabuleiro preenchido para ele.
                if vez == 1:
                    skt.sendto(str(tabuleiro).encode(),adr)
            else:
                #Caso a jogada tenha sido incorreta                
                if vez == 1:
                    print("O cliente é muito noob, errou.")
                    skt.sendto("MOVE_ERROR".encode(),adr)
                else:
                    print("Jogada incorreta. Perdeu, pai")
                    
            aux_modules.printarTabuleiro(tabuleiro)

            if vez == 0:
                vez = 1
            else:
                vez = 0

                
def pvp_online_cliente(skt,servidorIP):
    # Handshake
    skt.sendto("HANDSHAKE".encode(),(servidorIP,5001))
    
    while True:
        msg,adr = skt.recvfrom(1024)
        msg = msg.decode()

        # Caso não receba uma lista, o jogo acabou
        if msg[0]!="[":
            if msg == "WINNER":
                print("Boa, boy. Tu gera, visse.")
                break
            elif msg == "LOSER":
                print("Tu é fraco. Foi gg izi")
                break
            elif msg == "DRAW":
                print("Empatou, comadres")
                break
        # Caso receba um tabuleiro, a coisa tem que continuar
        else:
            # Receber e mostrar o tabuleiro
            recv_tabuleiro(msg)

        print("Esperando a vez...")
        msg, adr = skt.recvfrom(1024)
        msg = msg.decode()

        if msg == "YOUR_TURN":
            # Receber a jogada do jogador
            print("SUA VEZ")
            posicao = int(input(">>> "))

            # Enviar a jogada
            skt.sendto(str(posicao).encode(),(servidorIP,5001))

            # Esperar a confirmação da jogada
            print("Esperando confirmação da jogada...")
            msg,adr = skt.recvfrom(1024)

            if msg.decode() == "MOVE_ERROR":
                print("Jogada incorreta, boy.")
            else:
                recv_tabuleiro(msg.decode())

            
        
def recv_tabuleiro(msg):
    msg = msg[1:-1]
    tabuleiro = msg.split(", ")
    i = 0
    while i<len(tabuleiro):
        tabuleiro[i]=int(tabuleiro[i])
        i = i+1
    aux_modules.printarTabuleiro(tabuleiro)



        
        
        
        
    
        
        
 
        
                      
        
