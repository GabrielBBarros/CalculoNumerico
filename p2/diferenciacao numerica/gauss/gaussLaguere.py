"""
A quadratura de Gauss-Laguerre é um método numérico utilizado para calcular integrais numéricas de funções multiplicadas por uma função peso, onde a função peso é dada pela forma e^(-x) * f(x). Esse método é especialmente adequado para integrar funções que têm um decaimento exponencial em intervalos infinitos positivos.

O método de Gauss-Laguerre aproxima a integral dividindo o intervalo de integração em pontos de amostragem específicos, chamados de pontos de Gauss-Laguerre, e atribuindo pesos a esses pontos. Os pontos de amostragem são obtidos a partir dos zeros do polinômio de Laguerre.

No código fornecido, a função gauss_laguerre_integration implementa o método da quadratura de Gauss-Laguerre. Ela recebe como entrada a função a ser integrada (f) e o número de pontos de amostragem (n). A função retorna a integral aproximada da função.

A biblioteca NumPy é utilizada para calcular os pontos de amostragem (x) e os pesos (w) da quadratura de Gauss-Laguerre através da função numpy.polynomial.laguerre.laggauss(). Esses pontos e pesos são usados para calcular a integral aproximada da função.

A função exemplo f(x) = x^2 * e^(-x) é utilizada para demonstrar o cálculo da integral aproximada. Essa função é comumente encontrada em problemas de física e matemática, especialmente em problemas envolvendo distribuições exponenciais.

A quadratura de Gauss-Laguerre é um método eficaz para calcular integrais numéricas em intervalos infinitos positivos, onde a função peso é dada por e^(-x) * f(x). É amplamente utilizado em diversas áreas, como física, matemática aplicada e engenharia, onde a função peso assume essa forma. A precisão da aproximação da integral pode ser ajustada variando o número de pontos de amostragem (n).

Em resumo, a quadratura de Gauss-Laguerre fornece uma técnica confiável e precisa para calcular integrais numéricas em problemas envolvendo intervalos infinitos positivos e funções com decaimento exponencial. É uma ferramenta valiosa para a resolução eficiente de problemas em diversas áreas do conhecimento.
"""

import numpy as np

def gauss_laguerre(f, n, lower, upper):
    # Calcula os pontos de amostragem e os pesos usando a fórmula de Gauss-Laguerre
    x, w = np.polynomial.laguerre.laggauss(n)

    # Calcula a integral aproximada
    integral = 0
    for i in range(n):
        t = (upper - lower) * (x[i] + 1) / 2 + lower  # Mapeia os pontos de amostragem para o intervalo [lower, upper]
        integral += w[i] * f(t)

    # Retorna a integral aproximada
    return (upper - lower) * integral / 2

# Exemplo de função para integrar: f(x) = x^2 * e^(-x), intervalo de [1, 3]
def f(x):
    return x**2 * np.exp(-x)

# Número de pontos de amostragem (precisão da aproximação)
n = 4

# Limites inferior e superior da integral
lower = 1
upper = 3

# Calcula a integral usando a quadratura de Gauss-Laguerre com os limites definidos
integral = gauss_laguerre(f, n, lower, upper)

print("Integral aproximada:", integral)

