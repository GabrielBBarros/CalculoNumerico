#Importação do numpy com euler e cosseno
from numpy import e, cos
#Função e os parametros
def falsa_posicao(funcao, a, b, tolerancia, intercacao_maxima):
 
    #Auxiliares
    aux_fa = funcao(a)
    aux_fb = funcao(b)

    #Verifica se um dos valores dentro da função são negativos
    if (aux_fa * aux_fb) > 0:
        print("Intervalo com algum valor negativo")
        #Falha
        return None

    #Laço até o máximo de interação
    for i in range(intercacao_maxima):
        # Método da Secante
        x = b - aux_fb*(b-a)/(aux_fb-aux_fa)
        #Coloca x na função e armazena em aux_fx
        aux_fx = funcao(x)
        #Imprime iteração
        print("Iteração {}: x = {}".format(i, x))  
        #Verificação se é menor que a tolerancia
        if abs(aux_fx) < tolerancia:
            return x
        #Atualização
        if aux_fa * aux_fx < 0:
            b = x
            aux_fb = aux_fx
        else:
            a = x
            aux_fa = aux_fx
    print("Limite de interação!")
    #Falha
    return None

#Função
funcao = lambda x: x**3 + cos(x)
#Primeiro valor
a = -10
#Segundo valor
b = 10
#Tolerancia
tolerancia = 1e-5
#Maxima interação
intercacao_maxima = 100
#Chama a função
resultado = falsa_posicao(funcao,a, b, tolerancia, intercacao_maxima)
#Valor da raiz
print("A raiz encontrada é: {}".format(resultado))
