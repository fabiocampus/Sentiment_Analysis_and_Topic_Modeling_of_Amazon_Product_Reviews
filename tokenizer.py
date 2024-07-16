# import pandas as pd
# import spacy
# from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from nltk.tokenize import word_tokenize

# df = pd.read_csv("kaggle.csv", encoding='utf-8', low_memory=None)
#
# # Carica il modello di lingua Spacy
# nlp = spacy.load('en_core_web_sm')
#
# # Crea una funzione per tokenizzare il testo utilizzando Spacy
# def spacy_tokenizer(text):
#     # Elabora il testo con Spacy
#     doc = nlp(text)
#     # Restituisce una lista di token in minuscolo
#     return [token.text.lower() for token in doc]
#
# # Crea un dataset di esempio con recensioni e etichette di sentimento
# reviews = df["body"].to_list()
# sentiments = df["polarity"].to_list # 1 = negativo, 2 = positivo
#
# # Crea un CountVectorizer utilizzando la funzione di tokenizzazione di Spacy
# vectorizer = CountVectorizer(tokenizer=spacy_tokenizer)
#
# # Trasforma le recensioni in una matrice di conteggi di parole
# X = vectorizer.fit_transform(reviews)
#
# # # Addestra un modello SVM sulle recensioni tokenizzate e le etichette di sentimento
# # clf = LinearSVC()
# # clf.fit(X, sentiments)
# #
# # # Prevedi il sentimento di una nuova recensione
# # new_review = 'This product is not bad'
# # X_new = vectorizer.transform([new_review])
# # predicted_sentiment = clf.predict(X_new)[0]
# # print(f'Predicted sentiment: {predicted_sentiment}')

df = pd.read_csv("kaggle.csv", encoding='utf-8', low_memory=None)

xData = df["body"].to_list()
yData = df["polarity"].to_list()
xTrain, xTest, yTrain, yTest = train_test_split(
 xData, yData,
 test_size=0.33,
 random_state=42
)

classifier = Pipeline([
 ('feature_vect', TfidfVectorizer(strip_accents='unicode',
 tokenizer=word_tokenize,
 stop_words='english',
 decode_error='ignore',
 analyzer='word',
 norm='l2',
 ngram_range=(1, 2)
 )),
 ('clf', SVC(probability=True, C=10, shrinking=True, kernel='linear'))
])

classifier.fit(xTrain, yTrain)
predicted = classifier.predict(xTest)
print(accuracy_score(yTest, predicted))
print(precision_recall_fscore_support(yTest, predicted))
print(classification_report(yTest, predicted))

