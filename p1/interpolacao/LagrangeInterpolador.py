# Pn = L0*F(x0) + L1*F(x1) + L2*F(x2) + ... + Ln*F(xn)
# L0 = (x - x1)*(x - x2)*...*(x - xn) / (x0 - x1)*(x0 - x2)*...*(x0 - xn) 
import numpy as np

def lagrange(x, fx, xi):
    n = len(x)
    fi = 0
    for i in range(n):
        Li = 1
        for j in range(n):
            if i != j:
                Li *= (xi - x[j])/ (x[i] - x[j])
        fi += fx[i] * Li
        print(f'L{i}(x) = {Li}')
    return fi

x = [1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
n = len(x)
f = lambda x: 4*np.cos(x) - np.e**x
fx = []
for i in range(n): 
    fx.append(round(f(x[i]), 3))
print(f'x = {x}')
print(f'fx = {fx}')
yi = lagrange(x, fx, 1.85)
print(f'\nf(1.85) = {f(1.85)}')