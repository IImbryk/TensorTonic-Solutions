import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    n_size, m_size = np.array(A).shape
    B = np.zeros((m_size, n_size))
    for i in range(0, n_size):
        for j in range(0, m_size):
            B[j][i] = A[i][j]
    return B
