from cmath import e, cos
def bisseccao(f, a, b, tol):
    """Método da bissecção para encontrar a raiz da função f(x) no intervalo [a, b] com uma tolerância tol."""
    # Verifica se a função tem sinais opostos nos extremos do intervalo
    if f(a) * f(b) >= 0:
        print("Erro: A função não tem sinais opostos nos extremos do intervalo.")
        return None
    
    # Inicializa o ponto médio e o número de iterações
    c = (a + b) / 2
    i = 0
    
    # Repete até que a diferença entre os extremos do intervalo seja menor do que a tolerância
    while abs(b - a) > tol:
        
        print("Iteração {}: x = {}".format(i, c))  
        
        # Verifica se a raiz está no intervalo [a, c] ou [c, b]
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        
        # Atualiza o ponto médio e o número de iterações
        c = (a + b) / 2
        i += 1
    
    # Retorna o resultado encontrado
    return c

f = lambda x: x**3 + cos(x)
a = 0
b = 1
tol = 1e-5

raiz = bisseccao(f, a, b, tol)
print(raiz)
