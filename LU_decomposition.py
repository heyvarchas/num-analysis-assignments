def lu_decomposition(A):
    n = len(A)

    # Initialize L and U with zeros
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

    for i in range(n):
        # Upper Triangular (U)
        for k in range(i, n):
            sum_u = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = A[i][k] - sum_u

        # Lower Triangular (L)
        for k in range(i, n):
            if i == k:
                L[i][i] = 1.0  # Diagonal = 1
            else:
                sum_l = sum(L[k][j] * U[j][i] for j in range(i))
                if U[i][i] == 0:
                    raise ValueError("Division by zero (pivot = 0). Try pivoting.")
                L[k][i] = (A[k][i] - sum_l) / U[i][i]

    return [L, U]