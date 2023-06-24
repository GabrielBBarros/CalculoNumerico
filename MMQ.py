#A ideia básica por trás do método é encontrar uma reta que minimize a distância vertical entre os pontos de dados e a reta. Isso é feito ajustando os coeficientes da equação da reta (y = ax + b) de forma a minimizar a soma dos quadrados das diferenças entre os valores observados de y e os valores preditos pela reta ajustada.

#Vamos analisar o código passo a passo:

 #   A função least_squares recebe dois arrays, x e y, que representam os pontos de dados que queremos ajustar.

 #   Em seguida, a função calcula algumas somas e produtos necessários para obter os coeficientes a e b da equação da reta.
#        n representa o número de pontos de dados.
#        sum_x é a soma dos valores de x.
#        sum_y é a soma dos valores de y.
#        sum_x_squared é a soma dos quadrados dos valores de x.
#        sum_xy é a soma dos produtos dos valores de x e y.

#    Os coeficientes a e b são calculados usando as fórmulas dos mínimos quadrados:
#        a = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)
#        b = (sum_y - a * sum_x) / n

#    Por fim, a função retorna os coeficientes a e b.

#No exemplo fornecido, os dados de exemplo são os pontos (1, 2), (2, 3), (3, 4), (4, 5), e (5, 6). O código calcula e imprime os coeficientes a e b da equação da reta que melhor se ajusta a esses pontos. Esses coeficientes podem ser interpretados como o coeficiente angular e o coeficiente linear da reta, respectivamente.


import numpy as np

def MMQ(x, y):
    # Calcula os coeficientes a e b da equação da reta y = ax + b
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x_squared = np.sum(x**2)
    sum_xy = np.sum(x*y)

    a = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)
    b = (sum_y - a * sum_x) / n

    return a, b

# Dados de exemplo
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 4, 5, 6])

# Calcula os coeficientes a e b usando o método dos mínimos quadrados
a, b = MMQ(x, y)

# Imprime os coeficientes
print("Coeficiente a:", a)
print("Coeficiente b:", b)
