"""
O código implementa o método de quadratura de Gauss-Legendre para calcular uma integral numérica de uma função em um intervalo específico.

O método de Gauss-Legendre aproxima a integral dividindo o intervalo em uma série de pontos de amostragem e atribuindo pesos a esses pontos. Esses pontos e pesos são calculados usando fórmulas específicas baseadas nos polinômios de Legendre.

O código começa definindo a função gauss_legendre_integration, que recebe como entrada a função a ser integrada, os limites de integração e o número de pontos de amostragem desejado.

Em seguida, o código utiliza a biblioteca NumPy para calcular os pontos de amostragem e pesos de Gauss-Legendre usando a função numpy.polynomial.legendre.leggauss(). Os pontos de amostragem são então transformados do intervalo (-1, 1) para o intervalo de integração especificado.

A integral é aproximada calculando a soma ponderada dos valores da função nos pontos de amostragem, multiplicados pelos pesos correspondentes. Por fim, o resultado da integral aproximada é retornado.

"""

import numpy as np

def gauss_legendre(f, a, b, n):
    # Calcula os pesos e pontos de amostragem usando a fórmula de Gauss-Legendre
    x, w = np.polynomial.legendre.leggauss(n)

    # Transforma os pontos de amostragem do intervalo (-1, 1) para o intervalo (a, b)
    t = 0.5 * (x + 1) * (b - a) + a

    # Calcula a integral aproximada
    integral = 0
    for i in range(n):
        integral += w[i] * f(t[i])

    # Retorna a integral aproximada
    return integral * 0.5 * (b - a)

# Exemplo de função para integrar: f(x) = x^2
def f(x):
    return (5*x*np.sqrt(x)/(2))

# Intervalo de integração
a = 4
b = 9

# Número de pontos de amostragem (precisão da aproximação)
n = 4

# Calcula a integral usando a quadratura de Gauss-Legendre
integral = gauss_legendre(f, a, b, n)

print("Integral aproximada:", integral)
