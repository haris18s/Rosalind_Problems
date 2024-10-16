from subprocess import run, PIPE
from sys import argv
#[N]{1}[^P](S|T){1}[^P] reular epression for glycosylation motif.


def parse_proteins(input_file):
    """This function parses the protein identifiers from a file
    Input: a txt file with the protein identifies
    Returns: a list with the ids that going to be used to download their sequence
    """
    with open(input_file, 'r') as file:
        file_data = file.readlines()
    dic_proteins = {}
    for line in file_data:
        line = line.strip()
        dic_proteins[line] = line[:6]

    return dic_proteins


def download_data(dic_proteins):
    """Downloads protein sequences from UniProtKB based on protein identifiers.
    Input: list_proteins (list): A list mapping protein identifiers to their first six characters.

    "Returns: A dictionary mapping protein identifiers to their corresponding sequences.
    """
    dic_proteins_fasta ={}
    for name,id in dic_proteins.items():
        output = id
        url = f"https://rest.uniprot.org/uniprotkb/{id}.fasta"
        file = run(['wget', '-O', output, url], check=True, stdout=PIPE, stderr=PIPE)
        sequence = parse_individual_fasta(output)
        dic_proteins_fasta[name] = sequence
    return dic_proteins_fasta

def parse_individual_fasta(file):
    """Parses a individual FASTA file to extract the sequence.
        Input: file (str): The path to the FASTA file.


        Returns :   str: The sequence extracted from the FASTA file.
    """
    with open(file, 'r') as file:
        data = file.readlines()
    seq = ""
    identifier = ""
    for line in data:
        line = line.strip()
        if line.startswith(">"):
            identifier = line[:11]
        else:
            seq +=line

    return  seq



def search_glyc_motif(sequence):
    """    Searches for the N-glycosylation motif in a protein sequence.
        Input: sequence (str): The protein sequence to search.
        output:  A space-separated string containing the positions of N-glycosylation motifs in the sequence.
    """
    locations_of_each_seq =[]
    for aa in range(len(sequence) -3):
        if sequence[aa] == "N":
            ##without parentesis or has higher value than or
            if sequence[aa+1] != "P"  and (sequence[aa + 2] == "S" or sequence[aa + 2] == "T" ) \
                 and sequence[aa+3] != "P":
                locations_of_each_seq.append(aa+1)
    return " ".join(str(location) for location in locations_of_each_seq)

def write_to_file(dic_with_sequences):

    """Function to write into file the glygocyation motifs of each seq
    Input: takes a dic, with key id and value:sequence:

    return a file with each row an id (and next row the positions of glycos motifs for respective seq)
    """
    with open("locations8.txt", "w") as file:
        for ident, sequence in dic_with_sequences.items():
            locations_per_protein = search_glyc_motif(sequence)
            if locations_per_protein == "":
                pass
            else:
                file.write(("{}\n{}\n").format(ident, locations_per_protein))

def main():
    data = parse_proteins(argv[1])
    dic_with_sequences = download_data(data)
    print(dic_with_sequences)
    write_to_file(dic_with_sequences)



if __name__ == "__main__":
    main()


 # subprobess.Popen, lets you run in paallel python before it returns the files from shell
    #inspect(file) #shows the result in nice format
