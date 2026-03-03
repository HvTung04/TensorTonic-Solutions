import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A = np.array(A)
    shape = A.shape
    result = np.zeros(shape=(shape[1], shape[0]))
    for i in range(shape[0]):
        for j in range(shape[1]):
            value = A[i][j]
            result[j][i] = value

    return result