from sys import argv

CODONS = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
       "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
       "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
       "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
       "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
       "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
       "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
       "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
       "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
       "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
       "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
       "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
       "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
       "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
       "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
       "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}



def aa_occurances(protein):
    """This function calculates the occurances of each aa in the given protein sequence

    Input: a protein (str) sequence
    Returns: A list containing the number of occurances for each aa present in the protein """
    global CODONS
    list_occu = []
    for aa in protein:
        count =0
        for seq, cha in CODONS.items():
            if aa == cha:
                count += 1
        if count !=0: # because the last iteration will be zero
            list_occu.append(count)
    print(list_occu)
    return list_occu

def multipl(list_occu):
    """ Calculates the number of different RNA string from which  the protein could have been transladedm modulo 1E6

    Input: A list containing the number of occurances for each aa ( output function :aa_occurances)

    Output: int: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000.
    """
    stop_codons = 3
    possibility = 1
    for occu in list_occu:
        possibility = (possibility* occu) % 1E6
        print(possibility)
    return int(possibility * stop_codons)

def main():
    with open(argv[1], 'r') as file_protein:
        protein = ' '.join(file_protein.readlines())

    aa_occur = aa_occurances(protein)
    possibility = multipl(aa_occur)
    print(possibility)
if __name__ =="__main__":
    main()


