def gauss_jordan(matrix):
    n = len(matrix)

    for i in range(n):
        pivot = matrix[i][i]

        if pivot == 0:
            raise ValueError("Zero pivot encountered")

        # Normalize row
        for j in range(len(matrix[i])):
            matrix[i][j] /= pivot

        # Eliminate other rows
        for k in range(n):
            if k != i:
                factor = matrix[k][i]
                for j in range(len(matrix[k])):
                    matrix[k][j] -= factor * matrix[i][j]

    return matrix