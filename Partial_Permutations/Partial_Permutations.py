#!/usr/bin/env python3

def parse_nums(filename):
    """
    Parses the input file to extract two integers, n and k.
    100≥n>0 and 10≥k>0
    Args:
    - filename (str): The name of the input file containing two integers.

    Returns:
    - n (int): The first integer.
    - k (int): The second integer.
    """
    with open(filename) as f:
        nums = f.readline().split()
        n = int(nums[0])
        k = int(nums[1])

    return n,k


def fact_int(n):
    """
    Computes the factorial of a non-negative integer n recursively.

    Args:
    - n (int): A non-negative integer.

    Returns:
    - int: The factorial of n (n!).
    """

    return 1 if(n==1 or n ==0) else n*fact_int(n-1)

def partial_perm(n,k):
    """
    Calculates the number of partial permutations of n taken k at a time,
    and returns the result modulo 1,000,000.

    Args:
    - n (int): The total number of items.
    - k (int): The number of items to choose.

    Returns:
    - int: The number of partial permutations modulo 1,000,000.
    """
    partial_perm = fact_int(n) / fact_int(n-k)

    modulo_perm = int(partial_perm) % 1000000

    return modulo_perm

def main():

    #parse nums
    n, k = parse_nums('rosalind_pper.txt')

    #find partial permutations
    num_part_perm = partial_perm(n,k)
    num_part_perm = partial_perm(4,3 )
    print(num_part_perm)

if __name__ == '__main__':
    main()