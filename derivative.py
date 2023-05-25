import sympy as sp 
def derivative(func, grau = 1):
    x = sp.symbols('x')
    dfx = sp.diff(func, x, grau)
    return dfx

func = ('sin(x)*cos(x)')
print(derivative(func))