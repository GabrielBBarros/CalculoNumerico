# O método das secantes é um algoritmo numérico utilizado para encontrar raízes de equações não lineares.
# Ele é uma variação do método da bissecção, porém, em vez de utilizar apenas dois pontos para estimar a raiz,
# o método das secantes utiliza uma reta secante formada por dois pontos próximos na curva da função.

# O algoritmo começa com dois valores iniciais, x0 e x1, que são escolhidos próximos o suficiente à raiz que se
# deseja encontrar. A partir desses pontos, é construída uma reta secante que intersecta o eixo x. A interseção
# dessa reta com o eixo x dá uma nova aproximação para a raiz, x2.

# Em seguida, o processo é repetido, utilizando x1 e x2 para construir uma nova reta secante e encontrar x3, e
# assim por diante. A cada iteração, a reta secante é ajustada com base nas aproximações anteriores, e a interseção
# com o eixo x fornece uma nova estimativa para a raiz.

# O método das secantes continua iterando até que a diferença entre duas aproximações consecutivas seja menor do que
# uma tolerância pré-definida, ou até que o número máximo de iterações seja atingido.

# A principal vantagem do método das secantes é que ele pode convergir mais rapidamente do que o método da bissecção,
# uma vez que utiliza informações adicionais da curva da função. No entanto, o método das secantes pode ser sensível
# à escolha dos pontos iniciais e pode não convergir em alguns casos. Portanto, é necessário tomar cuidado ao utilizá-lo
# e verificar a convergência adequada.

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