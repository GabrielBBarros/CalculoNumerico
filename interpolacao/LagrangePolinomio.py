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

a = [1, 2, 3]
b = [1, 8, 27]
polinomio = lag(a, b)
f = np.poly1d(polinomio)
print(lag(a, b))
print(f(4))