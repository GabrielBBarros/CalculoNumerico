"""
O código implementa o método de quadratura de Gauss-Chebyshev para calcular uma integral numérica de uma função em um intervalo específico.

A quadratura de Gauss-Chebyshev utiliza pontos de amostragem baseados nos zeros do polinômio de Chebyshev de primeira espécie. Esses pontos são distribuídos de forma a obter uma aproximação precisa da integral.

O código começa definindo a função gauss_chebyshev_integration, que recebe como entrada a função a ser integrada, os limites de integração e o número de pontos de amostragem desejado.

Em seguida, o código calcula os pontos de amostragem usando os zeros do polinômio de Chebyshev de primeira espécie através da função numpy.cos() e numpy.pi. Esses pontos são transformados do intervalo (-1, 1) para o intervalo de integração especificado.

A integral é aproximada calculando a soma dos valores da função nos pontos de amostragem. Em seguida, é aplicado um fator de escala para ajustar a integral aproximada ao intervalo de integração original.

No exemplo fornecido, a função f(x) = x^2 é integrada no intervalo de 0 a 1, usando 4 pontos de amostragem. O resultado da integral aproximada é exibido no console.

A quadratura de Gauss-Chebyshev é um método eficaz para calcular integrais numéricas em intervalos limitados, especialmente quando a função possui singularidades no intervalo [-1, 1]. Ela é amplamente utilizada em cálculos numéricos e análise numérica para obter aproximações precisas das integrais.
"""

import numpy as np

def gauss_chebyshev(f, a, b, n):
    # Calcula os pontos de amostragem usando os zeros do polinômio de Chebyshev de primeira espécie
    x = np.cos(np.pi * (np.arange(n) + 0.5) / n)

    # Transforma os pontos de amostragem do intervalo (-1, 1) para o intervalo (a, b)
    t = 0.5 * (x + 1) * (b - a) + a

    # Calcula a integral aproximada
    integral = 0
    for i in range(n):
        integral += f(t[i])

    # Multiplica pelo fator de escala
    integral *= (b - a) / n

    # Retorna a integral aproximada
    return integral

# Exemplo de função para integrar: f(x) = x^2
def f(x):
    return (5*x*np.sqrt(x)/(2))

# Intervalo de integração
a = 4
b = 9

# Número de pontos de amostragem (precisão da aproximação)
n = 10

# Calcula a integral usando a quadratura de Gauss-Chebyshev
integral = gauss_chebyshev(f, a, b, n)

print("Integral aproximada:", integral)
