"""
A fórmula do trapézio é um método de integração numérica utilizado para estimar o valor de uma integral definida. 
Ela é baseada na aproximação da curva da função integranda por uma série de trapézios.

A fórmula geral do trapézio para uma função f(x) integrada no intervalo [a, b] é a seguinte:

∫[a,b] f(x) dx ≈ (b - a) * [f(a) + f(b)] / 2

Nessa fórmula, a e b são os limites do intervalo de integração, f(a) e f(b) são os valores da função nos extremos do intervalo, 
e o termo (b - a) / 2 é o tamanho da base do trapézio.

Para obter uma estimativa mais precisa da integral, é possível dividir o intervalo [a, b] em vários subintervalos e aplicar a 
fórmula do trapézio para cada subintervalo, somando os resultados individuais. Isso é conhecido como regra do trapézio composta.

A fórmula do trapézio é um método simples de integração numérica, mas pode não ser tão preciso para funções com curvas acentuadas. 
Existem outros métodos mais avançados, como a regra de Simpson, que proporcionam resultados mais precisos em certas situações.
"""


def trapezio(f, a, b, n):
    """
    Calcula uma aproximação da integral definida de f(x) no intervalo [a, b] usando a fórmula do trapézio.

    Parâmetros:
    - f: função a ser integrada
    - a: limite inferior do intervalo de integração
    - b: limite superior do intervalo de integração
    - n: número de subintervalos (quanto maior, mais precisa a estimativa)

    Retorna:
    - A aproximação da integral definida de f(x) no intervalo [a, b]
    """
    h = (b - a) / n  # tamanho do subintervalo
    soma = f(a) + f(b)  # soma dos extremos

    # Soma dos valores da função nos pontos internos do intervalo
    for i in range(1, n):
        x = a + i * h
        soma += 2 * f(x)

    # Calcula a aproximação da integral
    integral = (h / 2) * soma
    return integral

# Exemplo de uso da função
def f(x):
    return x**2  # Função a ser integrada

a = 0  # Limite inferior do intervalo de integração
b = 1  # Limite superior do intervalo de integração
n = 1000  # Número de subintervalos

aproximacao = trapezio(f, a, b, n)
print("Aproximação da integral:", aproximacao)
