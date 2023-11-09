import pandas as pd

df = pd.read_csv('actors.csv')

# 4. Apresente o nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.
movies_counts = df['#1 Movie'].value_counts()
most_frequent_movies = movies_counts[movies_counts == movies_counts.max()]

print("Nome do(s) filme(s) mais frequente(s):")
for movie, frequency in most_frequent_movies.items():
    print(f"{movie}: {frequency} vezes")