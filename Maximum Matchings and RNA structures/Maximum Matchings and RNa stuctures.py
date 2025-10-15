
def parse_file(filename):
    with open(filename) as f:
        data =f.readlines()

    seq = ""
    for line in data:
        line = line.rstrip()
        if line.startswith(">"):
            continue
        else:
           seq +=line

    return seq

def fact(n):
    """Calculate the factoria of a number"""
    if n ==1:
        return n
    return fact(n-1) *n

import math
def count_matchings(RNA_string):

    #count the num of nucleotidex
    A = RNA_string.count("A")
    C = RNA_string.count("C")
    G = RNA_string.count("G")
    U = RNA_string.count("U")


    #the number of pairs that A can pair with U is the min(A,U). Same holds for G,C.
    #So when we get max(A,U) we need to account for the left over pairs that main unpaired.

    # we make a floor division
    AU = math.factorial(max(A,U)) // math.factorial(max(A,U) - min(A,U))

    GC = math.factorial(max(G,C)) // math.factorial(max(G,C) - min(G,C))

    totalMaxPairings = AU * GC

    return int(totalMaxPairings)

if __name__ == "__main__":
    rna_string = parse_file("rosalind_mmch.txt")
    print(rna_string)
    totalmMaxPairings = count_matchings(rna_string)
    print(totalmMaxPairings)


