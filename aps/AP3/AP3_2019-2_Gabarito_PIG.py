#!/usr/bin/env python
#coding: UTF-8

class Intervalo:
    u"""Representa um intervalo [a,b] entre 2 valores a e b (números
    inteiros ou ponto-flutuante)."""

    def __init__(self,a,b):
        u"""Cria um intervalo entre a e b. Os valores a e b podem
        ser dados em qualquer ordem."""
        self.a,self.b = min(a,b),max(a,b)

    def __repr__(self):
        u"""Retorna uma representação string deste objeto."""
        return "Intervalo("+str(self.a)+","+str(self.b)+")"

    def intersecao (self,i):
        u"""Retorna um objeto da classe Intervalo com a interseção entre self e o 
        intervalo i, caso exista, ou causa uma exceção ValueError caso contrário.
        Assume-se que 2 intervalos se intersectam se têm ao menos um ponto em comum."""
        a,b=max(self.a,i.a),min(self.b,i.b)
        if a > b: raise ValueError
        return Intervalo(a,b)
        
    def uniao(self,i):
        u"""Retorna um objeto da classe Intervalo com a união entre self e o 
        intervalo i. Assume-se que união de dois intervalos é o menor intervalo
        que contém ambos"""
        a,b=min(self.a,i.a),max(self.b,i.b)
        return Intervalo(a,b)

def adiciona(l,i):
    u"""Dada l, uma lista de intervalos que não se intersectam, retorna uma nova lista 
    contendo incluindo o novo intervalo i dado. Se i intersecta algum intervalo j
    de l este é substituído pela união de i e j, de tal maneira que a lista resultante
    só contenha intervalos que não se intersectam."""
    for k,j in enumerate(l):
        try:
            x = i.intersecao(j)
            return adiciona(l[:k]+l[k+1:],i.uniao(j))
        except ValueError:
            pass
    return l+[i]

print (Intervalo(4,1).uniao(Intervalo(10,2)))
print (Intervalo(1,4).intersecao(Intervalo(2,10)))

try:
    print (Intervalo(1,4).intersecao(Intervalo(6,10)))
except ValueError:
    print ("Deu Bode")
l = adiciona([Intervalo(2,3)],Intervalo(0,1))

print (l)
l = adiciona(l,Intervalo(1,2))
print (l)
l = adiciona(l,Intervalo(7,9))
print (l)
l = adiciona(l,Intervalo(4,5))
print (l)
l = adiciona(l,Intervalo(2,8))
print (l)
