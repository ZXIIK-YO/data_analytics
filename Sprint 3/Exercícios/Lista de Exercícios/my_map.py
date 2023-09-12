# Implemente a função my_map(list, f) que recebe uma lista como primeiro argumento e uma função como segundo argumento. 
# Esta função aplica a função recebida para cada elemento da lista recebida e retorna o resultado em uma nova lista.

# Teste sua função com a lista de entrada [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] e com uma função que potência de 2 para cada elemento.

def my_map(lista, funcao):
    # Inicializa uma lista vazia para armazenar os resultados
    resultados = []
    
    # Itera sobre cada elemento da lista e aplica a função
    for elemento in lista:
        resultado = funcao(elemento)
        resultados.append(resultado)
    
    return resultados

# Função para calcular a potência de 2 de um número
def potencia_de_2(numero):
    return numero ** 2

# Lista de entrada
lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Aplica a função potencia_de_2 a cada elemento da lista usando my_map
resultados = my_map(lista_de_numeros, potencia_de_2)

# Imprime os resultados
print(resultados)
