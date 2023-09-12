import csv

# Abra o arquivo CSV para leitura
with open('actors.csv', 'r', newline='', encoding='utf-8') as csvfile:
    # Crie um objeto de leitura CSV
    csvreader = csv.reader(csvfile)

    # Pule o cabeçalho (se houver)
    next(csvreader)

    # Inicialize uma lista para armazenar os dados
    data = []

    # Itere sobre as linhas do arquivo CSV e armazene os dados em uma lista
    for row in csvreader:
        actor = row[0]
        total_gross = float(row[1])
        number_of_movies = int(row[2])
        average_per_movie = float(row[3])
        top_movie = row[4]
        gross = float(row[5])
        
        # Crie uma tupla com os dados e adicione à lista
        actor_data = (actor, total_gross, number_of_movies, average_per_movie, top_movie, gross)
        data.append(actor_data)

# Agora você tem os dados do arquivo CSV armazenados na lista 'data'

# #1.
# # Encontre o ator com o maior número de filmes
# actor_with_most_movies = max(data, key=lambda x: x[2])
# # Extrai o nome do ator e a quantidade de filmes
# actor_name, number_of_movies = actor_with_most_movies[0], actor_with_most_movies[2]
# print(f"{actor_name} - {number_of_movies} filmes")


# #2.
# # Calcula a média da coluna Gross (receita bruta dos principais filmes)
# gross_values = [row[5] for row in data]
# average_gross = sum(gross_values) / len(gross_values)
# print(f"Média de Receita Bruta dos Principais Filmes: ${average_gross:.2f} milhões de dólares")


# #3.
# # Encontra o ator com a maior média de receita por filme
# actor_with_highest_average = max(data, key=lambda x: x[3])
# # Extrai o nome do ator e a média
# actor_name, average_per_movie = actor_with_highest_average[0], actor_with_highest_average[3]
# print(f"{actor_name} - Média de Receita Bruta por Filme: ${average_per_movie:.2f} milhões de dólares")


# #4.
# from collections import Counter

# # Extrai os filmes da coluna #1 Movie
# movies = [row[4] for row in data]
# # Conta a frequência de cada filme
# movie_counts = Counter(movies)
# # Ordena os filmes pela contagem em ordem decrescente e, em segundo nível, pelo nome do filme
# sorted_movies = sorted(movie_counts.items(), key=lambda x: (-x[1], x[0]))

# # Escreve os resultados em um arquivo
# with open('filmes_mais_frequentes.txt', 'w') as file:
#     for idx, (movie, count) in enumerate(sorted_movies, start=1):
#         file.write(f"{idx} - O filme {movie} aparece {count} vez(es) no dataset\n")

# # Imprime os resultados na saída padrão
# for idx, (movie, count) in enumerate(sorted_movies, start=1):
#     print(f"{idx} - O filme {movie} aparece {count} vez(es) no dataset")


# # 5.
# # Ordena os atores pela receita bruta em ordem decrescente
# actors_sorted_by_gross = sorted(data, key=lambda x: -x[1])

# # Escreve os resultados em um arquivo
# with open('atores_por_receita.txt', 'w') as file:
#     for actor in actors_sorted_by_gross:
#         file.write(f"{actor[0]} - ${actor[1]:.2f} milhões de dólares\n")

# # Imprime os resultados na saída padrão
# for actor in actors_sorted_by_gross:
#     print(f"{actor[0]} - ${actor[1]:.2f} milhões de dólares")
