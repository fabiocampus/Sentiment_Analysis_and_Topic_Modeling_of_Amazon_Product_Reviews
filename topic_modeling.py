import pandas as pd
from sklearn.decomposition import NMF, LatentDirichletAllocation
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

# importiamo i bodies dei commenti dal nostro file csv
df = pd.read_csv("mac_edited.csv", encoding='utf-8', low_memory=None)
comments_body = df[["body"]]

#NMF è basato sulla TfIdf
tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, stop_words="english")
tfidf = tfidf_vectorizer.fit_transform(comments_body['body'])
tfidf_feature_names = tfidf_vectorizer.get_feature_names_out()

#LDA usa solo il conteggio dei token in quanto basato su modello probabilistico
tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words="english")
tf = tf_vectorizer.fit_transform(comments_body['body'])
tf_feature_names = tf_vectorizer.get_feature_names_out()

#run NMF
#(i parametri alpha li uso se voglio regolarizzare per evitare l'overfitting)
nmf = NMF(n_components=10, random_state=1, l1_ratio=.5, init="nndsvd") .fit(tfidf)

#run LDA
lda = LatentDirichletAllocation(n_components=10, learning_method="online", learning_offset=50., random_state=0).fit(tf)

def display_topics(model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        for i in topic.argsort()[:-no_top_words - 1:-1]:
            print(topic_idx)
            print(" ".join([feature_names[i]]))

display_topics(nmf, tfidf_feature_names, 1)
display_topics(lda, tf_feature_names, 1)


