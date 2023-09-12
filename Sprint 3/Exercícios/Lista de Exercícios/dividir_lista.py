# Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas: a lista recebida dividida em 3 partes iguais. 
# Teste sua implementação com a lista abaixo

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Define uma função chamada dividir_lista_em_tres_partes que recebe uma lista como entrada.
def dividir_lista_em_tres_partes(lista):
    # Calcula o tamanho total da lista.
    tamanho = len(lista)
    # Calcula o tamanho de cada parte, dividindo o tamanho total por 3.
    tamanho_parte = tamanho // 3
    # Converte as partes da lista em uma string e aa armazena.
    parte1 = str(lista[:tamanho_parte])

    parte2 = str(lista[tamanho_parte:2 * tamanho_parte])

    parte3 = str(lista[2 * tamanho_parte:])
    
    # Combina as três partes em uma única string, separando-as com espaços.
    resultado = parte1 + ' ' + parte2 + ' ' + parte3
    # Retorna a string resultante.
    return resultado

# Teste com a lista fornecida.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
resultado = dividir_lista_em_tres_partes(lista)
# Imprime o resultado.
print(resultado)