#!/usr/bin/env python3

"""Rosalind problem: https://rosalind.info/problems/grph/
Author:Haris Spyridis
"""

def parse_fasta(fasta_file):
    """
    Function to parse a FASTA file and store sequences in a dictionary.

    Input:
        fasta_file (str): Path to the FASTA file.

    Output:
        dict: A dictionary where the keys are sequence names and the values are the sequences.
    """

    data_dic = {}

    with open(fasta_file, "r") as f:
        data = f.readlines()

    for line in data:
        line = line.strip()

        if line.startswith(">"):
            seq_name = str(line[1:])
            data_dic[seq_name] = ""

        else:
            data_dic[seq_name] +=line


    return data_dic


def find_overlaps(adj_list):
    """
    Function to find 3-character overlaps between sequence ends and starts.

    Input:
        adj_list (dict): Dictionary where keys are sequence names and values are sequences.

    Output:
        dict: A dictionary representing the overlap graph where each key is a sequence,
              and the value is a list of sequences that overlap with it.
    """

    list_seqs = list(adj_list.values())

    overlp_graph = {}
    for i in range(len(list_seqs)):
        for j in range(len(list_seqs)):
            #avoid comparing seq with itself
            if i != j:
                seq1 = list_seqs[i]
                seq2 = list_seqs[j]
                #check If the last 3 characters of seq1 match the first 3 of seq2
                if seq1[-3:] == seq2[:3]:
                    if seq1 not in overlp_graph:
                        overlp_graph[seq1] = []
                    if seq2 not in overlp_graph[seq1]:
                        overlp_graph[seq1].append(seq2)

    return overlp_graph
def write_to_file(overlap_graph,sequences_to_names):
    """
    Function to write the overlap relationships between sequences to a file.

    Input:
        overlap_graph (dict): A dictionary where keys are sequences and values are lists of sequences that overlap.
        sequences_to_names (dict): A dictionary mapping sequences to their corresponding names.

    Output:
        None: Writes the overlap results to 'output.txt'.
    """
    # Write results to output file
    with open("output.txt", "w") as f:

        for key_seq, follow_sequences in overlap_graph.items():
            #Get the name of the current sequence
            key_name = sequences_to_names.get(key_seq)

            for follower_seq in follow_sequences:
                #get the name of the following sequence
                fol_name = sequences_to_names.get(follower_seq)
                #prepare the line to write to file
                line_to_write = f"{key_name} {fol_name}\n"
                f.write(line_to_write)

def main():
    """
    Main function that parses the input, finds overlaps, and writes results to a file.
    """
    #parse data
    data = parse_fasta("overalp_test.txt")

    #find overlappping sequences
    overlap_grap = find_overlaps(data)
    #Create a mapping of sequences to their corresponding sequence names
    sequences_to_names = {sequence: name for name, sequence in data.items()}


if __name__ == '__main__':
    main()