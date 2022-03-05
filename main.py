# CPSC 450 - Bioinformatics
# Isayha Raposo - 230133508
# Assignment 4 - Greedy Sorting with Reversals

from sys import argv, exit
from os import path

# Returns the permutation found within the user-specified data file
def process_data_file(data_file_name):
    data_file = open(data_file_name, 'r')
    permutation = [int(x) for x in data_file.readline().strip().replace('+', '').split(' ')]
    return permutation

# Prints string to the console in addition to writing string to output_file
def print_and_write(output_file, string):
    print(string)
    output_file.write(string + '\n')

# Performs a reversal on the provided permutation given a start index (inclusive) and an end index (inclusive)
# as per in-lecture algorithm discussion, and returns the result
def get_reversal(permutation, start_index, end_index):
    permutation = [0] + permutation

    beginning = permutation[1:start_index + 1]
    middle = permutation[end_index + 1:start_index:-1]
    end = permutation[end_index + 2:]

    middle = [-x for x in middle]

    return beginning + middle + end

def get_formatted_p(p):
    formatted_p = ""
    for x in p:
        if x == abs(x):
            formatted_p += ('+' + str(x) + ' ')
        else:
            formatted_p += str(x) + ' '
    return formatted_p

def main():
    arg_count = len(argv)
    if arg_count < 2:
        print("ERROR: No command line argument provided. See README.md.")
        exit(1)

    data_file_name = argv[1]
    if not path.isfile(data_file_name):
        print("ERROR: Specified data file " + data_file_name + " not found. See README.md.")
        exit(1)
    
    permutation = process_data_file(data_file_name)

    print("Specified data file found and processed:", "\nPermutation =", permutation, '\n')

    #
    # Solution Logic:
    #

    solution = []

    step = 1

    identity = [number for number in range(1, len(permutation) + 1)]
    # For each number in the identity permutation...
    for number in identity:
        # For each index in the permutation
        for p_index in range(len(permutation)):
            # Search for the current number in the permutation
            # If the absolute value of the number at the current permutation index is equal to the current number...
            if abs(permutation[p_index]) == number:
                # If the number is at the incorrect index...
                if number - 1 != p_index:
                    # Perform a reversal on the permutation in order to place said number at the correct index
                    permutation = get_reversal(permutation, number - 1, p_index)
                    # Append the reversal to the solution
                    solution.append("(" + str(step) + ") " + get_formatted_p(permutation))
                    # Increment the step counter
                    step += 1
                # If the number (now guaranteed to be at the correct index of the permutation) is negative...
                if permutation[number - 1] != abs(permutation[number - 1]):
                    # Perform a reversal on the permutation in order to make said number positive
                    permutation = get_reversal(permutation, number - 1, number - 1)
                    # Append the reversal to the solution  
                    solution.append("(" + str(step) + ") " + get_formatted_p(permutation))
                    # Increment the step counter
                    step += 1

    #
    # Output Logic:
    #

    output_file_name = data_file_name.split(".txt")[0] + "_output.txt"
    output_file = open(output_file_name, "w")

    print_and_write(output_file, "Steps: ")
    for step in solution:
        print_and_write(output_file, step)

    print("\nThis solution has been written to " + output_file_name)

if __name__ == "__main__":
    main()