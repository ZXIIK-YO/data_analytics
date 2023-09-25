import csv

# Função para calcular a média das três maiores notas
def calcular_media_tres_maiores(notas):
    return round(sum(notas) / 3, 2)

# Ler o arquivo CSV e armazenar os dados em uma lista de dicionários
dados_estudantes = []
with open('estudantes.csv', newline='') as csvfile:
    leitor = csv.reader(csvfile)
    for linha in leitor:
        nome = linha[0]
        notas = list(map(int, linha[1:]))
        tres_maiores = sorted(notas, reverse=True)[:3]  # Limita a 3 notas e as ordena
        media_tres_maiores = calcular_media_tres_maiores(tres_maiores)
        dados_estudantes.append({'nome': nome, 'notas': tres_maiores, 'media_tres_maiores': media_tres_maiores})

# Processar e ordenar os dados
dados_estudantes = sorted(dados_estudantes, key=lambda x: x['nome'])

# Gerar o relatório
for estudante in dados_estudantes:
    nome = estudante['nome']
    notas = estudante['notas']
    media_tres_maiores = estudante['media_tres_maiores']
    print(f"Nome: {nome} Notas: {notas} Média: {media_tres_maiores}")
