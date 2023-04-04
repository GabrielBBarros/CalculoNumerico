import math

def bissecao(f, a, b, eps):
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        raise Exception("A função deve ter sinais opostos nos pontos a e b.")
    while abs(b - a) > eps:
        c = (a + b) / 2
        fc = f(c)
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    return c

# Exemplo de uso:
f = lambda x: math.cos(x) - x
raiz = bissecao(f, 0, 1, 1e-6)
print(raiz)
