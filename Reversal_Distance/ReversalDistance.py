import math

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
B =  [3, 1, 5, 2, 7, 4, 9, 6, 10, 8]


def parse_pairs(filename):
    """Parse pairs of permutations from a txt file
    Input: a file name, with pairs of permutations

    Output: a list of lists of  pairs
    """
    new_pair = []
    all_pairs = []
    with open(filename) as f:
        data =  f.readlines()
    for line in data:
        line = line.rstrip()
        if not line: #blank line
            if new_pair: # if we have a pair
                all_pairs.append(new_pair)
                new_pair = []
        else:
            nums = list(map(int, line.split()))
            new_pair.append(nums)
    if new_pair is not None:
        all_pairs.append(new_pair)

    return all_pairs



def inverse_perm(B):
    """Give the inverse permutation of an array, where each  elemnt (1-n) located in B
    Input: a (list) of nums
    Outputs: The ivnerse permutation of the array

    """
    max_range = max(B)
    inverse_B = []
    for i in range(1,max_range+1):
        inverse_B.append(B.index(i)+1) #bcasue python use 0 index
    return inverse_B

def compose_perms(A, inverse_array):
    """Apply rught hand permutation, and then left one
    Finds where A sends i, and where inverse B⁻¹ sends that.
    So finds the pos of element in A, in B.
    A = [4, 1, 3, 2]
    B⁻¹ = [4, 3, 1, 2]
    Output :B−1∘A = [2,4,1,3]
    """
    pi = []
    #loop over elements
    for num in A:
        #find where each element belongs in final order
        pi.append(inverse_array[num-1]) #bcause inversing array is -based

    return pi

def find_reversals(array):
    """Function to create all possible permutations with one reversal
    If the function is applied again, the permutations are with 2 reversals
    """

    i= 0
    j= 1
    reversals = []
    while i < j and j < len(array):
        seg_to_reversed = array[i:j+1]
        reversals.append(array[:i] + seg_to_reversed[::-1] + array[j+1:])
        j +=1
        if j == len(array):
            i +=1
            j = i + 1
    return reversals

def find_breakpoints(perm):
    """function to find wheather 2 elements are conscutive, if not it is breakpoint
        Count the number of breakpoints, so how many reversals we need until we sort it
        Then finds te permutaitons with lowest breakpoints.
    """
    array = [0] + perm + [len(perm) + 1] #add the boundaris for 1,2,3,4, perm, add 0 and 5 in edges
    count = 0
    for i in range(len(array) - 1):
        if abs(array[i+1] - array[i]) !=1:
            count +=1
    return count
from heapq import heappush, heappop
def reversal_distance_BFS(A,B):

    """Run A* (based on bfs) algorithm in the pi_array, with heuristic (which perm to expand nest based on breakpoints):
        Each permutation gets score: f(p)  = g(p) + h(p)
                g = reversals so far.
                h = estimated reversals still needed
                fewer breakpoints, closer to sorted --> smaller h(p)

                A node is one permutations, and an edge a reversal between 2 nodes
    """
    #get the inverse array of B
    inverse_array = inverse_perm(B)
    pi = compose_perms(A, inverse_array)
    #find breakpoints in pi
    b0 = find_breakpoints(pi)
    #lower bound on how man  reversals we need, each reversal can fix at most 2 breakpoints
    h0 = math.ceil(b0/2)

    #Initialize a Queue
    queue = []
    #start the A* with g=0 (0 reversals , f = h0 total estimated cost
    heappush(queue, (h0,0,pi))
    #create visited set, ensures that dont exapnd same permutation twice
    visited = set() #
    #add the fist perm in visited
    visited.add(tuple(pi))
    #instead of moving from A--> B, we move B⁻¹A --> B⁻¹ B = I(identity), so move pi --> identity
    goal = list(range(1, len(A) + 1)) #sorted identiy permutation
    #while q is not empty
    while queue:
        #p = perm that we will expand next
        """Very important step: remove elment with lowest f and then continue with that"""
        f, depth, p = heappop(queue) #remove the element with lowest f value(most promising perm)!!!Most
        if p == goal:
            return depth

        #generate all perms rearchable from py one reversal, if already one, then 1 +1 =2 reversals
        perms = find_reversals(p)
        for perm in perms:
            #avoid revisting states
            if tuple(perm) not in visited:
                #instead of explorims perms in the ordered htey discovered, explore base from lwer to the closetst ot goal
                g = depth + 1
                h = math.ceil(find_breakpoints(perm)/2)
                #how far we have gone (g), and how far we think is left(h
                f = g + h
                #mark as visited
                visited.add(tuple(perm))
                #add state back to priority queue
                heappush(queue, (f,g, perm))

def main():
    pairs = parse_pairs("rosalind_rear.txt")

    import time
    tic = time.time()
    output = []
    for pair in pairs:
        A, B = pair[0], pair[1]
        revrsal_dist_per_pair = reversal_distance_BFS(A,B)
        output.append(revrsal_dist_per_pair)


    print(" ".join(map(str,output)))# first convert to str, join expect str
    toc = time.time()
    print("Duration of algorithm:", toc-tic)


if __name__ == "__main__":
    main()