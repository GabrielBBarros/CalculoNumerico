"""
A quadratura de Gauss-Hermite é um método numérico utilizado para calcular integrais numéricas de funções multiplicadas por uma função peso, onde a função peso é dada pela distribuição normal. Esse método é particularmente útil quando a função a ser integrada envolve termos exponenciais e a função peso tem a forma e^(-x^2).

O método de Gauss-Hermite aproxima a integral dividindo o intervalo de integração em pontos de amostragem específicos, chamados de pontos de Gauss-Hermite, e atribuindo pesos a esses pontos. Os pontos de amostragem são obtidos a partir dos zeros do polinômio de Hermite.

No código fornecido, a função gauss_hermite_integration implementa o método da quadratura de Gauss-Hermite. Ela recebe como entrada a função a ser integrada (f) e o número de pontos de amostragem (n). A função retorna a integral aproximada da função.

A biblioteca NumPy é utilizada para calcular os pontos de amostragem (x) e os pesos (w) da quadratura de Gauss-Hermite através da função numpy.polynomial.hermite.hermgauss(). Esses pontos e pesos são usados para calcular a integral aproximada da função.

A função exemplo f(x) = x^2 * e^(-x^2) é utilizada para demonstrar o cálculo da integral aproximada. Essa função é comumente encontrada em problemas de física e matemática, especialmente em problemas relacionados à mecânica quântica.

A quadratura de Gauss-Hermite é um método eficaz para calcular integrais numéricas envolvendo a distribuição normal e funções exponenciais. É amplamente utilizado em diversas áreas, como física, matemática e engenharia, onde a função peso assume a forma e^(-x^2). A precisão da aproximação da integral pode ser ajustada variando o número de pontos de amostragem (n).

Em resumo, a quadratura de Gauss-Hermite fornece uma técnica confiável e precisa para calcular integrais numéricas em problemas envolvendo a distribuição normal e funções exponenciais, contribuindo para a resolução eficiente de diversos tipos de problemas.

"""

import numpy as np

def gauss_hermite(f, n):
    # Calcula os pontos de amostragem e os pesos usando a fórmula de Gauss-Hermite
    x, w = np.polynomial.hermite.hermgauss(n)

    # Calcula a integral aproximada
    integral = 0
    for i in range(n):
        integral += w[i] * f(x[i])

    # Retorna a integral aproximada
    return integral

# Exemplo de função para integrar: f(x) = x^2 * e^(-x^2)
def f(x):
    return x ** 2 * np.exp(-x ** 2)

# Número de pontos de amostragem (precisão da aproximação)
n = 4

# Calcula a integral usando a quadratura de Gauss-Hermite
integral = gauss_hermite(f, n)

print("Integral aproximada:", integral)
