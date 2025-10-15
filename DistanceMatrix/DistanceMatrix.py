from Shortest_Superstring_Assembly.Shortest_Superstring import calculate_overlap


def parse_strings(filename):

    with open(filename) as f:
        data = f.readlines()

    strings = []
    seq = ""
    for line in data:
        line = line.rstrip()
        if line.startswith(">"):
            if seq:
                strings.append(seq)
                seq = ""
        else:
            seq += line
    if seq:
        strings.append(seq)
    return strings

def calculate_distance(s1 , s2):
    """Calculate the distance between 2 strings
    Input : 2 dna strings
    Output: p-distance (dp) on the given strings
    """
    diff = 0

    for i in range(len(s2)): # doesnt matter which string have same length
        if s1[i] != s2[i]:
            diff +=1
        else:
            continue
    ratio = diff/len(s1)
    return ratio


def created_matrix(strings):
    """Calculate a distance matrix
    Input: a list of strings
    Output: n x n distance matrix
    """
    n = len(strings)

    matrix = [[0] *n  for _ in range(n)]
    for i in range(len(strings)):
        for j in range(i, len(strings)): # this cut the work in half
            if i == j :
                matrix[i][j] = 0.000
            else:
                #dist i-j and j - i would be the same
                dist  =  round(calculate_distance(strings[i], strings[j]), 3)
                matrix[i][j] = dist
                matrix[j][i] = dist
    return matrix


def main():
    strings = parse_strings("rosalind_pdst.txt")
    output_matrix = created_matrix(strings)
    with open("output.txt" , "w") as output:
        for row in output_matrix:
            line = " ".join(f"{val:.3f}" for val in row)
            output.write(line + "\n")


if __name__ == "__main__":
    main()

