def falsa_posicao(funcao, a, b, tolerancia, max_iter):
    """
    Encontra a raiz da função funcao no intervalo [a, b] pelo método da falsa posição.

    Args:
        funcao: função a ser avaliada
        a, b: limites do intervalo
        tolerancia: tolerância para o resultado
        max_iter: número máximo de iterações

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



funcao = lambda x: x**2 - 2
a = 1
b = 2
tolerancia = 1e-20
max_iter = 100
root = falsa_posicao(funcao,a, b, tolerancia, max_iter)
print("A raiz encontrada é: {}".format(root))