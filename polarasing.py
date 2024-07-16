import pandas as pd

df = pd.read_csv("data.csv", encoding='utf-8', low_memory=None)

# Rimuovi le righe corrispondenti alle recensioni a 3 stelle
# df = df[df['rating'] != 3]

# Crea una nuova colonna 'polarity' basata sui valori della colonna 'rating'
df['polarity'] = df['rating'].apply(lambda x: 1 if x > 2 else 0)

# Salva il nuovo DataFrame in un file CSV
df.to_csv("p.data.csv", index=False)