#!/usr/bin/python
from sys import argv
def compute_gc_content(dna):
    """This function takes a dna string
     Returns: Gc content of this dna sting"""
    gc = dna.count("c") + dna.count("g") + dna.count("G") +dna.count("C")
    gc_content =  gc/len(dna)
    return gc_content


def parse_file(filename):
    """Function to parse the fasta file
    Reutrns a dic with key:id and value:nt sequence"""
    data_dic = {}
    seq = ""
    identifier = ""
    with open(filename) as file:
        file_content = file.readlines()
        for line in file_content:
            line = line.strip()
            if line.startswith(">"):
                if seq:
                    data_dic[identifier] = seq
                identifier = line[1:]
                seq = ""
            else:
                seq +=line
        # for the last sequence
        data_dic[identifier] = seq
    return data_dic

def computer_maximum_gc(data_dic):
    """This function takes a  dictionary with  key:id, value: nt sequence/
    Returns the id with maximum gc gontent"""
    maximum_gc = 0
    id_max = ""
    for id,seq in data_dic.items():
        gc_content_current = compute_gc_content(seq) *100
        if gc_content_current > maximum_gc:
            maximum_gc = round(gc_content_current,6)
            id_max =id
    return id_max,maximum_gc


def main():
    'run with argv '
    data_dic = parse_file(argv[1])
    max_GC = computer_maximum_gc(data_dic)
    print(f'The id with maximum Gc content is {max_GC[0]} with {max_GC[1]}% GC content' )

if __name__ == "__main__":
    main()
