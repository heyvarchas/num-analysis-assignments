# I'm going to start the file by importing the necessary libraries and functions from other files. 
# I will import the format_matrix and print_matrix functions from helpers.py, and other functions from their respective files.

from helpers import format_matrix, print_matrix
from gauss_jordan import gauss_jordan
from gauss_elimination import gauss_elimination

def main():
    # I want to create a menu for the user to choose which method they want to use, so I'm doing this below
    menu = ["1. Gauss Jordan Elimination", "2. Gauss Elimination"]

    # Now I take the number as input and then perform stuff accordingly
    print("See the list of options below and choose the one you want to use:")
    for option in menu:
        print(option)
    choice = input("Enter your choice: ")

    mat = [
        [2, 1, -1, 8],
        [-3, -1, 2, -11],
        [-2, 1, 2, -3]
    ]

    if choice == "1":
        result = gauss_jordan(mat)
        result = format_matrix(result)  # Format the matrix values
        print("RREF:")
        print_matrix(result)
    elif choice == "2":
        A = [[2, 1, -1],
         [-3, -1, 2],
         [-2, 1, 2]]
        b = [8, -11, -3]
        result = gauss_elimination(A, b)
        result = format_matrix(result)
        print("Solution:")
        print_matrix(result)
    else:
        print("Invalid choice.")
        return


if __name__ == "__main__":
    main()