s ="AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
code_rna = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"*", "UAG":"*",
    "UGU":"C", "UGC":"C", "UGA":"*", "UGG":"W",
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
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}



def parse_fasta(filename):
    """Function for parsing a fasta file
    Input: a fasta file
    Output: a dic with seq id as a key, and sequence itself as a value.
            In this case because is a single entry file, the sequence string just joined

    """
    fasta_dict = {}
    with open(filename) as f:
        data = f.readlines()
    sequence_id = None
    sequence = []


    for line in data:
        line = line.rstrip()
        if line.startswith(">"):
            if sequence_id is not None:
                fasta_dict[sequence_id] = "".join(sequence)
            sequence_id = line[1:]
            sequence = []
        else:
            sequence.append(line)

    #save last sequence if needed
    if sequence_id is not None:
        fasta_dict[sequence_id] = "".join(sequence)
    #bcause in file is one sequence return as string
    return "".join(fasta_dict.values())

def transcribe_dna(dna_string):
    rna_string = "".join("U" if nt =="T" else nt for nt in dna_string)

    return rna_string

def translate_rna(rna_string):
    """Function for translating a rna string

    Input:
        rna string: an rna string
    Output:
        str: A str representing the protein sequence, built by tannslating rna codons into aa using a codon table.
    """
    i = 0
    protein = ''
    while i < len(rna_string) - 2:
        triplet = rna_string[i:i+3]
        protein += code_rna.get(triplet, '?')
        i +=3
    return protein


def rev_complement(dna_string):
    """Function of finding the reverse complement of a dna string

    Input:
        dna string (str):  A string of DNA nucleotid

    Output:
        str: The  reverse complmenet of the input dna sequence.
    """

    rev_complem = ""
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    for nt in dna_string[::-1]:
        rev_complem += complement[nt]
    return rev_complem


def extract_orfs(protein):
    """Function for extracting orfs from a protein sequence

    Input:
        a protein sequence(str)
    Output:
        List: A list of orfs for a given protein, where each orf starts with M and ends at stop codon.
            Stop codon is not included in the Orfs
    """
    orfs = []

    for i in range(len(protein)):
        if protein[i] == 'M':  # Find the first 'M'
            current_orf = ''

            # Build the ORF starting from this 'M'
            for j in range(i, len(protein)):
                if protein[j] == "*":  # Stop codon found
                    orfs.append(current_orf)  # Append the full ORF
                    break
                current_orf += protein[j]

    return orfs

def whole_process(dna_string):
    """ Function for processing a DNA seq to extract all proteins fromm all possible reading frame

    Input:
        dna string
    Output:
        Set: aset of unique orf sequences produced from a DNA sequence in all reading frames
    """
    transcr_rna = transcribe_dna(dna_string)

    lis_proteins = []
    for i in range(3):
        orf = transcr_rna[i:]
        protein = translate_rna(orf)
        lis_proteins.append(protein)

    total_proteins =set()
    for protein in lis_proteins:
        lis_ofs = extract_orfs(protein)
        total_proteins.update(lis_ofs)

    return total_proteins

def write_to_file(lis_proteins):
    """Function for writing final protein sequences to a file
        Input:
            Lis_proteins: a list or seet of proteins:
        Output:
        None: Writes the ORF sequences to output_file_orfs.txt, one per line.
        """
    with open("output_file_orfs.txt", "w") as file:
        for protein in lis_proteins:
            file.write(f'{protein} \n')

def main():
    #parse sequence
    seq = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'

    #proteins for dna string
    set1 = whole_process(seq)
    #proteins from reve.complement
    set2 = whole_process(rev_complement(seq))

    #union of these to find the unique
    final_proteins  =set1.union(set2)

    #write to file
    write_to_file(final_proteins)

if __name__ == "__main__":
     main()








