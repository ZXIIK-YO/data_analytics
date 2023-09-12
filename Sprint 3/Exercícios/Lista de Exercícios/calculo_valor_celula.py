# Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada na célula abaixo:
# Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada!
# import random 
# # amostra aleatoriamente 50 números do intervalo 0...500
# random_list = random.sample(range(500),50)
# Use as variáveis abaixo para representar cada operação matemática:
# mediana
# media
# valor_minimo 
# valor_maximo 
# Importante: Esperamos que você utilize as funções abaixo em seu código:
# random
# max
# min
# sum

import random

random_list = random.sample(range(500), 50)

mediana = 0
media = 0
valor_minimo = 0
valor_maximo = 0

# Ordena a lista
random_list.sort()

# Calcula o valor mínimo
valor_minimo = min(random_list)

# Calcula o valor máximo
valor_maximo = max(random_list)

# Calcula a soma de todos os valores
soma_valores = sum(random_list)

# Calcula a média
media = soma_valores / len(random_list)

# Calcula a mediana (a mediana é o valor do meio quando a lista está ordenada)
tamanho_lista = len(random_list)
if tamanho_lista % 2 == 0:
    # Se a lista tiver um número par de elementos, a mediana é a média dos dois valores do meio
    indice_meio1 = tamanho_lista // 2
    indice_meio2 = indice_meio1 - 1
    mediana = (random_list[indice_meio1] + random_list[indice_meio2]) / 2
else:
    # Se a lista tiver um número ímpar de elementos, a mediana é o valor do meio
    indice_meio = tamanho_lista // 2
    mediana = random_list[indice_meio]

# Formata a saída de acordo com o esperado
resultado_formatado = f'Media: {media:.2f}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}\n'

# Imprime o resultado formatado
print(resultado_formatado, end='')
