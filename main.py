# I'm going to start the file by importing the necessary libraries and functions from other files. 
# I will import the format_matrix and print_matrix functions from helpers.py, and other functions from their respective files.

from helpers import format_matrix, print_matrix
from gauss_jordan import gauss_jordan
from gauss_elimination import gauss_elimination
from LU_decomposition import lu_decomposition
from QR_decomposition import qr_decomposition
from bairstow_method import bairstow

def main():
    # I want to create a menu for the user to choose which method they want to use, so I'm doing this below
    menu = ["1. Gauss Jordan Elimination", "2. Gauss Elimination", "3. LU Decomposition", "4. QR Decomposition", "5. Bairstow's Method"]

    # Now I take the number as input and then perform stuff accordingly
    print("See the list of options below and choose the one you want to use:")
    for option in menu:
        print(option)
    choice = input("Enter your choice: ")

    if choice == "1":
        mat = [[], [], []]  # Placeholder for the augmented matrix
        print("Input Augmented Matrix:")
        for i in range(3):
            row = input(f"Enter row {i+1} (space-separated): ")
            mat[i] = list(map(float, row.split()))
        result = gauss_jordan(mat)
        result = format_matrix(result)  # Format the matrix values
        print("RREF:")
        print_matrix(result)
    elif choice == "2":
        n = int(input("Enter number of variables: "))
        A = []
        print("Enter matrix A row by row:")
        for i in range(n):
            row = list(map(float, input(f"Row {i+1}: ").split()))
            A.append(row)
            if len(row) != n:
                raise ValueError("Each row must have n elements")
        print("Enter vector b:")
        b = list(map(float, input().split()))
        if len(b) != n:
            raise ValueError("b must have n elements")

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
    elif choice == "5":
        coeffs = [1, -6, 15, -30, 44, -24]  # x^5 - 6x^4 + 15x^3 - 30x^2 + 44x - 24
        roots = bairstow(coeffs[::-1])  # Reverse coefficients for bairstow

        print("\nAll roots:")
        print_matrix(roots)
    else:
        print("Invalid choice.")
        return


if __name__ == "__main__":
    main()