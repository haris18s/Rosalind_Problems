""""Problem: https://rosalind.info/problems/iev/"""


def parse_nums(filename):
    """
    Parses the input file to extract the number of couples of each genotype pair.

    Args:
    - filename (str): Name of the input file containing integers corresponding to the number of couples.

    Returns:
    - num_couples (list): A list of integers representing the number of couples with specific genotype pairings.
    """

    with open(filename) as f:
        num_couples = list((map(int, f.readline().split() )))
    return num_couples



def calculate_offspring(num_couples, probabilties):
    """Function to calculate the number of expected offpring with dominant pheotpy
        The function assumes each couple produces two offspring. The dominant phenotype
    probabilities for the following genotype pairings are given:
    - AA-AA: 100% dominant
    - AA-Aa: 100% dominant
    - AA-aa: 100% dominant
    - Aa-Aa: 75% dominant
    - Aa-aa: 50% dominant
    - aa-aa: 0% dominant
    Input:
        (list) of positive integers that correspond to the number of couples in a population
        (list) of probabilities for the number of couples having following genotypes
                AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa
    Output:
        (float):The expected number of offspring with the dominant phenotype.

    """
    #porbability after pairing to have dominant phenotype (for respective genotype) and by 2( each couple 2 offspring)
    expected_offspring = 2* sum(couples * prob for couples, prob in zip(num_couples,probabilities))

    return expected_offspring

def main():
    # Probabilities for each genotype pair producing an offspring with the dominant phenotype
    probabilities = [1, 1, 1, 3 / 4, 2 / 4, 0]

    #parse file fo number of couples
    nums_couples = parse_nums("rosalind_iev.txt")

    #calculate expected offspring
    expected_offspring = calculate_offspring(nums_couples, probabilities)
    print(expected_offspring)


if __name__ == "__main__":
    main()