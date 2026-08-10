# I'm going to start the file by importing the necessary libraries and functions from other files. 
# I will import the format_matrix and print_matrix functions from helpers.py, and other functions from their respective files.

from helpers import format_matrix, print_matrix
from gauss_jordan import gauss_jordan
from gauss_elimination import gauss_elimination
from LU_decomposition import lu_decomposition
from QR_decomposition import qr_decomposition

def main():
    # I want to create a menu for the user to choose which method they want to use, so I'm doing this below
    menu = ["1. Gauss Jordan Elimination", "2. Gauss Elimination", "3. LU Decomposition", "4. QR Decomposition"]

    # Now I take the number as input and then perform stuff accordingly
    print("See the list of options below and choose the one you want to use:")
    for option in menu:
        print(option)
    choice = input("Enter your choice: ")

    if choice == "1":
        mat = [
                [2, 1, -1, 8],
                [-3, -1, 2, -11],
                [-2, 1, 2, -3]
            ]
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
    elif choice == "3":
        A = [[4, 3], [6, 3]]
        L, U = lu_decomposition(A)
        L = format_matrix(L)
        U = format_matrix(U)
        print("L:")
        print_matrix(L)
        print("U:")
        print_matrix(U)
    elif choice == "4":
        A = [[4, 3], [6, 3]]
        Q, R = qr_decomposition(A)
        Q = format_matrix(Q)
        R = format_matrix(R)
        print("Q:")
        print_matrix(Q)
        print("R:")
        print_matrix(R)
    else:
        print("Invalid choice.")
        return


if __name__ == "__main__":
    main()