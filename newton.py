import numpy as np
from sympy import * 

def newton(x0, func):
    x = x0
    fx0 = func(x0)
    dx0 = np.derivative(func, x0)
    
    