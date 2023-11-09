import pandas as pd

# 1. Identifique o ator/atriz com o maior número de filmes e o respectivo número de filmes.
df = pd.read_csv('actors.csv')
actor_with_most_movies = df[df['Number of Movies'] == df['Number of Movies'].max()]
max_movies = actor_with_most_movies.iloc[0]['Number of Movies']
print("Ator/atriz com o maior número de filmes:", actor_with_most_movies.iloc[0]['Actor'])
print("Número de filmes:", max_movies)
