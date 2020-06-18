#!/usr/bin/env python
# coding: UTF-8
#
# A simple address book.
#

import sys

## Class for aggregating all personal data in a single object.
#
class personalData:
    ## Constructor from a phone list and an address.
    #
    #  @param l phone list.
    #  @param addr address
    #
    def __init__(self,l=None,addr=''):
        if ( l is None ):
             l = []
        ### Contact phone list.
        self.lPhone = l
        ### Contact address.
        self.address = addr

    ## Returns the phone list of this contact. 
    #
    #  @return the contact phone list.
    #
    def getlPhone(self):
        return self.lPhone

    ## Returns the address of this contact.
    #
    #  @return the contact address.
    #
    def getAddress(self):
        return self.address

    ## Sets the address of this contact.
    #
    #  @param addr the contact address.
    #
    def setAddress(self,addr):
        self.address = addr

    ## Appends a phone list to this contact phone list.
    #
    #  @param l a phone list.
    #
    def setlPhone(self,l):
        self.lPhone += l

    ## Used to print a human readable presentation of an object.
    #  In this case, it prints the contact name and his personal data.
    #
    #  @return a string.
    #
    def __repr__(self):
        txt = ""
        txt += "Endereço: " + self.address + ", Tel: " + " | ".join(self.lPhone)
        return txt

    ## Used to print a human readable presentation of an object.
    #  In this case, it prints the contact name and his personal data.
    #
    #  @return a multi line string.
    #
    def __str__(self):
        txt = ""
        txt += "\nEndereço: " + self.address + '\n' + " | ".join(self.lPhone)
        return txt

## Class for holding an address book.
#
class Agenda:
    ## Constructor. Just creates an empty dictionary.
    #
    def __init__(self):
        ### Dictionary for associating a contact name to a personalData object.
        self.dic = {}

    ## Associates new phones and an address to the given name.
    #
    #  @param nome contact name.
    #  @param lista contact phone list.
    #  @param addr contact address.
    #
    def putPhone(self, nome, lista=None, addr=''):
        if nome in self.dic:
            self.dic[nome].setlPhone(lista)
            if addr != '': self.dic[nome].setAddress(addr)
        else:
            self.dic[nome] = personalData(lista,addr)  # primeira vez

    ## Retrieves the index-th phone of a given contact.
    # 
    #  @param nome contact name.
    #  @param index selects a certain phone from the contact phone list.
    #  @return a phone number or None, if the contact does not exist.
    #
    def getPhone(self, nome, index):
        if nome in self.dic: 
           data = self.dic[nome]
           if data:
              lt = data.getlPhone()  
              if index > 0 and index <= len(lt):
                 return lt[index-1]
        return None
    
    ## Removes a given contact from the address book.
    #
    #  @param nome contact name.
    #
    def remContact(self, nome):
        if nome in self.dic:
           self.dic.pop(nome)

    ## Used to print a human readable presentation of an object.
    #  In this case, it prints the contact name and his personal data.
    #
    #  @return a multi line string.
    #
    def __repr__(self):
        txt = ""
        # items() returns a **copy** of the dictionary’s list of (key, value) tuple pairs.
        for name, pdata in self.dic.items(): 
            txt += name + ': ' + repr(pdata) + '\n'
        txt = txt.split("\n") 
        txt.sort()
        return "\n".join(txt) + "\n"

    ## For printing an address book x by using just print x.
    #  Each line is made up of a name followed by its corresponding personal data.
    #  Names are listed in alphabetical order.
    #
    #  @return a multi line string.
    #
    def __str__(self):
        texto = ""               
        # Python 3 returns a dict_keys object instead of a list
        nomes = list(self.dic.keys())  # name list (the keys) from the dictionary
        nomes.sort()                   # sorted name list
        for nome in nomes:
            texto += nome + ': ' + str(self.dic[nome]) + '\n'
        return texto

## Main program for testing.
#
def main ():
    a = Agenda()
    a.putPhone("Mig", ['2274-4635'], 'Leblon')
    a.putPhone("Eva", ['9087-1234', '2267-6767'], 'UFRJ')
    a.putPhone("Mig", ['9876-1234'] )
    a.putPhone("Cris", ['2111-0000'], 'Ilha do Governador')
    print("\nAgenda(str):\n%s" % a)
    print("Agenda(repr):%s" % repr(a)) 
    print("getPhone Mig - 1: %s" % a.getPhone("Mig",1))
    print("getPhone Mig - 2: %s" % a.getPhone("Mig",2))
    print("getPhone Mig - 3: %s" % a.getPhone("Mig",3))
    print("getPhone Paul - 2: %s" % a.getPhone("Paul",2))
    print("Removed Eva and Peter") 
    a.remContact("Eva")
    a.remContact("Peter")
    print("\nAgenda(str):\n%s" % a)

if __name__=="__main__":
    sys.exit(main())
