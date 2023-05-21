# Ele envolve a utilização de derivadas para iterativamente se aproximar de uma raiz. Aqui está uma explicação concisa do método:

# 1- Escolha uma estimativa inicial para a raiz da função.
# 2- Calcule a derivada da função no ponto da estimativa inicial.
# 3- Use a fórmula de Newton-Raphson para obter uma nova estimativa mais precisa da raiz: a nova estimativa é igual à estimativa atual menos o valor da função dividido pelo valor da derivada.
# 4- Repita os passos 2 e 3 até que a diferença entre as estimativas consecutivas seja suficientemente pequena ou até que um número máximo de iterações seja atingido.
# 5- A estimativa final obtida é a aproximação da raiz da função.

# O método de Newton-Raphson é eficiente para encontrar raízes de funções quando a derivada é conhecida e quando a estimativa inicial está suficientemente próxima da raiz desejada.

# A fórmula do método de Newton-Raphson para obter uma nova estimativa da raiz é:
# x_{n+1} = x_n - f(x_n) / f'(x_n)
# Onde:
# x_n é a estimativa atual da raiz.
# f(x_n) é o valor da função no ponto da estimativa atual.
# f'(x_n) é o valor da derivada da função no ponto da estimativa atual.
# x_{n+1} é a nova estimativa mais precisa da raiz.

import numpy as np
from sympy import symbols, diff, cos

def newton_raphson(f, x0, tolerance, max_it):
    x = symbols('x')
    for i in range(max_it):
        fx = f(x)
        dfx = diff(fx, x)
        if abs(fx.subs(x, x0).evalf()) < tolerance:
            return x0
        x0 = x0 - fx.subs(x, x0).evalf() / dfx.subs(x, x0).evalf()
        print ("Iteração {}: x = {}".format(i, x0))
    return None

# Example usage:
x = symbols('x')
funcao = lambda x: x**3 - 4
tol = 1e-5
root = newton_raphson(funcao, 1, tol, 100)
print("Root found:", root)
