# O método dos mínimos quadrados é uma técnica usada para encontrar a melhor aproximação de um conjunto de pontos por uma função matemática. Ele é comumente aplicado em problemas de regressão, onde o objetivo é encontrar a equação de uma curva que melhor se ajusta aos dados observados.
# minimizar o erro |a1x + a0 - y| para um conjunto de pontos (Xi, Yi), i=0,..., m
# para isso determinamos a função φ(a) = ||Aa - Y||² onde:
# A = |1 x0|    ,   a = |a0|  ,   Y = | y0|
#     |1 x1|        a = |a1|          | y1|
#     |... |                          |...|
#     |1 xm|                          | ym|
# e a norma || ||² é definida por: ||X||² = √(Σ(xi²)) para um vetor X = {Xi}
# desta forma temos:
# φ(a) = 1/2 * √(Σ(a1xi + a0 - yi)²)² => 1/2 * Σ(a1xi + a0 - yi)²
# para minimizar φ(a) devemos ter ∂φ(a)/∂a = 0 e ∂φ(a)/∂b = 0
# ∂φ(a)/∂a = 0 = Σ(a1xi + a0 - yi)
# ∂φ(a)/∂b = 0 = Σ(xi(a1xi² + a0xi - yixi))
# Logo, podemos construir o seguite sistema equivalente:
# AtAa = AtAy => |m+1     Σ(xi)| * |a0| = | Σ(yi) |
#                |Σ(xi)  Σ(xi²)|   |a1|   |Σ(yixi)|
import numpy as np
import matplotlib.pyplot as plt

# Pontos tabelados (xi, yi)
x = np.array([0, 1, 2, 3, 4, 5, 6])
y = np.array([0, -4, -2, 12, 44, 100, 186])

# Construir as matrizes X e Y
X = np.column_stack((np.ones_like(x), x**3))
Y = y.reshape(-1, 1)

# Resolver o sistema de equações lineares
coef = np.linalg.lstsq(X, Y, rcond=None)[0]

# Obter os coeficientes a e b
a, b = coef.flatten()

# Construir o polinômio P(x)
def P(x):
    return a + b * x**3

# Gerar pontos para plotagem
x_plot = np.linspace(min(x), max(x), 100)
y_plot = P(x_plot)

# Imprimir os resultados
print("Coeficientes a e b:", a, b)
print("P(x) = ",a+b)

# Plotar o gráfico
plt.scatter(x, y, color='blue', label='Pontos Tabelados')
plt.plot(x_plot, y_plot, color='red', label='Polinômio Aproximado')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
