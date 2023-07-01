import numpy as np

def f(x):
    return (np.exp(np.sin(x)))

fx = f(0.001)
fy = f(-0.001)
print("fx = ", fx , "fy = ", fy)
print("conta: ", (fx - fy)/0.002)