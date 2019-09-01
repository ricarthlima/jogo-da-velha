def baskhara(a,b,c):
    resultado = (b*(-1))
    denominador = 2*a
    delta = (b**2 - 4*a*c)**(0.5)
    resultado1 = (resultado + delta)/denominador
    resultado2 = (resultado - delta)/denominador
    return (resultado1,resultado2)

def fibonacci(n):
    lista =[]
    for i in range(n+1):
        lista.append(None)
    return memoFibonacci(n,lista)
        
        
    
def memoFibonacci(n,lista):
    if n == 0:
        return 0
    elif n==1:
        return 1

    elif lista[n]!=None:
        return lista[n]
    else:
        lista[n]=(memoFibonacci(n-1,lista)+memoFibonacci(n-2,lista))
        return lista[n]
             
class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def diga_seu_nome(self):
        return "meu nome é " + self.nome
    def diga_sua_idade(self):
        return "minha idade é " + str(self.idade)
    def mais_velho(self, other):
        if self.idade > other.idade:
            return self.nome + " é mais velho que " + other.nome
        else:
            return other.nome + " é mais velh@ que " + self.nome
    
            
    
    

