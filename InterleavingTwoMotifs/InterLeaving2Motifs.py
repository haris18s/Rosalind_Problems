


def parse_strings(filename):
    with open(filename) as f:
        data = f.readlines()
    s , t = data[0], data[1]

    return s, t


def construct_DP(s,t):
    """Fucntinon to constuct dp matrix, that has the length of the shortest common superseuqnece(SCS)

    Input: 2 dna strings, s and t
    Output: a dp matrix, with the last cell, is the length of the SCS.
    """

    m, n = len(s), len(t)
    dp = [[0] * (n+1) for _ in range(m+1)]

    #initialize the length of first rows and cols

    for i in range(m+1):
        dp[i][0] = i

    for j in range(n+1):
        dp[0][j] = j

    #fill dp table
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
    return dp

def find_SCS(dp):
    """From the dp matrix, reverse back to obtain the actual SCS
    Input: a dp matrix that has the length of the SCS in the last cell
    Output: (str) the actual SCS.
    """

    m, n = len(s), len(t)
    print(m)
    i, j = m, n
    superseq = ""

    while i > 0 and j > 0:
        if s[i-1] == t[j-1]:
            superseq += s[i-1]
            i -= 1
            j -= 1
        elif dp[i-1][j] < dp[i][j-1]:
            superseq += s[i-1]
            i -= 1
        else:
            superseq += t[j-1]
            j -= 1

    # add remaining characters
    while i > 0:
        superseq += s[i-1]
        i -= 1
    while j > 0:
        superseq += t[j-1]
        j -= 1
    return superseq[::-1]

def main():
    s,t = parse_strings("rosalind_scsp.txt")
    #Get the matrix
    dp = construct_DP(s,t)

    superseq = find_SCS(dp)

    print("Shortest Common Supersequence:", superseq)
if __name__ == "__main__":
    main()

