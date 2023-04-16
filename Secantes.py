from cmath import e, cos

def secant_method(x0, x1, tol, max_iter):
    i = 0
    while i < max_iter:
        x2 = x1 - funcao(x1) * (x1 - x0) / (funcao(x1) - funcao(x0))
        if abs(x2 - x1) < tol:
            return x2
        x0 = x1
        x1 = x2
        print("Iteração {}: x = {}".format(i, x2))
        i += 1
    print("O método das secantes não convergiu após {} iterações.".format(max_iter))

# Exemplo de uso
funcao = lambda x: x**3 + cos(x)
x0 = -1
x1 = 1
tol = 1e-5
max_iter = 100
root = secant_method(x0, x1, tol, max_iter)
print("A raiz encontrada é: {}".format(root))