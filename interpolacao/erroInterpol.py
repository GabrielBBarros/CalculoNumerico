import numpy as np
import math as mt
def calculaErro(derF, x0, x, max, n):
  fatN =  1/mt.factorial(n+1)
  valorDerivada = np.abs(derF(max))
  it = len(x)
  mul = 1.
  for i in range(it):
    mul *= np.abs((x0 - x[i]))
  return fatN*valorDerivada*mul

#@title Aplicação erro interpolador
f  = lambda x: np.cos(x)*4 - np.exp(x)
max = 2 
x0 = 1.85
x = np.array([1.7, 1.8, 1.9, 2.0])
n = 3
print(calculaErro(f, x0, x, max, n))