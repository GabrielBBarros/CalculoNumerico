# O método da bissecção é um algoritmo utilizado para encontrar raízes de uma função em um intervalo específico.
# O método envolve dividir o intervalo ao meio repetidamente até que a raiz seja encontrada com a precisão desejada.

# 1- Dado um intervalo inicial [a, b] no qual a função tem uma mudança de sinal (ou seja, a função muda de positiva para negativa ou vice-versa), verifique se a função tem uma raiz dentro desse intervalo. Caso contrário, o método não pode ser aplicado.

# 2- Divida o intervalo ao meio, calculando o ponto médio c = (a + b) / 2.

# 3- Avalie o valor da função no ponto médio, ou seja, calcule f(c).

# 4- Verifique se f(c) é igual a zero ou se é suficientemente próximo de zero, dentro de uma tolerância predefinida. Se for, c é considerado uma raiz aproximada e o processo é encerrado.

# 5- Caso contrário, verifique em qual metade do intervalo a função tem uma mudança de sinal. Se f(a) e f(c) têm sinais opostos, a raiz está no intervalo [a, c]. Caso contrário, a raiz está no intervalo [c, b].

# 6- Repita os passos de 2 a 5 até encontrar uma raiz aproximada com a precisão desejada.

#O método da bissecção é um método iterativo que garante a convergência para uma raiz, desde que a função seja contínua no intervalo considerado e tenha uma mudança de sinal dentro dele. No entanto, o método pode ser relativamente lento em comparação com outros métodos de otimização, especialmente para funções complexas ou intervalos grandes.

from sympy import symbols, diff, cos

def bisseccao(f, a, b, tol):
    """Método da bissecção para encontrar a raiz da função f(x) no intervalo [a, b] com uma tolerância tol."""
    # Verifica se a função tem sinais opostos nos extremos do intervalo
    if f(a)*f(b) >= 0:
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


x = symbols('x')
f = lambda x: x**3 - 4

a = 1
b = 3
tol = 1e-5

raiz = bisseccao(f, a, b, tol)
print(raiz)
