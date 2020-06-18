#coding: utf-8
#

class Tabela (object):
    """Representa uma tabela de strings genérica."""
    
    def __init__(self):
        """Gera uma tabela vazia com 1 linha e 1 coluna."""

        self.tab = [[None]]
    
    def insere_linhas (self,i,n):
        """Insere n linhas vazias entre a linha i-1 e a linha i da tabela 
		(numeração começa com 0). Para inserir linhas antes da 1a linha, 
		use i=0. Para inserir linhas no fim use i=k onde k é qualquer 
		número maior que o número de linhas da tabela. (2 pontos)"""

        # [ [a00, a01, a02], [a10, a11, a12], [a20, a21, 22] ]
        ncol = len(self.tab[0])
        # [ [None, None, None], [None, None, None], ..., [None, None, None] ]
        rows = [[None]*ncol for j in range(n)]
        self.tab = self.tab[:i]+rows+self.tab[i:]
    
    def insere_colunas (self,i,n):
        """Análogo a insere_linhas, mas insere n colunas antes da coluna i (2 pontos)."""

        ncol = len(self.tab[0])
        # insere em cada linha
        for row in self.tab:
            row[:] = row[:i]+[None]*n+row[i:]
            
    def altera(self,i,j,val):
        """Altera a célula na linha i, coluna j para val. (1 ponto)"""

        self.tab[i][j] = val
        
    def valor(self,i,j):
        """Retorna o valor armazenado na linha i, coluna j. Caso nenhum valor
        tenha sido armazenado nessa célula, retorna None. (1 ponto)"""

        return self.tab[i][j]
    
    def __repr__(self):
        """Retorna uma string representativa da tabela, própria
        para ser impressa. Cada coluna é impressa com as strings 
        alinhadas à direita e tem a largura do maior valor
        armazenado naquela coluna. Colunas vazias são mostradas com 
        largura 1 (um espaço). Linhas são separadas por hífens e
        colunas por barras verticais. Dica: use \n para separar 
        duas linhas: Uma tabela com 1 linha e 1 coluna vazia
        retorna "---\n| |\n---". (4 pontos)"""

        ncol = len(self.tab[0])
        # [1, 1, 1, 1]
        ns = [1]*ncol
        # acha a largura máxima em cada coluna
        for row in self.tab:
            for i,val in enumerate(row):
                if val != None: ns[i] = max(ns[i],len(val))
        print(ns) # imprime a largura de cada coluna, para entender o que foi feito

        hline = '-'*(sum(ns)+ncol+1) # nchar em cada coluna + ncol | + 1
        result = [hline]

        for row in self.tab:
            s = "|"
            for i,val in enumerate(row):
                if val == None: val = ' '
                # coloca espaços à esquerda + val + |
                s += ' '*(ns[i]-len(val))+val+"|"
            result += [s,hline]
        return "\n".join(result)

t = Tabela()
t.insere_linhas(0,3)
print(t)
t.altera(1,0,'aaaaaaa')
print(t)
t.insere_colunas(0,3)
print(t)
print (t.valor(1,0))
print (t.valor(1,3))
t.altera(0,0,'bbbbb')
t.altera(3,0,'cc')
print (t)
