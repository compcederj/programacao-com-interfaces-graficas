#!/usr/bin/env python
# coding: UTF-8

# 1)
# [1, 3]
# [1, 3, 2, 1, 3, 2]

# 2)
# [4, 5, 1, 2, 3]
# [1, 2, 4, 5, 3]

# 3)

from random import random

class Forca:
    
    palavras = ["abacaxi", "xicara", "chapeu", "procuracao"]
    
    def __init__(self):
        """Inicia um novo jogo de forca."""
        self.palavra = self.palavras[int(random()*len(self.palavras))]
        self.erros = 0
        self.chutadas = set([self.palavra[0]])
    
    def joga(self,letra):
        """Registra o palpite na letra dada. Levanta a exceção ValueError se
        a letra já foi jogada antes ou se letra não é um caractere entre
        "a" e "z". Levanta a exceção IndexError se a letra dada é o sexto 
        palpite errado. Retorna True se o jogador acertou todas as letras ou
        False em caso contrário."""
        if letra in self.chutadas or letra < "a" or letra > "z" \
            or len (letra) != 1: 
            raise ValueError
        if letra not in self.palavra: 
            self.erros+=1
            if self.erros == 6: 
                raise IndexError
        self.chutadas.add(letra)
        return len([x for x in self.palavra if x not in self.chutadas])==0
    
    def __repr__(self):
        """Retorna uma representação do jogo no momento"""
        x = ""
        for y in self.palavra:
            if y in self.chutadas: x+=y
            else: x+= "_"
        y = str(6 - self.erros)+" palpites restantes"
        return x+"\n"+y
        
jogo = Forca()
ok = True
while True:
    print (jogo)
    letra = input("Palpite? ")
    try:
        if jogo.joga(letra): break
    except ValueError:
        print ("Palpite inválido: ",letra)
    except IndexError:
        ok = False
        break
print ("Você ganhou" if ok else "Você perdeu")
            
        
