"""Problem : Expected Number of Restriction Sites
caclulate the number of times that a string s will appear as subtring of random DNA string t of length n,
where t is formed with GC content in Array A
"""

def parse_file(filename):
    """Parse the Rosalind file for this exercise where in
        n -length of the random dna string t- in line1
        DNA s =- the string (DNA) that will be appear as substring in t - line 2
        A - the GC content under the random  string t is generated
    """

    with open(filename) as f:
        data = f.readlines()

    n = int(data[0].strip())
    s = data[1].strip()
    A = data[2].strip().split()
    print(A)
    return n, s, A

def calculateProb(s, GC_content):
    """Function to Calculate the proabability of a string (s) matches a random string (t) under specific GC content
    Input:
        -(str) a Dna string
        -(float) GC content that under a random string is generated
    output:
        -(float)  the probability that string s matches a random string
    """
    #num of GCs and ATs in the stirng
    GC_num = s.count("C") + s.count("G")
    AT_num = s.count("A") + s.count("T")


    #in each position in random string will be either GorC or AorT
    G_freq = GC_content/2 #same as C freq
    A_freq = (1-GC_content) / 2 #same as T_freq

    #the joint probability of each position -- > each postion is random variable --> find joint event (all position occur simultaneously
    prob_of_match = G_freq**GC_num * A_freq**AT_num #multinomial probability

    return prob_of_match

def calculate_Expectted(s,n, prob):

    """Calcluate the number of expected times that a string s will be found as substring in random string t

    Input:
        - (str) s: a Dna string
        - (float) GC: the GC content that  random string t generated
        -n (int) : the length of the random string
        -prob: the probability that
    output:
        (float): the expected num of times that s will be found as substring in random string t,
            --> it is the Linearity of expectation with indicator value being the prob of matching
    """

    #the string s (m=len(s)) can match t (n=len(t)) in num_of_positions = n - m +1, eg. if s=AG, and n=10, then cna match in 9 startingpositions
    num_of_starting_poa = n - len(s) + 1
    #expected num of occurances of s in t E(#occurances of s in t) = num_of_positions * probability that strings match
    expectedOccurances = num_of_starting_poa * prob #

    return round(expectedOccurances,3)
def main():
     n, s, A = parse_file("rosalind_eval.txt")
     B = []
     for gc_content in A:
         prob = calculateProb(s, float(gc_content))
         B.append(calculate_Expectted(s, n, prob=prob))
     print(" ".join(map(str, B))) # join can only used for strings, so map to strings





if __name__ == "__main__":
    main()