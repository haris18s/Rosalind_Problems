import sys


print("hello")



def parse_rosalind_file(file_name):
    """It parses the rosalind file with the dna string
    Input:rosalind file with the DNa sting as input
    """
    dna_string = ''
    with open(file_name, "r") as file:
        fasta_file = file.readlines()
        for line in fasta_file:
            if not line.startswith(">"):
                dna_string +=line.strip()
    return dna_string

def rever_comple(string):
    """It finds and returns the reverse complement of a DNA string
    Input DNA string
    Return: the reverse complement of the DNA string
    """
    complement_dict = {'A':'T', "C":"G", "G":'C', "T":"A"}

    reverse_comple = "".join(complement_dict[base] for base in string[::-1])

    return reverse_comple

def find_palindromes(dna_string):
    """It finds the palindomes of the dna string, with 4<=length<=12
    Input:dna string
    Output: (list of lists) with  the position of each palindrome together with the length of the palindrom
    """

    list_palindromes = []
    for i in range(len(dna_string)):
        for j in range(i, len(dna_string) + 1):
            substring = dna_string[i:j]
            reverse_compl = rever_comple(substring)
            if reverse_compl == substring and 4 <= len(substring) <= 12:
                list_palindromes.append([i+1, len(substring)])


    return list_palindromes


def write_to_file(lis_of_palidromes):
    """Writes to file the outoupt.
    Input takes a list of list, with first element the position and 2nd elemnt length of the palindrome"""
    with open('palindromes_rosalind.txt', 'w') as file:
        for item in lis_of_palidromes:
            palidrome = ' '.join(map(str,item))
            file.write(palidrome + '\n')


complements = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
def rev_comp(string):
    newstring = ''
    for base in string:
        newstring += complements.get(base)
    newstring = newstring[::-1]
    return newstring



if __name__ == '__main__':
    dna_string = parse_rosalind_file('rosalind_revp.txt')
    palindromes_lis = find_palindromes(dna_string)
    output_palindroms = write_to_file(palindromes_lis)
    query_sequence =dna_string

