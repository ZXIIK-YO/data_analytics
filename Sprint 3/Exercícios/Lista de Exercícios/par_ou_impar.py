# Escreva um código Python para verificar se três números digitados na entrada padrão são pares ou ímpares. 
# Para cada número, imprima como saída Par: ou Ímpar: e o número correspondente (um linha para cada número lido).
# Importante: Aplique a função range() em seu código.
# Exemplos de saída:
# Par: 2
# Ímpar: 3

# Loop para solicitar três números
for i in range(3):
    numero = int(input("Digite um número: "))
    
    # Verifica se o número é par ou ímpar e imprime a saída correspondente
    if numero % 2 == 0:
        print(f"Par: {numero}")
    else:
        print(f"Ímpar: {numero}")
