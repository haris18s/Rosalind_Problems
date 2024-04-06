



def permutations_integ(array, indx_l, indx_r):
    """Function to calculate the  num of permutation for an array of integers. It uses the backatracking method.
    Input: array of integers
    Output (list of lists): the permutations for the ingegers of the array
    """

    permutations = []
    if indx_l == indx_r:
        permutations.append(list(array))
    else:
        for i in range(indx_l,indx_r):
            array[indx_l], array[i] = array[i], array[indx_l]
            permutations.extend(permutations_integ(array, indx_l + 1, indx_r))
            #Backtrack: swap the element to their original positions
            array[indx_l], array[i] = array[i], array[indx_l]
    return permutations

def write_file(lis_of_lis):
    """It writes a file where each new line is each element from a  list of lists.
    Input: list of lists
    Prints: each element (individual list) from list of lists,  into seperate line, seperated with spaces
    """
    with open("file.txt", "w") as file:
        #the number of permutation in the first line
        file.write(f'{len(lis_of_lis)}\n')

        for permu in lis_of_lis:
            file.write(" ". join(map(str,permu)) + '\n')


if __name__ == '__main__':

    #open the file of rosaling to read the positive integer
    with open("rosalind_perm.txt", "r") as file:
        num = int(file.readline())

    #make a list of integer from that given ingeger
    array = [i for i in range(1, num+1)]
    #calculate the num of perumataiton
    lis_num_permutations = permutations_integ(array,0,len(array))

    #write to a file
    write_file(lis_num_permutations)