#!/usr/bin/env python3


"""
Author: Haris Spyridis
Rosalind problem: Rabbits and recurrence relations

This script calculates the total number of rabbit pairs after a given number
of months, following a recurrence relation where each reproductive pair produces
a fixed number of offspring pairs per month.
"""
from sys import argv


def parse_nums(file):
    """
    Parse two integers from the input file: number of months (n) and
    number of rabbit pairs produced per reproductive pair (k).

    Input:
        file (str): Path to the input file.

    Output:
        tuple (int, int): Number of months (n) and number of rabbit pairs (k).
    """
    with open(file, "r") as f:
        #split into two nums
        data = f.readline().split()

    months, pairs_per_month = int(data[0]), int(data[1])
    return months, pairs_per_month

def rabbit_pairs(n,k):
    """
    Calculate the number of rabbit pairs after 'n' months, where each
    reproductive pair produces 'k' pairs of offspring every month.
    THe problem followss a recuurance relation similar to fibonnacci series

    Input:
        n (int): Number of months.
        k (int): Number of rabbit pairs produced by each pair every month.

    Output:
        int: Total number of rabbit pairs after 'n' months.
    """
    #Initialize 1 for the first 2 months (the dont reproduce yet)
    total_pairs = [1,1]

    for i in range(2,n):
        #i-1 the previous month (not reproducible yet) + the pairs produced by the pairs from previous 2 months
        pairs_per_month = total_pairs[i-1] + k * total_pairs[i-2]
        total_pairs.append(pairs_per_month)

    #return the pairs in the last month
    return  total_pairs[-1]


def main():
    #parse the numbers
    months, pairs_per_month = parse_nums(argv[1])

    total_pairs = rabbit_pairs(months,pairs_per_month)
    print(total_pairs)



if __name__ =="__main__":
    main()