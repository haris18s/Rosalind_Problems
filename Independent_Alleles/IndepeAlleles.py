"""2 events are independent if Pr(A and B) is equal to Pr(A)×Pr(B).,

    Pr(X+Y is odd) = Pr(X is even and Y is odd)+Pr(X is odd and Y is even),
    using independence :  [Pr(X is even)×Pr(Y is odd)]+[Pr(X is odd)×Pr(Y is even)],

    Problem fits Binomial model:
        - Fixeed number of trials n --> in generation k, there are exactly 2^k children (no mater)
        - Each trial has only 2 outcomes (success or failure)--> 2 outcomes each child is either AaBb or not
        - Each trial has same prob of success p--> each chilce is produced by the same cross : 1/4 to have the genotype
        = The trials are independent of each other -> each child's genotype is independent

        X ~ Binomial(n = 2**k , p = 1/4)

    n --> number of inditivation in the kth gneration
    N--> minimum number of indivdausl you want in that gneration
   Looking for Pr(X>=N) = (n choose k) (1/4)  ** i (1-1/4) ** (n-1), where X is the number of inidvidausl carry AaBb
   in gneration k


"""
p = 1/4
q = 1-p # prob of failure
k = 7
N = 32
n = 2**k # number of indiivduals in k generation, if 2 indiivusals per generation

import math
result = sum(
    (math.factorial(n)/(math.factorial(i) * math.factorial(n-i))) *
    (p**i) * (q**(n-i))
    for i in range(N, n+1))



print(round(result,3))