#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, random

class Joias: 
    """Implementação parcial do jogo "Jewels".""" 

    def __init__(self): 
        """Inicializa o jogo.""" 
        self.tab = [[0 for j in range(8)] for i in range(8)] 
        self.preenche_tabuleiro() 
        
    def preenche_vazias(self): 
        """Preenche as casas vazias (preenchidas com zeros) do tabuleiro.""" 
        for i in range(8): 
            for j in range(8): 
                if self.tab[i][j]==0: self.tab[i][j]=random.randint(1,7) 
                
    def preenche_tabuleiro(self): 
        """Preenche o tabuleiro, assegurando que não há triplas.""" 
        self.preenche_vazias() 
        while self.limpa_triplas(): 
              self.atualiza_tabuleiro()

    def atualiza_tabuleiro(self):
        """Atualiza o tabuleiro após um movimento."""
        self.compacta_colunas()
        self.preenche_vazias()
            
    def procura_triplas(self): 
        """Procura no tabuleiro três ou mais peças seguidas iguais em linhas ou
        colunas. Retorna uma lista de posições onde tais peças se encontram. Uma
        posição é um par (linha,coluna) onde linha e coluna são índices de 0 a 7.""" 
        triplas = []
        for i in range(8):
            for j in range(6):
                if self.tab[i][j] == self.tab[i][j+1] and \
                   self.tab[i][j] == self.tab[i][j+2]:
                   triplas += [(i,j),(i,j+1),(i,j+2)]
        for j in range(8):
            for i in range(6):
                if self.tab[i][j] == self.tab[i+1][j] and \
                   self.tab[i][j] == self.tab[i+2][j]:
                   triplas += [(i,j),(i+1,j),(i+2,j)]
        return triplas
        
    def limpa_triplas(self): 
        """Limpa as triplas do tabuleiro, substituindo as peças por zeros. 
        Retorna True se houve triplas a limpar ou False, caso contrário.""" 
        posicoes = self.procura_triplas() 
        for i,j in posicoes: self.tab[i][j] = 0 
        return len(posicoes)

    def swap (self,a,b,c,d):
        """Troca as posições self.tab[a][b] com self.tab[c][d]."""
        self.tab[a][b], self.tab[c][d] = self.tab[c][d], self.tab[a][b]

    def compacta_colunas(self): 
        """Compacta as colunas do tabuleiro fazendo com que os zeros do tabuleiro 
        se concentrem nas linhas de número mais alto.""" 
        for j in range(8):
            for i in range(7,0,-1):
                for k in range(i):
                    if self.tab[k][j] == 0:
                       self.swap (k,j,k+1,j)
            
    def __repr__(self): 
        """Retorna uma string com uma representação do tabuleiro.""" 
        return "0 1 2 3 4 5 6 7\n\n"+ \
                "\n".join([" ".join([" .+*$%#@"[self.tab[i][j]] \
                     for j in range(8)]) 
                         for i in range(7,-1,-1)])+"\n"

def mainloop():
    global total
    while True:
      try:
         if (sys.hexversion > 0x03000000):
            (i,j)= tuple(int(x.strip()) for x in input("Entre a posição (i,j): ").split(','))
         else:
            (i,j)=input("Entre a posição (i,j): ")
         i = min(max(0,i),7)
         j = min(max(0,j),7)
         pos=input("Entre a direção (up, down, left, right): ")
         if pos == 'left' and j > 0:
            l = j - 1
            k = i
         elif pos == 'up' and i < 7:
            k = i + 1
            l = j
         elif pos == 'down' and i > 0:
            k = i - 1
            l = j
         elif pos == 'right' and j < 7:
            l = j + 1
            k = i
         else:
            raise ValueError ("Direção Inválida")
      except (NameError,TypeError) as e:
         print ("Tente de novo (%s):" % e)
         print ("posição: 0..7, 0..7")
      except SyntaxError:
         print ("Total de jóias = ", total)
         sys.exit ("Fim")
      except KeyboardInterrupt as e:
         sys.exit(e)
      else:
         break

    jew.swap (i,j,k,l)
    nt = jew.limpa_triplas()
    if nt > 0:  # um único movimento pode criar duas triplas
       jew.atualiza_tabuleiro()
       total += nt/3
    else:
       jew.swap (k,l,i,j)
       raise ValueError ("Movimento Inválido")

def main():
    total = 0
    jew = Joias()
    print (jew)
    while True:
       try:
          mainloop()
       except ValueError as e:
          print (e)
       print (jew)

if __name__=="__main__":
    while True:
       main()
