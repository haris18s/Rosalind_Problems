def parse_reads(filename):
    """
    PArse a FASTa file and extracts DNA reads.
    Reads are expected to be in FASTa format, where each red starts wiht a line beginning with '>' followed by 1 or more
    lines of nt sequences

    Input:
        filename : path to the FASTa file

    Returns:
        a list of str: a list of DNA reads (as strings).
    """

    with open(filename) as f:
        data = f.readlines()
    read = ""
    reads = []
    for line in data:
        line = line.rstrip()
        if line.startswith(">"):
            if read:
                reads.append(read)
                read = ""
        else:
            read +=line
    if read:
        reads.append(read)
    return reads

def reverse_comple(string):
    """find the reverse completemenet of a string
    Input: DNA string
    output: the reverse complement of the input
    """
    rev_dic = {"A": "T", "G":"C", "C": "G", "T":"A"}
    rev = ""
    for nt in string:
        rev += rev_dic[nt]
    rev_comple = rev[::-1]
    return rev_comple

def CountReads(reads):
    """Counts the occruances of DNA reads, treating each reads and rev.complement as a single canonical form
    This ensures that a read and its reverse complement are considered equivalant when determining how many times
    the read appears in the dataset.

    Input:
        -reads list of str: a list of DNA reads
    Return:
        -a dic mapping eahc canonical read to its count
    """
    count_reads = {}
    for read in reads:
        rev_comple = reverse_comple(read)
        #canonical form of the read --> to treat them as one unique idenity
        key = min(read, rev_comple)

        if key in count_reads :
            count_reads[key] +=1
        else:
            count_reads[key] = 1
    return count_reads

def ClassifyReads(reads):
    """Classifies DNA reads as correct or incorrect
    A read sis ccorrect if (or its reverse comple) appers at least twice in the dataset.
    All other (apperaing once, and not as rev comllement) are considered incorrects

    Input:
        reads (list of str): a list of dna redas

    Output:
        tuple:  a set of correct reads and list of incorrect reads
    """
    correct_reads = set()
    count_reads =  CountReads(reads)
    incorrect_reads = []

    for read in reads:
        canonical = min(read, reverse_comple(read))
        if count_reads[canonical] >=2:
            correct_reads.add(read)
            correct_reads.add(reverse_comple(read))
        elif count_reads[canonical] ==1 :
            incorrect_reads.append(read)

    return correct_reads , incorrect_reads

def HammDist(read1, read2):
    """Finds the hamm distance between 2 reads

    Returns:
        - a int, that gives the distance between 2 reads
    """
    length = min(len(read1), len(read2))
    hamm_dist = 0

    for idx in range(length):
        nt1, nt2 = read1[idx], read2[idx]
        if nt1 != nt2:
            hamm_dist +=1
        if hamm_dist >1:
            break

    return hamm_dist

def FindCorrections(corr_reads, incor_reads):
    """For each incoreact read finds the correact rad, that differs exactly one nt (hamm_dist=1

    Returns:
            - a list of correction pairs in the form
    """
    final_corrections = []
    for incor_read in incor_reads:
        for corr_read in corr_reads:
            hamm_dist_reads = HammDist(incor_read, corr_read)

            if hamm_dist_reads ==1:
                final_corrections.append([incor_read,corr_read])

    return final_corrections

def main():
    reads = parse_reads("rosalind_corr.txt")

    correct_reads, incorect_reads = ClassifyReads(reads)
    final_correct = FindCorrections(correct_reads, incorect_reads)

    with open("output.txt", "w") as f:

        for pair in final_correct:
            line = "->".join([seq for seq in pair])
            f.write(line + "\n")


if __name__ == "__main__":
    main()