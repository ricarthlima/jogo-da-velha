from socket import *

def ouvir():
    skt = socket(AF_INET,SOCK_DGRAM)
    skt.bind(("",5001))
    msg,adr = skt.recvfrom(1024)
    skt.close()
    return msg,adr
       
def falar(mensagem,adr):
    skt = socket(AF_INET,SOCK_DGRAM)
    skt.sendto(mensagem.encode(),(adr,5001))
    skt.close()
        
