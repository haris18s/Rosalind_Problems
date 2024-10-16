import itertools
def parse_alphabet(filename):
    """
    Parses the input file to extract the alphabet and the integer 'n'.

    Args:
    - filename (str): The name of the input file containing the alphabet and 'n'.

    Returns:
    - alphabet (list): A list of characters representing the alphabet.
    - n (int): The length of the desired k-mers.
    """
    with open(filename) as f:
        data = f.readlines()

    alphabet = [char.strip() for char in data[0] if not char.isspace()]
    # Read the second line as an integer 'n' (k-mer length)
    n = int(data[1])

    return alphabet,n






def kmers_lexi(alphabet, n):
    """function to enumerate kmers lexicographically by a dynamic approach, each time add a letter to previous
        combination

    Input:
        (list) of an ordered alphabet

    Output:
        list of kmers combinations in lexicographical order"""

    #make a copy of original alphabet to append th ecombinaitons
    combinations = alphabet.copy()

    # Dynamically build k-mers by appending each character from the alphabet
    for i in range(n-1):
        combinations = [comb + char for comb in combinations for char in alphabet]

    return combinations

def main():
    alphabet , n = parse_alphabet("rosalind_lexf.txt")

    combo_kmers_m1 = kmers_lexi(alphabet,n)
    with open("output_kmers_lex.txt", "w") as f:
        for line in combo_kmers_m1:
            f.write(f'{line} \n' )

    #a second method for generating keywords using itertools.product
    combo_kmers = [''.join(i) for i in itertools.product(alphabet, repeat=4)]


if __name__ == '__main__':
    main()