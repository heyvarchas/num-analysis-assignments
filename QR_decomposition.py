# In this I've coded a function that performs QR decomposition using the Gram Schmidt Process...
import math

def qr_decomposition(A):

    # Convert to float for precision
    A = [[float(x) for x in row] for row in A]

    m = len(A)
    n = len(A[0])

    # Initialize Q and R
    Q = [[0.0] * n for _ in range(m)]
    R = [[0.0] * n for _ in range(n)]

    # Helper: dot product
    def dot(u, v):
        return sum(u[i] * v[i] for i in range(len(u)))

    # Helper: norm
    def norm(v):
        return math.sqrt(dot(v, v))

    # Helper: scalar multiply
    def scalar_mult(s, v):
        return [s * x for x in v]

    # Helper: vector subtraction
    def subtract(u, v):
        return [u[i] - v[i] for i in range(len(u))]

    # Get column from matrix
    def get_col(A, j):
        return [A[i][j] for i in range(m)]

    # Set column in Q
    def set_col(Q, j, col):
        for i in range(m):
            Q[i][j] = col[i]

    for j in range(n):
        v = get_col(A, j)

        for i in range(j):
            q_i = get_col(Q, i)
            R[i][j] = dot(q_i, v)
            proj = scalar_mult(R[i][j], q_i)
            v = subtract(v, proj)

        R[j][j] = norm(v)

        if R[j][j] == 0:
            raise ValueError("Matrix has linearly dependent columns")

        q_j = scalar_mult(1 / R[j][j], v)
        set_col(Q, j, q_j)

    return [Q, R]