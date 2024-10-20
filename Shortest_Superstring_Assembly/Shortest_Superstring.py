#!/usr/bin/env python


import itertools

def parse_file(filename):
    """
    Parses the input file to extract sequences associated with each header.

    Args:
    - filename (str): The name of the input file.

    Returns:
    - seqs (list): A list of sequences extracted from the file.
    """
    with open(filename) as f:
        data  = f.readlines()

    dic_seqs = {}
    cuurent_seq = ''
    seq = None
    for line in data:
        line = line.strip()
        if line.startswith(">"):
            if seq:
                dic_seqs[seq] = cuurent_seq

            seq = line[1:]
            cuurent_seq = ''
        else:
            cuurent_seq +=line
    #aapend last sequence
    if cuurent_seq:
        dic_seqs[seq] = cuurent_seq

    #create a list with only the seqs to work
    seqs = [sequence for seq_name, sequence in dic_seqs.items()]

    return seqs

def calculate_overlap(s1,s2):
    """
    Calculates the maximum overlap between two sequences.

    Args:
    - s1 (str): The first sequence.
    - s2 (str): The second sequence.

    Returns:
    - max_overlap (int): The length of the maximum overlap.
    - merged_string (str): The merged string after the overlap.
    """
    max_overlap = 0
    merge_string = s1 + s2
    for i in range(1, min(len(s1), len(s2)) +1):
        if s1[-i:] == s2[:i]:
            max_overlap = i
            merge_string = s1 + s2[i:]

    return max_overlap, merge_string



def greedy_shortest(sequences):
    """
    Merges sequences to find the shortest superstring using a greedy approach.

    Args:
    - sequences (list): List of sequences to merge.

    Returns:
    - str: The shortest superstring containing all input sequences.
    """

    while len(sequences) > 1:
        max_overlap = -1
        best_overlap =  None
        merged_string = None

        best_pair_indices = None
        #loop over all pairs of sequences
        for idx_seq1, idx_seq2 in itertools.permutations(range(len(sequences)), 2):
            # seq1 and sew2 pair
            seq1, seq2 = sequences[idx_seq1], sequences[idx_seq2]
            overlap_len, merged = calculate_overlap(seq1, seq2)

            # keep track the best overlap
            if overlap_len > max_overlap:
                max_overlap = overlap_len
                merged_string = merged

                #indices of best pair
                best_pair_indices = idx_seq1, idx_seq2

        # indeces of seqs with maximum overlap, if found
        idx_seq1, idx_seq2 = best_pair_indices

        # Ensure we remove the higher index first to avoid index shifting
        if idx_seq1 > idx_seq2:
            sequences[idx_seq1] = merged_string
            sequences.pop(idx_seq2)
        else:
            sequences[idx_seq2] = merged_string
            sequences.pop(idx_seq1)

    return sequences[0]


def main():
    #test sequences
    SEQUENCES = ['ATTAGACCTG', 'CCTGCCGGAA', 'AGACCTGCCG', 'GCCGGAATAC']

    #pars file
    #sequences = parse_file('rosalind_long.txt')

    #find the shorest superstring
    shortest_superstring = greedy_shortest(SEQUENCES)
    #write the output to file
    with open("shotest_superstring.txt", 'w') as f:
        f.write(shortest_superstring)


if __name__ == '__main__':
    main()





