#!/usr/bin/env python
# coding: UTF-8

import sys

class Particao:
    """Define uma partição de um todo em partes."""
    
    def __init__(self,*p):
        """Define a divisão de um todo (somatório dos elementos 
           de uma lista de números) em partes."""
        s = sum(p)
        self.t = 1
        #self.partition = [float(x)/s for x in p]
        self.partition = list(map(lambda n: float(n)/s, p))

    @property
    def todo(self):
        """Retorna o valor do todo."""
        return self.t
      
    @todo.setter
    def todo(self,t):
        """Passa a assumir que o tamanho do todo é t,
           ao invés de 1.""" 
        self.t = t

    def __len__(self):
        """Retorna o número de partes"""
        return len(self.partition)
    
    def __getitem__(self,key):
        """Retorna o tamanho da key'ésima parte"""
        return self.partition[key]*self.todo

    def __repr__(self):
        """Retorna uma string com o conteúdo detalhado da partição."""
        return "%s: len = %d, todo = %f" % (str(self), len(self), self.todo) 

    def __str__(self):
        """Retorna uma string com o conteúdo da partição."""
        #return " ".join([str(x) for x in self])
        return " ".join(map(str,self))

def main():    
    """Resultado da execução de main():
       [0.2, 0.5, 0.3]
       20.0 50.0 30.0: len = 3, todo = 100.000000
       0.45454545454545453 0.5454545454545454: len = 2, todo = 1.000000
       5.0 6.0: len = 2, todo = 11.000000"""

    p = Particao(*[2,5,3]) # construtor com número variável de args
    print ("[%s]" % str(p).replace(' ', ', ') )
    p.todo = 100           # todo é uma propriedade de p
    print ("%r" % p)
    p = Particao(5,6)
    print( "%r" % p)
    p.todo = 11
    print(repr(p))

if __name__=="__main__":
    sys.exit(main())
