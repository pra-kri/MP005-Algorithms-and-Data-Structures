import numpy as np
import scipy
import math
"""
Cholesky decomposition --> implement from scratch.

Uses: Used to decompose a +ve symmetrical matrix into L.L^T, where L is a lower triangular matrix.

- Very useful for Quants, since correlation matrices between assets are symmetrical, and the corresponding lower triangular matrix (L) can be used to generate random correlated samples.


References:
http://drsfenner.org/blog/2016/02/basic-cholesky-implementation/
https://www.quantstart.com/articles/Cholesky-Decomposition-in-Python-and-NumPy
https://www.geeksforgeeks.org/cholesky-decomposition-matrix-decomposition/
"""



N = np.array([
    [4, 12, -16],
    [12, 37, -43],
    [-16, -43, 98]])

print(N)
print(N.shape[1])


def cholesky_decomposition(M):
    """
    output will be a lower triangular matrix, L.
    Can use L when trying to sample correlated random variables (e.g. correlated market returns...)
    """
    L = np.zeros(shape = (M.shape[0], M.shape[1]))

    for row in range(M.shape[0]):
        for column in range(row + 1): 
        #only go up to row+1, because the rest of the elements will be zero
            temp1 = 0
            for j in range(column):
                temp1 += L[row][j] * L[column][j]

            # for diagonal elements:
            if row == column:
                L[row][column] = math.sqrt(M[row][column] - temp1)

            else:
                L[row][column] = (1/ L[column][column]) * (M[row][column] - temp1)

    return L
            


print(cholesky_decomposition(N))
# ok it works...but should probably use names like i,j,k instead of 'column' and 'row', next time...


