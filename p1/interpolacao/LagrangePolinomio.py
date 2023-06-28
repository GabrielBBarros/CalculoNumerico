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

x = [1.1, 1.2, 1.3]
n = len(x)
f = lambda x: 4*np.cos(x) - np.e**x
fx = [0.404, 0.338, 0.258]
#for i in range(n): 
#    fx.append(round(f(x[i]), 3))

polinomio = lag(x, fx)
f = np.poly1d(polinomio)
print(f) #imprime o polinomio
print(lag(x, fx))
print(f(1.25)) #imprime o resultado de f(1.85)