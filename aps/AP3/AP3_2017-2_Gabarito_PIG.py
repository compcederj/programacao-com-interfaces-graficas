#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, functools
from random import choice

class QuebraCabeca:
    "Quebra-cabeca tradicional de 15 pecas."
    def __init__(self):
        "Construtor. Monta o tabuleiro de 4x4 aleatoriamente."

        pecas = list(range(16))
        pecas [0] = " "
        self.tabuleiro = []
        while pecas != []:
            x = choice(pecas)
            self.tabuleiro += [x]
            del pecas[pecas.index(x)]

    def __repr__(self):
        "Retorna uma string que representa o tabuleiro."

        separador = "+--"*4 + "+\n"
        resultado = separador
        for i in range(16):
            if i%4 == 0: resultado += "|"
            resultado += "%2s|" % str(self.tabuleiro[i])
            if i%4 == 3: resultado += "\n" + separador
        return resultado

    def ganhou (self):
        "Retorna True se as 15 primeiras casas contêm os números de 1 a 15"

        return self.tabuleiro[0:15]==list(range(1,16))

    def validas (self):
        """Retorna uma lista com os números das peças livres
         (que podem ser movidas)"""

        resultado = []
        i = self.tabuleiro.index(" ")
        if i+4 <= 15: resultado+=[self.tabuleiro[i+4]] # up
        if i-4 >= 0:  resultado+=[self.tabuleiro[i-4]] # down
        if i%4 != 0:  resultado+=[self.tabuleiro[i-1]] # left
        if i%4 != 3:  resultado+=[self.tabuleiro[i+1]] # right
        return resultado

    def joga (self,peca):
        """Movimenta a peça dada. Levanta exceção ValueError caso peça não
        seja válida"""

        # print QuebraCabeca.validas()  <--- Errado!!! gera exceção abaixo:
        #   unbound method validas() must be called with QuebraCabeca instance
        #   as first argument (got nothing instead)
        if peca not in self.validas():
            raise ValueError("Escolha uma das seguintes pecas: "+\
                functools.reduce(lambda a,b: str(a) + "," + str(b), self.validas()))
        i = self.tabuleiro.index(peca)
        j = self.tabuleiro.index(" ")
        self.tabuleiro[i],self.tabuleiro[j] = \
        self.tabuleiro[j],self.tabuleiro[i]

def main():
    qc = QuebraCabeca()
    while not qc.ganhou():
        print (qc)
        try:
            qc.joga(int(input ("Entre com o numero da peca: ")))
        except ValueError as e:
            print ("Erro: %s " % e)
        except SyntaxError:
            sys.exit ("Fim")
        except Exception as e: 
            print ("Nao entendi %s: " % e)
        except KeyboardInterrupt as e:
            sys.exit(e)
    print (qc)

if __name__=="__main__":
    while True:
       main()

