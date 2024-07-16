import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

df = pd.read_csv("mac_edited.csv", encoding='utf-8', low_memory=None)

# Ottieni tutti i valori univoci della colonna 'location'
different_locations = df["location"].unique()
print(different_locations)

# Ora vogliamo contare quanti commenti ci sono per ciascuna location,e rappresentarli graficamente
count_loc = df["location"].value_counts()
print(count_loc)
count_loc.plot(kind='bar')
plt.show()

# Ora vogliamo sapere quali sono i 10 commenti che sono stati più d'aiuto per le persone, e metterli in un csv
df_sorted = df.sort_values(by="helpful", ascending=False)
top_10 = df_sorted.head(10)
#top_10.to_csv("mac_top10_help.csv", encoding="utf-8", index=False)


# Selezioniamo le stopwords inglesi
stop_words = set(stopwords.words('english'))
# Individuiamo i 10 aggettivi più utilizzati nei titoli dei commenti
titles = ' '.join(df["title"])
words_title = word_tokenize(titles)
filtered_words_title = [word.lower() for word in words_title if word.isalpha() and word.lower() not in stop_words]
tagged_title = nltk.pos_tag(filtered_words_title)
adj_title = [word.lower() for word, pos in tagged_title if pos == 'JJ']
fdist_title = FreqDist(adj_title)
print(fdist_title.most_common(10))
# Individuiamo i 10 aggettivi più utilizzati nel body dei commenti
bodies = ' '.join(df["body"])
words_body = word_tokenize(bodies)
filtered_words_body = [word.lower() for word in words_body if word.isalpha() and word.lower() not in stop_words]
tagged_body = nltk.pos_tag(filtered_words_body)
adj_body = [word.lower() for word, pos in tagged_body if pos == 'JJ']
fdist_body = FreqDist(adj_body)
print(fdist_body.most_common(10))

# Vogliamo inoltre sapere quanti sono i commenti che son stati valutati con cinque stelle
count_5star = (df["rating"]==5.0).sum()
print(f"Ci sono {count_5star} commenti valutati con 5.0")
