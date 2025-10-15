





def parse_string(filename):

    """Parse rosalind text file, with fasta as format.
    Input: fasta file name as input, with DNA seqeunce.

    Output: a str, of the DNA string which will be used to find the kmer composition
    """

    with open(filename) as f:
        data = f.readlines()
    dna_str = ""
    for line in data:
        line = line.strip()
        if not line.startswith(">"):
            dna_str +=line
    return dna_str


def create_kmers_iter(k):
    """Ceeate all possible 4-mers for the nucleotides
        4 ** 4
    """
    nts = ["A", "C", "G", "T"]
    kmers_iter = [""]

    #loop thrugh length of k
    for i in range(k):
        new_kmer_lis = []
        #for each kmer in the list
        for kmer in kmers_iter:
            #add a nt in the existing one string in the kmers.
            for nt in nts:
                new_kmer_lis.append(kmer+nt)
        kmers_iter = new_kmer_lis
    return kmers_iter

def count_kmers_str(dna_str, kmers_dic, k=4):
    """For each 4-mer in the dna string count the existance in all possible kmers

    input:
        -dna string
        -kmers dic (dic): all possible 4mers for the nts, and 0 count
        -k=4
    output:
        count matrix for 4-mers (lexicographically)  in the dna string, and their count
    """

    for i in range(len(dna_str) -k +1):
        kmer = dna_str[i:i+k]
        if kmer in kmers_dic:
            kmers_dic[kmer] +=1
    return kmers_dic


def second_method(dna_str, k =4):
    """
    Create 4mers with te fucntion product from itertools

    for each possible kmer in dna string, check if it exists in the dic of all kmers
    """
    from itertools import product
    k = 4
    # generate all kmers in general
    all_kmers = {"".join(p): 0 for p in product(("ACGT"), repeat=4)}


    for i in range(len(dna_str) - k + 1):
        kmer = dna_str[i:i + k]
        if kmer in all_kmers:
            all_kmers[kmer] += 1

    for kmer in sorted(all_kmers.keys()):
        count_per_kmer = all_kmers[kmer] #write if if you use this method



def main():
    all_kmers_iter = create_kmers_iter(k=4)
    dna_str = parse_string("rosalind_kmer.txt")
    #count dic  for all possible kmers from the nts.
    kmers_dic = {kmer:0 for kmer in all_kmers_iter}

    count_dic = count_kmers_str(dna_str, kmers_dic, k=4)
    with open("output_count.txt", "w") as f:
        for kmer in count_dic.keys():
            f.write(str(count_dic[kmer]) + " ")



if __name__ == "__main__":
    main()