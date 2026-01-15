
def parse_string(filename):
    """Parse a single RNA sequence from a FASTA-like file.

    The file format is:
        >header line
        RNA sequence split across one or more subsequent lines

    Input:
        filename (str): path to a text file

    Output:
        str: RNA sequence with no whitespace or newlines
    """
    with open(filename) as f:
        next(f)
        data = f.readlines()
    rna_str =  "".join(line.rstrip() for line in data)
    return rna_str



def create_dp_table(n):
    """    Create and initialize the DP table for Motzkin recursion.
    dp[i][j] =  number of non crossing RNA secondary structures for substring rna[i..j]
    Input
        -(nt)the lengh of the string

    Output:
        list[list[int]]: DP table of size (n+1) x (n+1)
    """
    #dp[i][j] --> means number of non crossign structurs of substring rna[i..j]

    dp = [[0]* (n+1) for _ in range(n+1)]
    #dp[i][j] = number of complete noncrossing structures of substring i...j
    for i in range(n):
        #both are empty matchings
        dp[i][i-1] =1 #empty substring (i>j) = 1, exactly 1  structures
        dp[i][i] = 1 # single Nt, e.g  "A" has exactly 1 structure, you need 2 bp to form an edge
    #empty suffix after the last character
    dp[n][n-1] = 1

    return dp
def is_pair(nt1,nt2):
    if {nt1, nt2} == {"C", "G"}:
        return True
    if {nt1, nt2} == {"A", "U"}:
        return True
    return False


def Motzkin_recursion(rna_string):
    """Function to calculate Total number of non crossing matchings of bp edges.
    Bases may be unpaired.
    Allowed pairs: A-U, C-G.

     Input: a(str) rna string.

     Output:
        (int): total number of non corssing matching of bp edges in the bonding graph modulo 10**6
     """
    
    n = len(rna_string)
    dp = create_dp_table(n)
    MOD = 10**6

    #odd and even lengths are allowed, in comparison to Catalan only even - perfect matchings
    for length in range(2, n+1):
        for i in range(0, n-length+1):
            j = i + length -1
            dp[i][j] = 0
            #Option 1: i is unpaired --> s[i+1][j]
            total = dp[i+1][j] #Case 1: the ith base can be unpaired, for length=4, i=0, pos 0 not paired with others,structures between 1..3

            #fix a base m
            for m in range(i+1, j+1):
                if is_pair(rna_string[i], rna_string[m]):
                    #Option 2: i pairs with m: and bases match, so indices and outside as catalan number
                   total += dp[i+1][m-1] * dp[m+1][j]
            dp[i][j] = total

    print(dp[0][n-1]%MOD)

def main():

    rna_str = parse_string('rosalind_motz.txt')
    Motzkin_recursion(rna_str)

if __name__ == "__main__":
    main()



