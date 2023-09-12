# Desenvolva um código Python que lê do teclado nome e a idade atual de uma pessoa.
# Como saída, imprima o ano em que a pessoa completará 100 anos de idade.

import datetime

# Solicita o nome da pessoa
nome = input("Digite seu nome: ")

# Solicita a idade atual da pessoa
idade = int(input("Digite sua idade atual: "))

# Obtém o ano atual
ano_atual = datetime.date.today().year

# Calcula o ano em que a pessoa completará 100 anos
ano_completar_100 = ano_atual + (100 - idade)

print(ano_completar_100)