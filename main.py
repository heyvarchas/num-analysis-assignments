from gauss_jordan import gauss_jordan

"""
So basically I'm getting a floating point problem when I run the code, it displays -0.0 instead of 0.0 in the output. 
This is a common issue with floating point arithmetic in Python (and many other programming languages) due to how numbers are represented in memory.
So I'm going to create another function that can modify my output the way I want it to be.
"""

def clean_matrix(matrix, eps=1e-9):
    return [
        [0.0 if abs(x) < eps else x for x in row]
        for row in matrix
    ]

def main():
    mat = [
        [2, 1, -1, 8],
        [-3, -1, 2, -11],
        [-2, 1, 2, -3]
    ]

    result = gauss_jordan(mat)
    result = clean_matrix(result)

    print("RREF:")
    for row in result:
        print(row)


if __name__ == "__main__":
    main()