"""
Problem: https://rosalind.info/problems/cons/

This program parses a file containing DNA strings in FASTA format, computes the
profile matrix, and derives the consensus sequence. The consensus sequence and
the profile matrix are then written to an output file.

- DNA strings are stored as lists.
- Profile matrix keeps the count of 'A', 'C', 'G', and 'T' at each position in the DNA strings.
- The consensus string is derived by selecting the most frequent nucleotide at each position.
"""


import numpy as np

num_positions = 0
nucleotides = ['A', 'C', 'G', 'T']
def parse_string(file_name):
    """
    Parses the input file containing DNA strings in FASTA format.

    Args:
    - file_name (str): Name of the file to read DNA sequences from.

    Returns:
    - dna_strings (list): List of parsed DNA strings.
    """
    dna_strings = []
    dna_string = ''
    with open(file_name, "r") as f:
        strings = f.readlines()

    for line in strings:
        line = line.rstrip()
        if  line.startswith(">"):
            if dna_string:
                dna_strings.append(dna_string)
                dna_string = ""
        else:

            dna_string +=line
    # Append the last DNA string after finishing reading the file
    if dna_string:
        dna_strings.append(dna_string)

    global num_positions
    num_positions = max(len(dna) for dna in dna_strings)
    return dna_strings



def create_consensus(dna_strings):
    """
    Creates a profile matrix from a list of DNA strings.

    Args:
    - dna_strings (list): List of DNA strings.

    Returns:
    - profile_matrix (ndarray): A 4xN matrix where N is the length of the DNA strings,
                                and each row corresponds to the counts of 'A', 'C', 'G', 'T' at each position.
    """
    global num_positions

    # Initialize a profile matrix with zeros (4 rows for A, C, G, T)
    profile_matrix = np.zeros((4, num_positions), dtype=int)
    print(profile_matrix.shape)
    #Dictionary to map nucleotides to corresponding row indices in the profile matrix
    nt_to_index = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

    # Fill the profile matrix by counting nucleotides at each position
    for dna_string in dna_strings:
        for position, nucleotide in enumerate(dna_string):
            profile_matrix[nt_to_index[nucleotide], position] +=1

    return profile_matrix


def maxNtPerPos(prof_matrix):
    """
    Determines the most frequent nucleotide at each position from the profile matrix.

    Args:
    - prof_matrix (ndarray): The profile matrix.

    Returns:
    - max_nu
    """
    global nucleotides
    max_nucleotides = []
    # Iterate over each position and find the nucleotide with the highest count
    for pos in range(num_positions):
        max_index = np.argmax(prof_matrix[:, pos])
        max_nucleotid = nucleotides[max_index]
        max_nucleotides.append(max_nucleotid)
    return max_nucleotides

def printConsensus(max_nucleotides, prof_matrix):
    """
    Prints and writes the consensus string and profile matrix to an output file.

    Args:
    - max_nucleotides (list): The consensus nucleotides.
    - prof_matrix (ndarray): The profile matrix.
    """

    #print consnsus string
    consensus_str = "".join(max_nucleotides)

    with open("output_file.txt", "w") as output:
        output.write(f"{consensus_str} \n")
        #Write each row of the profile matrix for A, C, G, T
        for i, nt in enumerate(nucleotides):
            counts = " ".join(map(str, prof_matrix[i]))

            output.write(f"{nt}: {counts} \n")

def main():
    """
    Main function to execute the program:
    1. Parse the DNA strings.
    2. Create the profile matrix.
    3. Find the consensus string.
    4. Write results to an output file.
    """

    dna_strings = parse_string("rosalind_cons.txt")
    prof_matrix = create_consensus(dna_strings)
    max_nucleotides = maxNtPerPos(prof_matrix)
    printConsensus(max_nucleotides,prof_matrix)

if __name__ == "__main__":
    main()
