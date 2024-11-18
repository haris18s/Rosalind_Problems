"""
Rosalind Problem: https://rosalind.info/problems/inod/

#total nodes (N) = Leaves (n) + Internal nodes (I) ----- (1)
N = n +I

#number of edges (m) = N -1  (2)
    $substitute from (1) m = n + I -1

#In unrooted binary tree each internal node has 3 connections  and each leaf (n) 1 connection = twice number of edges
    (Handshaking Lemma)
    3 * L + n = 2 * m ---- (3)

# substitute from  (2)
    $ 3 * L + n  = 2 * (n + I -1) =>
     3 * L + n = 2*N + 2*I -2
    I = n-2

    # we can subtitute to (1) to get total nodes in respect to leaves
        $ N = n + I = n + n-2 = 2*n - 2
"""

#Parse the number of Leaves
with open('rosalind_inod.txt') as f:
    leaves = int(f.readline().strip())

print(f"The number of internal nodes in unrooted binary tree is  {leaves - 2}")
total_nodes = 2 * leaves - 2
print(f"The number of total  nodes is {2* leaves - 2}")
print(f"The number of edges  is { total_nodes- 1}")