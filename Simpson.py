def simpsons_rule(f, a, b, n):
    """Calcula a integral de uma função usando a regra de Simpson.

    Args:
        f: Função a ser integrada.
        a: Limite inferior do intervalo de integração.
        b: Limite superior do intervalo de integração.
        n: Número de subintervalos para dividir o intervalo [a, b]. Deve ser um número par.

    Returns:
        Valor aproximado da integral definida de f no intervalo [a, b].
    """
    if n % 2 != 0:
        raise ValueError("O número de subintervalos deve ser par.")
    
    h = (b - a) / n  # Tamanho de cada subintervalo
    x = a
    integral = f(x)  # Contribuição inicial do limite inferior
    for i in range(1, n):
        x += h
        coefficient = 2 if i % 2 == 0 else 4
        integral += coefficient * f(x)  # Contribuição dos pontos internos
    integral += f(b)  # Contribuição do limite superior
    integral *= h / 3  # Multiplica pelo tamanho do intervalo
    return integral


def f(x):
    return x ** 2

a = 0
b = 1
n = 100

integral = simpsons_rule(f, a, b, n)
print("Integral aproximada:", integral)
