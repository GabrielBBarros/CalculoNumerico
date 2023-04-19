import numpy as np

def eliminacao_gauss(A, b):
    n = len(b)
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


A = np.array([[2, -1, 1],
              [3, 2, -2],
              [1, 1, 1]])

b = np.array([5, -1, 3])

x = eliminacao_gauss(A, b)

print("Solução:")
for i, xi in enumerate(x):
    print("x{} = {:.2f}".format(i+1, xi))