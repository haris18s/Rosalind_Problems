"""Rosalind Problem: https://rosalind.info/problems/pmch/"""

"""Perfect matching
    -no base (node) left unpaired
    - no base (node) is paired more than once
    
In RNA structurre, A can only pair with U, and C only G.
    Therefore, if there (n) A's, it can pair with U, n! (Pick A to form a pair with u, there are n choices.
     Next pair: there are n-1 choices (n-1 A's and n-1 U's remain). Repeat until all bases paired.  """

with open("rosalind_pmch.txt") as f:
    next(f)
    lines  = f.readlines()
    str = "".join(line.rstrip() for line in lines)
    print(str)

import math
try:
    A = str.count("A")
    C = str.count("C")
    U = str.count("U")
    G = str.count("G")
    
    if A != U or G != C:
        raise ValueError("There is mismatch in the count of complementary bases")
    noPerfectMatch = math.factorial(A) * math.factorial(C)
    print(noPerfectMatch)
except ValueError as e:
    print(e)
