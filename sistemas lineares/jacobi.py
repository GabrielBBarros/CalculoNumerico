# O método de Jacobi é um algoritmo iterativo utilizado para resolver sistemas de equações lineares. Ele é especialmente útil quando o sistema é grande e esparsamente populado.

# O método de Jacobi funciona da seguinte maneira:
 
# 1- Dado um sistema de equações lineares na forma matricial Ax = b, onde A é a matriz dos coeficientes, x é o vetor desconhecido e b é o vetor de termos independentes, podemos reescrever a equação como Ax = (L + D + U)x = b, onde L é a matriz triangular inferior, D é a matriz diagonal e U é a matriz triangular superior de A.
 
# 2- A equação pode ser então reescrita como (D)x = (b - (L + U)x), onde D é invertível.
 
# 3- A partir dessa equação, podemos iterativamente calcular a solução aproximada x em cada iteração. A fórmula de iteração de Jacobi é dada por: x(k+1) = D^(-1) * (b - (L + U)x(k)) onde x(k) é a aproximação atual na k-ésima iteração e x(k+1) é a aproximação na próxima iteração. D^(-1) representa a matriz inversa de D.
 
# 4- O processo de iteração continua até que a solução converja para um determinado critério de parada, como uma tolerância pré-definida ou um número máximo de iterações.

# Em resumo, o método de Jacobi divide o sistema original em uma série de equações lineares mais simples, que são iterativamente resolvidas para obter uma solução aproximada. O método continua a iterar até que a solução convirja para uma solução aceitável.

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