'''
Calculo de aproximação de integral,
calcular a area de um intervalo entre uma curva de uma função com o eixo das abcissas,
h = (xn - x1) / 2 ((n - 1) / 2)
Is = (h / 3) * (f(x1) + 4f(x2) + f(x3)) ... (f(xn) + 4f(xn+1) + f(xn+2))
'''
import numpy as np
def f(x):
     return (5*x*np.sqrt(x)/(2))

def simpsons_rule(a, b, n):
    h = (b - a) / n  # Tamanho do intervalo
    integral = f(a) + f(b)  # Inicialização da integral

    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            integral += 2 * f(x)
        else:
            integral += 4 * f(x)

    integral *= h / 3  # Multiplica pela largura do intervalo e divide por 3
    return integral

# Exemplo de uso
a = 4  # Extremo inferior do intervalo
b = 9  # Extremo superior do intervalo
n = 100  # Número de segmentos (quanto maior, mais precisa)

approximation = simpsons_rule(a, b, n)
print("Estimativa da integral:", approximation)
