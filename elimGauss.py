import numpy as np

def eliminGauss(A, b):
    n = len(b)
    b = b.astype(float)
    A = A.astype(float)
    # Etapa de escalonamento
    for k in range(n-1):  # Loop sobre as colunas
        for i in range(k+1, n):  # Loop sobre as linhas abaixo da diagonal
            # Cálculo do multiplicador
            m = A[i,k] / A[k,k]
            # Operações de eliminação
            A[i,k+1:n] -= m * A[k,k+1:n]
            b[i] -= m * b[k]
    
    # Etapa de substituição retroativa
    x = np.zeros(n)
    x[n-1] = b[n-1] / A[n-1,n-1]  # Última variável desconhecida
    for i in range(n-2, -1, -1):  # Loop reverso sobre as linhas
        # Cálculo das variáveis desconhecidas restantes
        x[i] = (b[i] - np.dot(A[i,i+1:n], x[i+1:n])) / A[i,i]
    
    return x

# metodo Gauss Pivotamente parcial
import numpy as np

def eliminGauss_pivot(A, b):
    n = len(b)
    A = A.astype(float)
    b = b.astype(float)
    # Etapa de escalonamento
    for k in range(n-1):  # Loop sobre as colunas
        # Escolha do pivô com pivotamento parcial
        p = np.argmax(np.abs(A[k:, k])) + k  # Índice da linha com maior valor absoluto
        # Permutação das linhas k e p
        if p != k:
            A[[k, p]] = A[[p, k]]
            b[[k, p]] = b[[p, k]]
        for i in range(k+1, n):  # Loop sobre as linhas abaixo da diagonal
            # Cálculo do multiplicador
            m = A[i,k] / A[k,k]
            # Operações de eliminação
            A[i,k+1:n] -= m * A[k,k+1:n]
            b[i] -= m * b[k]
    
    # Etapa de substituição retroativa
    x = np.zeros(n)
    x[n-1] = b[n-1] / A[n-1,n-1]  # Última variável desconhecida
    for i in range(n-2, -1, -1):  # Loop reverso sobre as linhas
        # Cálculo das variáveis desconhecidas restantes
        x[i] = (b[i] - np.dot(A[i,i+1:n], x[i+1:n])) / A[i,i]
    
    return x

A = np.array([[3, 3, 1],
              [2, 2, -1],
              [1, -1, 5]])

b = np.array([7, 3, 5])

x = eliminGauss_pivot(A, b)

print("Solução:")
for i, xi in enumerate(x):
    print("x{} = {:.2f}".format(i+1, xi))
    