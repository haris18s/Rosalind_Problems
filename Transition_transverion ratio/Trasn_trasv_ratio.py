#!/usr/bin/env python3


from sys import argv

def parse_fasta_dic(file):
    """
    Parses a FASTA file and returns a dictionary where the keys are the sequence identifiers
    and the values are the corresponding sequences.

    Input:
        file (str): Path to the FASTA file.

    Output:
        dic_data (dict): A dictionary containing sequence identifiers as keys and sequences as values.
    """
    with open(file, 'r') as file:
        data = file.readlines()
    dic_data = {}
    identi = None
    sequence = ""
    for line in data:
        line = line.strip()
        if line.startswith(">"):
            if identi != None:
                dic_data[identi] = sequence
            identi = line
            sequence = ""
        else:
            sequence += line

    if identi is not None:
        dic_data[identi] = sequence
    return dic_data




def count_trans_trasnv(seq1, seq2):
    """
    Counts the number of transitions and transversions between two DNA sequences
    and calculates their ratio.

    Input:
        seq1 (str): The first DNA sequence.
        seq2 (str): The second DNA sequence.

    Output:
        ratio (float): The ratio of transitions to transversions.
    """
    num_trans = 0
    num_trasnv = 0
    for nt1, nt2 in zip(seq1, seq2):
        if nt1 != nt2:
            if nt1 == "A" and nt2 == "G" or nt1 == "G" and nt2 =="A":
                num_trans += 1
            elif nt1 == "C" and nt2 == "T" or nt1 == "T" and nt2 =="C":
                num_trans += 1
            else:
                num_trasnv += 1


    #Avoid division by 0 in case thee are no tranversions (denominator)
    if num_trasnv ==0:
        return float('inf') # infinte ration if no transversions
    else:
        ratio = num_trans / num_trasnv

        return ratio


def main():
    input_file = argv[1]
    dic_fasta = parse_fasta_dic(input_file)
    sequences = list(dic_fasta.items())

    if len(sequences) < 2:
        raise ValueError('The inut file must contain exactly 2 sequence')

    sequence1 = sequences[0][1]
    sequence2 = sequences[1][1]


    ratio =count_trans_trasnv(sequence1, sequence2)
    print(f"Transitions/Transversions ratio: {ratio:.6f}")
if __name__ == "__main__":
    main()



#Alternative way of code
# for base1, base2 in zip(seq1, seq2):
#
#     if base1 != base2:
#         if (base1 in 'AG' and base2 in 'AG') or (base1 in 'CT' and base2 in 'CT'):
#             transitions += 1
#         else:
#             transversions += 1
#
#     ratio = transitions / transversions