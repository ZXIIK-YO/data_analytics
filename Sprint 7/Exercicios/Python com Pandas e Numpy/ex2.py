import pandas as pd

# 2. Apresente a média da coluna contendo o número de filmes.
df = pd.read_csv('actors.csv')
average_number_of_movies = df['Number of Movies'].mean()
print("Média do número de filmes:", average_number_of_movies)