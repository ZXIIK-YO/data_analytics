# Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados.
# Utilize a lista a seguir para testar sua função.

# ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

def remove_duplicatas(lista):
    lista_sem_duplicatas = list(set(lista))
    return lista_sem_duplicatas

# Lista de exemplo
lista_exemplo = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

# Chama a função para remover duplicatas
resultado = remove_duplicatas(lista_exemplo)

# Imprime o resultado
print(resultado)
