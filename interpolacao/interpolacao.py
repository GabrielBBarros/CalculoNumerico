def lagrange_interpolation(x, y, xi):
    n = len(x)
    yi = 0.0
    
    for i in range(n):
        Li = 1.0
        for j in range(n):
            if i != j:
                Li *= (xi - x[j]) / (x[i] - x[j])


        yi += y[i] * Li

        print(f'L{i}(x) = {Li}')
    
    return yi


# Exemplo de pontos conhecidos
x = [1, 2, 3]
y = [1, 4, 9]

# Valor a ser interpolado
xi = 2.5

# Realiza a interpolação
result = lagrange_interpolation(x, y, xi)

print(f'\nO valor interpolado em xi = {xi} é yi = {result}')
