#!/usr/bin/ python3


def parse_numbers(filename):
    """
    Parse two integers from the first line of a file.

    Input:
        filename (str): The name of the file to read from.

    Output:
        tuple (int, int): The first two integers from the file.
    """
    with open(filename) as f:
        numbers =  f.readline().split()

    n, m = int(numbers[0]), int(numbers[1])

    return n,m


def fibonacci_mortal(n, m):
    """
    Calculate the total number of rabbit pairs after n months with a lifespan of m months.

    This uses a dynamic programming approach where a 2D matrix is constructed
    to represent rabbit population by month and age.

    Input:
        n (int): The number of months.
        m (int): The lifespan of the rabbits in months.

    Output:
        int: The total number of rabbit pairs at the nth month.
    """
    # Create a matrix (list of lists) to store the population,
    # where rows represent months and columns represent ages (from 0 to m-1).
    matrix_pop = [ [0]*m for i in range(n+1)]

    #Initialize 1  newbor pair for 1st  month
    matrix_pop[1][0] = 1

    #loop through each month from 2 to n
    for month in range(2, n+1):
        #newbors in the current month come from adults from the previous month (from ages 1 to m-1)
        matrix_pop[month][0] = sum(matrix_pop[month-1][1:])

        #rabbits gets older 1 month so move them forward
        for age in range(1, m):
            #each cell has value of previous row and previous col, all will be 1 month older
            matrix_pop[month][age] = matrix_pop[month-1][age-1]

    #the total pairs in nth month is the sum of all ages in nth month
    total_pairs = sum(matrix_pop[n])


    return total_pairs


def main():
    m, n = parse_numbers('rosalind_fibd.txt')

    print(fibonacci_mortal(m,n))

if __name__ == "__main__":
    main()