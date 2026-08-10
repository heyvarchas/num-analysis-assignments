"""
So basically I'm getting a floating point problem when I run the code, it displays -0.0 instead of 0.0 in the output. 
This is a common issue with floating point arithmetic in Python (and many other programming languages) due to how numbers are represented in memory.
I'm going to create a function to round and format the matrix, later another one to print the matrix (pretty print)
"""

def format_matrix(data, eps=1e-9):
    """
    This function uses recursion to format the matrix, so if the data is a list, it will call itself on each element of the list. 
    If the data is a float or int, it will round it to 2 decimal places and if it's very close to zero, it will set it to 0.0
    """
    # case 1: If the data is a list, I want to format each element in the list
    if isinstance(data, list):
        return [format_matrix(x, eps) for x in data]

    # case 2: If the data is a float or int, I want to round it to 2 decimal places and if it's very close to zero, I want to set it to 0.0
    elif isinstance(data, (int, float)):
        if abs(data) < eps:
            data = 0.0
        return f"{data:.2f}"

    # fallback (just in case)
    return data

# Pretty Print function
def print_matrix(matrix):
    # check if 1D list
    if not isinstance(matrix[0], list):
        print("[", end=" ")
        for val in matrix:
            print(f"{val:>6}", end=" ")
        print("]")
        return

    # normal 2D case
    for row in matrix:
        print("[", end=" ")
        for val in row:
            print(f"{val:>6}", end=" ")
        print("]")

def get_input(choice):
    if choice == "1":
        mat = [[], [], []]  # Placeholder for the augmented matrix
        print("Input Augmented Matrix:")
        for i in range(3):
            row = input(f"Enter row {i+1} (space-separated): ")
            mat[i] = list(map(float, row.split()))
        return mat
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
        return A, b
    elif choice == "3":
        n = int(input("Enter the value of n (square matrix): "))
        print("Enter the matrix A row by row (Space-separated):")
        A = [list(map(float, input(f"Row {i+1}: ").split())) for i in range(n)]
        return A
    elif choice == "4":
        m = int(input("Enter number of rows: "))
        n = int(input("Enter number of columns: "))
        A = []
        print("Enter the matrix row-wise:")
        for i in range(m):
            row = list(map(float, input(f"Row {i+1} (space separated): ").split()))
            A.append(row)
        return A
    elif choice == "5":
        coeffs_input = input("Enter coefficients of the polynomial (highest degree first, space-separated): ")
        coeffs = list(map(float, coeffs_input.split()))
        return coeffs