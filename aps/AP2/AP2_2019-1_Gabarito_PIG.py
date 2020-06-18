#!/usr/bin/env python
#coding: UTF-8

import sys

print ("+".join(map(str,filter(lambda x:x%3,range(9)))))

class D:
    def __init__(self,x):
        self.x = set(x)
    def __add__(self,d):
        return D(list(self.x)+list(d.x))
    def __sub__(self,d):
        return D(list(self.x.difference(d.x)))
    def __repr__(self):
        x = list(self.x)
        x.sort()
        return str(x)
print (D(range(10))-D(range(5,15))+D([10,1]))

class Polinomio(object):
    """Representa um polinômio sobre a incógnita x."""
    
    def __init__(self,x):
        """Construtor a partir de uma lista de coeficientes."""
        self.x = x[:]
        
    def __add__(self,p):
        """Retorna a soma deste polinômio com o polinômio p."""
        n = min(len(self.x),len(p.x))
        x = [a+b for a,b in zip(self.x[:n],p.x[:n])] 
        return Polinomio(x + self.x[n:]+p.x[n:])

    def __sub__(self,p):
        """Retorna a diferença entre este polinômio e o polinômio p."""
        n = min(len(self.x),len(p.x))
        x = [a-b for a,b in zip(self.x[:n],p.x[:n])] 
        return Polinomio(x + self.x[n:]+[-y for y in p.x[n:]])
        
    def __mul__(self,p):
        """Retorna o produto entre este polinômio e o polinômio p."""
        x = [0]*(len(self.x)+len(p.x))
        for i in range(len(self.x)):
            for j in range(len(p.x)):
                x[i+j] += self.x[i]*p.x[j]
        return Polinomio(x)

    def __repr__(self):
        """Retorna uma string que descreve o polinômio."""
        r = []
        if len(self.x) > 0 and self.x[0] != 0: 
            r.append("%d" % self.x[0])
        if len(self.x) > 0 and self.x[1] != 0: 
            r.append("%d x" % self.x[1])
        for i in range(2,len(self.x)):
            if self.x[i] != 0: 
               r.append ("%d x^%d" % (self.x[i],i))
        return " + ".join(r)

    def __str__(self):
        """Idêntica ao __repr__, mas retorna x^n ao invés de 1 x^n, 
           para qualquer n."""
        return repr(self).replace("1 x", "x") 

def main():
    print (Polinomio([1,0,-3]))
    print (Polinomio([1,0,3])+Polinomio([-3,1,1]))
    print (Polinomio([1,0,3])+Polinomio([-3,1,-2]))
    print (Polinomio([1,0,3])-Polinomio([-3,1,1]))
    print (Polinomio([1,0,3])*Polinomio([-3,1,1]))

if __name__ == '__main__':
   sys.exit(main())
