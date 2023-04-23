import numpy as np
from numpy import linalg as la

def jacobi(A, b, x0 = None, tol = 50, max_iter = 1e-4):
    if x0 is None:
        x0 = np.ones_like(b)
    D = np.diag(np.diag(A))
    L = np.tril(A, -1)
    R = np.triu(A, 1)
    n = A.shape[0]
    
    # for i in range(n):
    #     D[i, i] = 1/D[i, i]
    invD = la.inv(D)
    
    B = -invD @ (L + R)
    g = invD @ b
    
    for it in range(max_iter):
        x = B @ x0 + g
        
        err = la.norm(x - x0)/la.norm(x)
        
        if err < tol:
            return x, it
        
        x0 = x
        
    print('Maximo de iteracoes atingido')
    return x, max_iter

A = np.array([[10., 2, 1], [1, 5, 1], [2, 3, 10]])
b = np.zeros((3, 1))
b[0] = 7
b[1] = -8
b[2] = 6

x, it = jacobi(A, b, tol = 1e-4, max_iter = 10)
print(f'Solução: {x} em {it} iterações')