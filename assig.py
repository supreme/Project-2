#  Stephen Andrews
#  CS 2223
#  Project 2
import itertools
import sys
from random import randint

# Ends the program while printing a custom message
# before termination.
# @param msg The message to print before aborting.
def end_program(msg):
    print(msg + " Aborting...")
    sys.exit()

# Reads in a text file styled as a matrix and converts it
# to a 2-D array. Requires spaces inbetween each column 
# in the matrix and line breaks between rows.
# Required format as follows:
# 1 5 3 5
# 2 3 2 5
# 2 1 2 4
# @return The converted matrix as a 2-D array.
def open_file(path):
    matrix = []
    # The following three variables are merely to ensure the input file
    # contains a square matrix
    rows = 0
    columns = -1
    last_columns = -1
    with open(path, "r") as f:
        for line in f:
            arr = list(map(int, line.strip().split(' ')))
            last_columns = len(arr)
            if (last_columns != columns and columns != -1):
                end_program("Input is not a square matrix -> column mismatch.")
            columns = len(arr)
            matrix.append(arr)
            rows += 1
        if (rows != columns):
            end_program("Input is not a square matrix -> column to row ratio mismatch.")
    return matrix

# Performs an exhaustive search on a cost matrix
# in order to find the optimal solution.
# @param matrix The cost matrix to search.
# @return An array containing the messages the cryptographers should crack
#         where the index corresponds to the person.
def exhaustive(matrix):
    print("Running exhaustive...")
    print("---------------------------------")
    # Create a list of possibile indicies in the n x m matrix
    index_range = list(range(len(matrix)))
    # Create a permutation of array indicies with itertools Python package
    permutation = (list(itertools.permutations(index_range)))

    lowest = -1
    # The index in the array represents the cryptographer
    assignment = []
    temp = [] # Temporary tuple storage
    total_cost = 0
    # Loop through all permutations possible
    for i in range(len(permutation)):
        index_assignment = permutation[i]
        cost = 0
        # Loop through all index assignments
        for person in permutation[0]:
            cost += matrix[person][index_assignment[person]]
        if cost < lowest or lowest == -1:
            lowest = cost
            temp = index_assignment

    # Increment all indicies by 1 so its easier to read     
    for k in temp:
        assignment.append(k + 1)
    print(assignment)
    print("Exhaustive total cost: %d \n" % lowest)
    return assignment

# Performs an greedy search on a cost matrix
# in order to find the a greedy solution to the problem.
# @param matrix The cost matrix to search.
# @return An array containing the messages the cryptographers should crack
#         where the index corresponds to the person.
def greedy(matrix):
    print("Running greedy...")
    print("---------------------------------")
    # Let n be the size of the matrix since n == m
    n = len(matrix)
    # The index in the array represents the cryptographer
    assignment = [0] * n
    total_cost = 0

    for p_index in range(n):
        person = matrix[p_index]
        lowest = -1
        # Store lowest cost in assignment
        for c_index in range(n):
            cost = person[c_index]
            # Compare lowest costs and check if the message has already been assigned
            if (cost < lowest or lowest == -1) and not (c_index + 1 in assignment):
                lowest = cost
                assignment[p_index] = (c_index + 1) # +1 because array is zero based
        total_cost += lowest
        lowest = -1 # Reset
    print(assignment)
    print("Greedy total cost is: %d" % total_cost)
    return assignment

def show_menu():
    """Set up the menu to be printed to the console."""
    option_example = "example - Runs the sample cost matrix provided in the assignment. \n"
    option_matrix = "matrix - Generates an n x n cost matrix with up to k values. \n"
    option_file = "file - Runs a matrix defined in an external text file. \n"
    option_quit = "quit - Ends the program. \n"
    return input(option_example + option_matrix + option_file + option_quit + "\n")

if __name__ == '__main__':
    should_quit = False
    while not should_quit:
        user_input = show_menu()
        #  Handle all menu commands
        if user_input == "example":
            exhaustive(open_file("matrix.txt"))
            greedy(open_file("matrix.txt"))
        elif user_input == "matrix":
            matrix_n = int(input("Please enter a value for n: "))
            matrix_k = int(input("Please enter a value for k: \n"))
            print("\n Generating a random %d x %d matrix with up to %d values..." % (matrix_n, matrix_n, matrix_k))
            print("----------------------------------------------------------")
            matrix = [[0 for x in range(matrix_n)] for y in range(matrix_n)]
            for x in range(len(matrix)):
                for y in range(len(matrix)):
                    matrix[x][y] = randint(0, matrix_k)
            print(matrix)
            print("")
            exhaustive(matrix)
            greedy(matrix)
        elif user_input == "file":
            print("Enter a path relative to this file.")
            path = input("Path: ")
            exhaustive(open_file(path))
            greedy(open_file(path))
        elif user_input == "quit":
            print("Ending program...")
            break

