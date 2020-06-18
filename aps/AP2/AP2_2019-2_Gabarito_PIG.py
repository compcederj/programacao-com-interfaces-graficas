#!/usr/bin/env python
#coding: UTF-8

# 1.)
# 4+ba-a-a-a-
# 2+[1, 2, 2]
#
# 2.)
# [2, 1, 1]
# [2, 2, 0, 0]
#
#3.)

from random import shuffle

class Dominos:
    "Simula um jogo de dominó"
    
    def __init__(self):
        "Inicializa um novo jogo"
        self.estoque = [(a,b) for a in range(7) for b in range(a,7)]
        shuffle(self.estoque)
        self.tabuleiro = []
        self.horizontal = True
        
    def compra (self):
        """Retira uma peça ainda não sorteada do estoque e a retorna.
        Levanta a exceção ValueError caso não existam mais peças"""
        if len(self.estoque)>0: return self.estoque.pop()
        raise ValueError
        
    def coloca(self,peca,extremidade):
        """Dada uma peça (tupla da forma a,b), e uma extremidade (0 ou 1),
        adiciona a peça ao jogo estendendo a extremidade dada. Se a peça
        não pode ser colocada na extremidade dada, retorna False."""
        a,b = peca
        if len(self.tabuleiro) == 0: 
            self.tabuleiro = [a,b]
            return True
        x,y = self.tabuleiro[0],self.tabuleiro[-1]
        if extremidade == 0: 
            if x == a: 
                self.tabuleiro = [b,a]+self.tabuleiro
            elif x == b: 
                self.tabuleiro = [a,b]+self.tabuleiro
            else: 
                return False
            self.horizontal = not self.horizontal
        else:
            if y == a: 
                self.tabuleiro = self.tabuleiro+[a,b]
            elif y == b: 
                self.tabuleiro = self.tabuleiro+[b,a]
            else: 
                return False
        return True

    def imprime(self):
        """Imprime o jogo até o momento. A impressão tem que ser na
        forma de uma 'escadinha', isto é, as peças colocadas na mesa
        se alternam na posição horizontal e vertical. O leiaute
        entre uma jogada e a próxima não pode mudar!"""
        dx = ""
        horiz = self.horizontal
        for i in range(0,len(self.tabuleiro),2):
            a,b = self.tabuleiro[i:i+2]
            if horiz:
                print (dx+str(a)+str(b))
                dx += " "
            else:
                print (dx+str(a))
                print (dx+str(b))
            horiz = not horiz
            
d = Dominos()
for i in range(6):
    p = d.compra()
    print ("Compra:", p)
    if d.coloca(p,0) or d.coloca(p,1): d.imprime()
