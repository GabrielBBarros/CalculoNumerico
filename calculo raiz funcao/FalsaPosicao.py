# O método da falsa posição, também conhecido como método da interpolação linear, é um método iterativo para encontrar
# a raiz de uma função. Ele funciona ao estabelecer uma estimativa inicial para a raiz e, em seguida, calcular o valor da
# função nesse ponto. Com base nesses dois valores, a função é aproximada por uma reta que passa pelos dois pontos
# (estimativa inicial e valor da função calculado). A interseção dessa reta com o eixo x fornece uma nova estimativa para 
# a raiz da função.

# A fórmula para calcular a nova estimativa é dada por:

# x = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))

# onde:

# x é a nova estimativa para a raiz da função.
# x1 é a estimativa anterior para a raiz.
# x0 é a estimativa inicial para a raiz.
# f(x1) é o valor da função no ponto x1.
# f(x0) é o valor da função no ponto x0.
# Esse processo é repetido até que a diferença entre as estimativas consecutivas seja suficientemente pequena 
# (ou seja, até que a raiz seja encontrada com a precisão desejada). O método da falsa posição converge para a raiz 
# da função se a função for contínua e tiver sinais opostos em ambos os lados da raiz.

# É importante observar que o método da falsa posição pode ser lento em alguns casos, especialmente quando a função
# possui regiões planas ou quase planas perto da raiz. Nesses casos, métodos mais avançados, como o método de 
# Newton-Raphson, podem ser mais eficientes.

from cmath import e, cos

def falsa_posicao(funcao, a, b, tolerancia, max_iter):
    """
    Encontra a raiz da função funcao no intervalo [a, b] pelo método da falsa posição.

    Returns:
        Aproximação da raiz da função funcao.
    """
    # Avalia a função nos pontos a e b
    fa, fb = funcao(a), funcao(b)

    # Verifica se a e b já são raízes
    if fa == 0:
        return a
    if fb == 0:
        return b

    # Verifica se o intervalo é adequado
    if fa * fb > 0:
        print("Intervalo inadequado!")
        return None

    # Inicia a iteração
    for i in range(max_iter):
        # Calcula a nova aproximação pelo método da secante
        x = b - fb*(b-a)/(fb-fa)

        # Avalia a função no ponto x
        fx = funcao(x)

        # Imprime o resultado e o numero de iterações
        print("Iteração {}: x = {}".format(i, x))  
        
        # Verifica se a aproximação é suficientemente precisa
        if abs(fx) < tolerancia:
            return x

        # Atualiza os limites do intervalo
        if fa * fx < 0:
            b, fb = x, fx
        else:
            a, fa = x, fx

    # Se atingir o número máximo de iterações sem encontrar uma raiz, retorna None
    print("Número máximo de iterações atingido!")
    return None

funcao = lambda x: x**3 + cos(x)
a = -1
b = 1
tolerancia = 1e-5
max_iter = 100
root = falsa_posicao(funcao,a, b, tolerancia, max_iter)
print("A raiz encontrada é: {}".format(root))