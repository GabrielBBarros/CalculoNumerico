# é preferível utilziar o método do trapézio quando há Funções com comportamento irregular: O método de Simpson é mais eficaz quando a função a ser integrada é suave e bem-comportada, aproximando-se de uma parábola. No entanto, se a função apresentar comportamento irregular, como descontinuidades ou picos acentuados, o método do trapézio pode ser mais estável e fornecer resultados mais confiáveis.import numpy as np
import numpy as np
def f(x):
    return (x*np.exp(-x**2))

def trapezoidal_rule(a, b, n):
    h = (b - a) / n  # Tamanho do intervalo
    integral = 0.5 * (f(a) + f(b))  # Inicialização da integral

    for i in range(1, n):
        x = a + i * h
        integral += f(x)

    integral *= h  # Multiplica pela largura do intervalo
    return integral

# Exemplo de uso
a = 0  # Extremo inferior do intervalo
b = 1  # Extremo superior do intervalo
n = 100  # Número de segmentos (quanto maior, mais precisa)

approximation = trapezoidal_rule(a, b, n)
print("Estimativa da integral:", approximation)