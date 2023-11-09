import pandas as pd

df = pd.read_csv('actors.csv')

# 3. Apresente o nome do ator/atriz com a maior média por filme.
df['Average per Movie'] = df['Total Gross'] / df['Number of Movies']
actor_with_highest_average = df[df['Average per Movie'] == df['Average per Movie'].max()]
highest_average = actor_with_highest_average.iloc[0]['Average per Movie']
print("Ator/atriz com a maior média por filme:", actor_with_highest_average.iloc[0]['Actor'])
print("Média por filme:", highest_average)