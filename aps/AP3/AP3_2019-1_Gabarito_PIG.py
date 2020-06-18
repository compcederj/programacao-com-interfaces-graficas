#!/usr/bin/env python
#coding: UTF-8

try:
    from tkinter import *     # python 3
except ImportError:
    from Tkinter import *     # python 2

class Pedra:
    "Representa uma pedra do jogo"

    tam = 40 # Tamanho da pedra

    def __init__(self,tipo):
        "Constrói uma pedra dado seu tipo (numero de 0 a 15)"
        self.tipo = tipo
        # representação binária reversa do tipo.
        self.padrao = [tipo%2==1,    tipo//2%2==1,
                       tipo//4%2==1, tipo//8%2==1]

    def desenha(self,x,y):
        "Desenha a pedra com canto superior esquerdo em x,y"
        a = [x+self.tam*i for i in [0, 0.5, 1]]
        b = [y+self.tam*i for i in [0, 0.5, 1]]
        p = [(0,0), (1,0), (2,0) ,(0,1)]
        q = [(2,2), (1,2), (0,2), (2,1)]
        canvas.create_rectangle(x,y,x+self.tam,y+self.tam, outline='white')
        for i in range(4):
            if self.padrao[i]:
               canvas.create_line(a[p[i][0]], b[p[i][1]], a[q[i][0]], b[q[i][1]], fill='white')

def main():
    global canvas
    root = Tk()
    root.title('Questão 2')
    root.geometry('+0+0')
    canvas = Canvas(root, width=Pedra.tam*7, height=Pedra.tam*8, background='black')
    canvas.pack(fill=BOTH,expand=YES)
    j = 0
    k = 0
    for i in range(16):
        k += 1
        if i % 4 == 0: 
           j += 1
           k = 0
        p = Pedra(i)
        p.desenha(p.tam*(1.5*k + 0.5), p.tam*1.5*j)
    root.mainloop()

import sys
if __name__ == '__main__':
   sys.exit(main())
