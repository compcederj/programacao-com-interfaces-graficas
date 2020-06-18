#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, random

class forca:
      filename = "forca.txt"
      # só é executado uma vez, sendo o mesmo para qualquer instância da classe.
      try:
         textf = open(filename, 'r')
      except IOError:
         sys.exit('Cannot open file %s for reading' % filename)

      opcoes = []
      for line in textf:
          opcoes.append (line.replace('\n','').replace(' ',''))      

      textf.close()

      def __init__ (self):
          self.palavra = random.choice (forca.opcoes)
          self.texto = list("_"*len(self.palavra))

      def __repr__(self): 
          """Retorna uma representação do estado atual do jogo de forca, 
          onde letras ainda não adivinhadas aparecem substituídas pelo 
          caractere '_'."""
          return "".join(self.texto)

      def adivinha(self, letra): 
          """Retorna verdadeiro se letra é uma das letras da palavra. 
          Nesse caso, a representação do jogo é alterada para refletir a 
          nova letra corretamente adivinhada. 
          Caso a letra já tenha sido chutada no passado, 
          levanta a exceção ValueError."""
 
          if letra in self.texto:
             raise ValueError ('Letra já usada')
          else:
             for l in range (len(self.palavra)):
                 if self.palavra[l] == letra: 
                    self.texto[l] = letra
             return letra in self.palavra

      def ganhou(self):
          """Retorna verdadeiro se todas as letras da palavra já foram adivinhadas."""

          return str(self) == self.palavra

def main():
    jogo = forca()
    tentativas = 7
    while tentativas > 0 and not jogo.ganhou():
        print jogo
        letra = ""
        try:
           while not letra:
                 letra = raw_input("Chute uma letra: ")
           if jogo.adivinha(letra): 
              print "Acertou!"
           else:
              print "Errou!"
              tentativas -= 1
        except (SyntaxError,KeyboardInterrupt):
           sys.exit ("Fim")
        except ValueError,e:
           print "Erro:", e

    if jogo.ganhou(): print "Parabéns! ",
    print "A palavra era '%s'\n\n" % jogo.palavra

while True:
    main()
