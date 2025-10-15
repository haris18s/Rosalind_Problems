def parse_strings(filename):
    with open(filename) as f:
        data = f.readlines()

    seqs = []
    seq = ""
    for line in data:
        line = line.rstrip()
        if line.startswith(">"):
            if seq:
                seqs.append(seq)
            seq = ""

        else:
            seq +=line
    seqs.append(seq)

    return seqs

def fill_dp(str1, str2):
    """DP programming approach to fill the matrix for subsequences
    Input: 2 dna strings
    Returns: matrix when dp[i][j] is the num of the longest subsequences
    """
    n = len(str1)
    m = len(str2)
    dp = [ [0] * (m+1) for _ in range(n+1)]
    for i in range(1, n +1):
        for j in range(1, m + 1):
            #if the characters match then it is the diagonal
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j]) #take max from left or top

    return dp

def reverse_dp(dp_matrix, str1, str2):
    """Trace back through the DP matrix to find the LCS strings:
    Input: the dp matrix from dp approach, and 2 dna strings

    Output: the longest subsequence between 2 dna strinfs
    """

    longest_seq = ""
    i, j = len(str1), len(str2)
    #go backwards from the last row, col to top
    while i > 0 and j >0:
        #if characters match go diagonally
        if str1[i-1] == str2[j-1]:
            longest_seq +=str1[i-1]
            i -=1
            j -=1
        elif dp_matrix[i-1][j] >= dp_matrix[i][j-1]: #if top > left value move to top cell
            i -=1
        else: #move to left
            j-=1

    return longest_seq[::-1]


def main():

    seqs = parse_strings("rosalind_lcsq.txt")
    str1 , str2 = seqs[0], seqs[1]

    str1 = "AACCTTGG"
    str2 = "ACACTGTGA"
    matrix_dp  = fill_dp(str1, str2)

    #find the longest subsequece
    longest_subsequence = reverse_dp(matrix_dp, str1, str2)


    print(longest_subsequence)


if __name__ ==  "__main__":
    main()