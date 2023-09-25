# Lê os números inteiros de um arquivo
with open('number.txt', 'r') as arquivo:
    numeros = [int(line.strip()) for line in arquivo]

# Filtra os números pares
numeros_pares = filter(lambda x: x % 2 == 0, numeros)

# Ordena os números pares em ordem decrescente
numeros_pares_ordenados = sorted(numeros_pares, reverse=True)

# Seleciona os 5 maiores números pares usando map
cinco_maiores_pares = list(map(lambda x: x[1], enumerate(numeros_pares_ordenados[:5], start=1)))

# Calcula a soma dos 5 maiores números pares
soma_cinco_maiores = sum(cinco_maiores_pares)

# Exibe a lista dos 5 maiores números pares e a soma
print(cinco_maiores_pares)
print(soma_cinco_maiores)
