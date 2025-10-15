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






def remove_introns(DNA,introns_to_remove):
    DNA_without_intron = DNA

    for substring in introns_to_remove:
        DNA_without_intron = DNA_without_intron.replace(substring, '')
    return DNA_without_intron




def transcription(final_sequence):
    RNA = ""
    for nt in final_sequence:
        if nt ==  "T":
            RNA +="U"
        else:
            RNA +=nt
    return RNA


def traslation(RNA):
    global CODONS
    protein = ""
    for index in range(0, len(RNA), 3):
        for codon_seq, aa in CODONS.items():
            if RNA[index:index + 3] == codon_seq and aa != "STOP" :
                protein += aa
    return protein


def parse_fasta(fasta_file):
    with open(fasta_file, 'r') as fasta_file:
        data = fasta_file.readlines()
    identifier = None
    DNA_seq =""
    dic_fasta = {}
    for line in data:
        line = line.strip()
        if line.startswith(">"):
            if identifier != None:
                dic_fasta[identifier] = DNA_seq
            identifier = line
            DNA_seq = ""
        else:
            DNA_seq += line
    if identifier != None:
        dic_fasta[identifier] = DNA_seq
    return dic_fasta



def seperate_introns_and_seq(dic_fasta):
    dic_to_list = list(dic_fasta.items())
    print(dic_to_list[1][1])
    index = 0
    list_introns= []
    for entry in dic_to_list:

        if index == 0:
            DNA_seq =dic_to_list[0][1]
        else:
            list_introns.append(dic_to_list[index][1])
        index+=1

    return DNA_seq, list_introns

def main():
    dic_fasta = parse_fasta(argv[1])
    DNA_seq, list_introns = seperate_introns_and_seq(dic_fasta)[0], seperate_introns_and_seq(dic_fasta)[1]
    DNA_without_introns = remove_introns(DNA_seq,list_introns)
    mRNA = transcription(DNA_without_introns)
    protein = traslation(mRNA)



if __name__ == "__main__":
    main()
