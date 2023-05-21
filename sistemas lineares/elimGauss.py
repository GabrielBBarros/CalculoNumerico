#  Ele envolve a aplicação de operações elementares de linha em uma matriz aumentada, levando-a a uma forma escalonada. O processo é realizado da seguinte maneira:

# 1- Dado um sistema de equações lineares, escreva-o como uma matriz aumentada, onde os coeficientes das variáveis são colocados em uma matriz e os termos constantes são colocados em uma coluna adicional.
 
# 2- Comece pela primeira coluna e primeira linha da matriz aumentada. Se o elemento nessa posição for zero, troque essa linha com outra linha abaixo para garantir que o elemento seja não-zero. Se não houver linhas abaixo com elementos não-zero nessa coluna, pare, pois o sistema não tem solução única.
 
# 3- Divida a primeira linha pelo elemento não-zero na posição atual para obter um "1" como pivô.
 
# 4- Use operações elementares de linha para zerar todos os elementos abaixo do pivô. Para cada linha abaixo, multiplique a primeira linha pelo valor necessário e subtraia-o da linha atual. Isso garante que todos os elementos abaixo do pivô se tornem zero.
 
# 5- Repita os passos 2 a 4 para as colunas subsequentes, avançando uma coluna de cada vez.
 
# 6- Depois de concluir todas as colunas ou alcançar a última linha, a matriz aumentada estará na forma escalonada reduzida.
 
# 7- Resolva o sistema de equações resultante, lendo os valores das variáveis a partir das colunas e determinando suas soluções.

# O método de eliminação de Gauss é eficiente e amplamente utilizado para resolver sistemas de equações lineares, pois simplifica o sistema, tornando-o mais fácil de resolver.

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
    