#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Tempo:
      def __init__ (self, h=0,m=0,s=0):
          """Constrói um objeto Tempo, de modo que:
                 0 <= h <= 23,
                 0 <= m <= 59, e 
                 0 <= s <= 59"""

          # % ou operador __mod__ é definido como:
          # r + d * (n // d) == n, onde n//d = (floor) n/(float) d
          # -1 % 60 = 59
          # -1/60 = -1, logo r + 60 * -1 = -1 => r = 59

          self.h, self.m, self.s = (h+(m+s//60)//60)%24,(m+s//60)%60,s%60

      def __repr__(self): 
          """Retorna uma representação do tempo."""
          return ("%2s:%2s:%2s" % (str(self.h), str(self.m), str(self.s))).replace (" ","0")

      def __sub__(self, t): 
          """Retorna a diferença de dois tempos."""

          return self + Tempo(-t.h, -t.m, -t.s)
 
      def __add__(self, t):
          """Retorna a soma de dois tempos."""

          return Tempo (t.h+self.h, t.m+self.m, t.s+self.s)

def main():
    print "Tempo(0)-Tempo(0,0,1) = %s" % (Tempo(0)-Tempo(0,0,1))               # 23:59:59
    print "Tempo(0,29,59)+Tempo(0,0,1) = %s" % (Tempo(0,29,59)+Tempo(0,0,1))   # 00:30:00
    print "Tempo(1,59,59)+Tempo(0,0,3) = %s" % (Tempo(1,59,59)+Tempo(0,0,3))   # 02:00:02
    print "Tempo(0)-Tempo(23,0,1) = %s" % (Tempo(0)-Tempo(23,0,1))             # 00:59:59
    print "Tempo(0,120,-125) = %s" % (Tempo(0,120,-125))                       # 01:57:55
    print "Tempo(-1,-1,-1) = %s" % (Tempo(-1,-1,-1))                           # 22:58:59
    t = Tempo (0,2,24)
    print "Tempo (0,2,24) = %s" % t
    t += Tempo (0,4,55)
    print "+= Tempo (0,4,55) = %s" % t
    t += Tempo (0,4,56)
    print "+= Tempo (0,4,56) = %s" % t
    t += Tempo (0,4,49)
    print "+= Tempo (0,4,49) = %s" % t
    t += Tempo (0,5,22)
    print "+= Tempo (0,5,22) = %s" % t
    t += Tempo (0,5,39)
    print "+= Tempo (0,5,39) = %s" % t
    t += Tempo (0,5,8)
    print "+= Tempo (0,5,8) = %s" % t
    t += Tempo (0,4,18)
    print "+= Tempo (0,4,18) = %s" % t
    t += Tempo (0,5,15)
    print "+= Tempo (0,5,15) = %s" % t
    t += Tempo (0,4,40)
    print "+= Tempo (0,4,40) = %s" % t
    t += Tempo (0,4,13)
    print "+= Tempo (0,4,13) = %s" % t
    t += Tempo (0,5,30)
    print "+= Tempo (0,5,30) = %s" % t
    print "Tempo (0,500) = %s" % Tempo(0,500)
  

if __name__=="__main__":
    main()
