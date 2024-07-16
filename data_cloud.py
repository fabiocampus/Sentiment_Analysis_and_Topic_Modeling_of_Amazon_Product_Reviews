import string
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# nltk.download('punkt')
# nltk.download('stopwords')

df = pd.read_csv("mac_edited.csv", encoding='utf-8', low_memory=None)

titles_string = ""
for i in df.title:
    i = str(i)
    i = i.lower()
    titles_string += i

translator = str.maketrans('', '', string.punctuation)
titles_string = titles_string.translate(translator)
stop_words = set(stopwords.words('english')).union(set("’"))
word_tokens = word_tokenize(titles_string)
filtered_sentence_t = [w for w in word_tokens if not w.lower() in stop_words]

fq_t = nltk.FreqDist(filtered_sentence_t)
common_t = (fq_t.most_common(30))

bodies_string = ""
for i in df.body:
    i = str(i)
    i = i.lower()
    bodies_string += i

translator = str.maketrans('', '', string.punctuation)
bodies_string = bodies_string.translate(translator)
stop_words = set(stopwords.words('english')).union(set("’"))
word_tokens = word_tokenize(bodies_string)
filtered_sentence_b = [w for w in word_tokens if not w.lower() in stop_words]

fq_b = nltk.FreqDist(filtered_sentence_b)
common_b = (fq_b.most_common(30))

# common_set_t = set()
# for i in common_t:
#     common_set_t.add(i[0])
#
# common_set_b = set()
# for i in common_b:
#     common_set_b.add(i[0])
#
# print(common_set_t.intersection(common_set_b))
# print(common_set_t.difference(common_set_b))
# print(common_set_b.difference(common_set_t))

from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt

# Creazione del dizionario
word_freq = dict([common_t[3]]+common_t[5:])

# Creazione del WordCloud
wc = WordCloud(width=1920, height=1080, max_words=100, background_color='white')
wc.generate_from_frequencies(word_freq)

# Visualizzazione del WordCloud
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()

# Creazione del dizionario
word_freq = dict([common_b[3]]+common_b[5:])

# Creazione del WordCloud
wc = WordCloud(width=1920, height=1080, max_words=100, background_color='white')
wc.generate_from_frequencies(word_freq)

# Visualizzazione del WordCloud
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
