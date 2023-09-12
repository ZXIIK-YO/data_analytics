# Escreva um código Python para imprimir todos os números primos entre 1 até 100. 
# Lembre-se que você deverá desenvolver o cálculo que identifica se um número é primo ou não.
# Importante: Aplique a função range().

# Função que verifica se um número é primo ou não
def eh_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

# Loop para verificar números primos de 1 a 100
for numero in range(1, 101):
    if eh_primo(numero):
        print(numero)
