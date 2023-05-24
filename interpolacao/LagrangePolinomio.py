import numpy as np
def lag(x, y):
  x = np.array(x)
  y = np.array(y)
  poly = []
  n = len(x)
  #Calcula o polinomio
  for i in range(n): 
    Li = [1.]
    di = 1.
    #Calcula Li
    for j in range(n):
      if(j == i):
        continue
      Li = np.polymul(Li, [1, -x[j]])
      di *= x[i] - x[j]
    Li /= di
    Li *= y[i]
    poly.append(Li)
  n = len(poly[0])
  # Converter a lista de polinômios em um array do NumPy
  poly = np.array(poly)
  # Somar os coeficientes ao longo do eixo 0 (colunas)
  poly = np.sum(poly, axis=0)
  return poly

x = [1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
n = len(x)
f = lambda x: 4*np.cos(x) - np.e**x
fx = []
for i in range(n): 
    fx.append(round(f(x[i]), 3))

polinomio = lag(x, fx)
f = np.poly1d(polinomio)
print(lag(x, fx))
print(f(1.85))