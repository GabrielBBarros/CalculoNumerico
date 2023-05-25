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
f  = lambda x: -np.sin(x)**2 + np.cos(x)**2
max = 2 #maior valor absoluto dos pointos x
x0 = 1.25 #ponto a ser interpolado
x = np.array([0.404, 0.338, 0.258]) #pontos conhecidos de x
n = 2 #grau do polinomio
print(calculaErro(f, x0, x, max, n))