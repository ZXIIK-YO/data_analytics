# Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles. 
# Depois imprima a soma dos valores.

# A string deve ter valor  "1,3,4,6,10,76"

def soma_string_numeros(string_numeros):
    numeros = string_numeros.split(',')  # Divide a string em uma lista de números
    soma = sum(map(int, numeros))  # Converte os números para inteiros e calcula a soma
    return soma

# String de números
string_numeros = "1,3,4,6,10,76"

# Calcula a soma e imprime
soma = soma_string_numeros(string_numeros)
print(soma)


