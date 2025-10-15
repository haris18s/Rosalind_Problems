"""Problem: Introduction to Alternative Splicing
https://rosalind.info/problems/aspc/
"""
import math


def SumCombinaitons(n,m):
    """Calculates the Sum of combinations for all k, where n<=k<=m

    Input:2 positive integers
        n: total number of items
        m: minimum of selections

    Return: sum of combinations
     """


    final_sum= 0
    for i in range(m, n + 1):
        final_sum += math.factorial(n) // (math.factorial(i) * math.factorial(n - i))
    print(final_sum)
    return final_sum % 1000000
if __name__ == "__main__":
    SumCombinaitons(6,3)