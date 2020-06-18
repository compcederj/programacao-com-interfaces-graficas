#!/usr/bin/env python
# coding: UTF-8
#
## @package DNAStrand
#
#   Playing with string matching.
#
#   @author Paulo Roma
#   @since 15/12/2019
#   @see https://www.sciencedirect.com/topics/medicine-and-dentistry/dna-strand
#
import sys

class DNAStrand:

    ## Valid DNA symbols.
    symbols = 'ATCG'

    ##
     # Constructs a DNAStrand with the given string of data, 
     # normally consisting of characters 'A', 'C', 'G', and 'T'.
     # Raises a ValueError exception, in case of an invalid givenData strand.
     #
     # @param givenData string of characters for this DNAStrand.
     #
    def __init__(self, givenData):
        ## Strand of this DNA, in upper case.
        self.strand = givenData.upper()

        # ...


    ## Returns a string representing the strand data of this DNAStrand.
    def __str__(self):
        return self.strand


    ##
     # Returns a new DNAStrand that is the complement of this one,
     # that is, 'A' is replaced with 'T' and so on.
     #
     # @return complement of this DNA.
     #
    def createComplement(self):
        complement = ""

        # ....
        
        return DNAStrand(complement)
    

    ##
     # Returns a string showing which characters in this strand are matched
     #  with 'other', when shifted left by the given amount.
     #
     # @param other given DNAStrand.
     # @param shift number of positions to shift other to the left.
     # @return a copy of this strand, where matched characters are upper case 
     #         and unmatched, lower case.
     #
    def findMatchesWithLeftShift(self, other, shift):

        matches = 0
       
        # ...
 
        return matches
    

    ##
     # Returns a string showing which characters in this strand are matched 
     # with 'other', when shifted right by the given amount.
     #
     # @param other given DNAStrand.
     # @param shift number of positions to shift other to the right.
     # @return a copy of this strand, where matched characters are upper case 
     #         and unmatched, lower case.
     #
    def findMatchesWithRightShift(self, other, shift):

        matches = 0

        # ...
        
        return matches
    

    ##
     # Returns the maximum possible number of matching base pairs,
     # when the given sequence is shifted left or right by any amount.
     #
     # @param other given DNAStrand to be matched with this one.
     # @return maximum number of matching pairs.
     #
    def findMaxPossibleMatches(self, other):
        COUNT = 0

        # ...
        
        return COUNT
    

    ##
     # Returns the number of matching pairs,
     # when 'other' is shifted to the left by 'shift' positions.
     #
     # @param other given DNAStrand to match with this strand.
     # @param shift number of positions to shift other to the left.
     # @return number of matching pairs.
     #
    def countMatchesWithLeftShift(self, other, shift):
        count = 0

        # ...
        
        return count
    

    ##
     # Returns the number of matching pairs,
     # when 'other' is shifted to the right by 'shift' positions.
     #
     # @param other given DNAStrand to be matched with this one.
     # @param shift number of positions to shift other to the right.
     # @return number of matching pairs.
     #
    def countMatchesWithRightShift (self, other, shift):
        count = 0

        # ...
        
        return count
    

    ##
     # Determines whether all characters in this strand 
     # are valid ('A', 'G', 'C', or 'T').
     #
     # @return True if valid, and False otherwise.
     #
    def isValid(self):
        valid = True

        # ...
        
        return valid
    

    ##
     # Counts the number of occurrences of the given character in this strand.
     #
     # @param ch given character.
     # @return number of occurrences of ch.
     #
    def letterCount(self,ch):
        count = 0

        # ...
        
        return count
    

    ##
     # Returns True if the two characters form a base pair 
     # ('A' with 'T' or 'C' with 'G').
     #
     # @param c1 first character.
     # @param c2 second character.
     # @return True if they form a base pair, and False otherwise.
     #
    def matches(self, c1, c2):
        match = False

        # ...
 
        return match
    
## Main program for testing.
 #
 # @param args two DNA strands.
 #
def main (args=None):

    if args is None:
       args = sys.argv

    if len(args) == 5:
       d = DNAStrand(args[1])
       d2 = DNAStrand(args[2])
       ls = int(args[3])
       rs = int(args[4])
    else:
       d = DNAStrand ("AGAGCAT")
       d2 = DNAStrand ("TCAT")
       ls = 2
       rs = 3

    print("Complement: %s" % d.createComplement()) 
    print("Count A in %s: %d" % (d, d.letterCount('A')))
    print("%s isValid: %r" % (d, d.isValid()))
    print("Strand: %s" % d2)
    print("RightShift: %s, %d = %s" % (d, rs, d2.findMatchesWithRightShift(d,rs)))
    print("Left Shift: %s, %d = %s" % (d, ls, d2.findMatchesWithLeftShift(d,ls)))
    print("Maximum Matches: %d" % d.findMaxPossibleMatches(d2))
    print("Number of matches left shift: %s, %d = %s" % (d2, ls+rs, d.countMatchesWithLeftShift(d2,ls+rs)))

if __name__ == "__main__":
   sys.exit(main())        
