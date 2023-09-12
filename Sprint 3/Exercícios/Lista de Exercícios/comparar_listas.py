# Considere as duas listas abaixo:

# a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Escreva um programa para avaliar o que ambas as listas têm em comum (sem repetições), imprimindo a lista de valores da interseção na saída padrão.
# Importante:  Esperamos que você utilize o construtor set() em seu código.

a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Converte as listas em conjuntos
conjunto_a = set(a)
conjunto_b = set(b)

# Calcula a interseção entre os conjuntos
intersecao = conjunto_a.intersection(conjunto_b)

# Converte o resultado de volta para uma lista
resultado = list(intersecao)

# Imprime a lista de valores da interseção
print(resultado)
