import pandas as pd
import time
from joblib import dump
from nltk import word_tokenize
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer, HashingVectorizer, CountVectorizer
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

start_time = time.time()
df = pd.read_csv("sample.csv")

# check integrità dati
df['title'] = df['title'].astype(str)
df['body'] = df['body'].astype(str)
df['title'] = df['title'].fillna(' ')
df['body'] = df['body'].fillna(' ')

# Divisione dei dati in set di training e test
xData = df[['body', 'title', 'tpf', 'bpf', 'sign']]
yData = df['polarity']
xTrain, xTest, yTrain, yTest = train_test_split(
    xData, yData,
    test_size=0.33,
    random_state=42,
    stratify=yData # manteniamo la stessa proporzione del dataset anche nel train e nel test set (50&50)
)

# preprocessamento dei predittori
preprocessor = ColumnTransformer(
    transformers=[
        ('tfidf_body', TfidfVectorizer(strip_accents='unicode', # corpo recensione
                                 tokenizer=word_tokenize,
                                 stop_words='english',
                                 decode_error='ignore',
                                 analyzer='word',
                                 norm='l2',
                                 ngram_range=(1, 2)), 'body'),
        ('tfidf_title', TfidfVectorizer(strip_accents='unicode', # titolo recensione
                                  tokenizer=word_tokenize,
                                  stop_words='english',
                                  decode_error='ignore',
                                  analyzer='word',
                                  norm='l2',
                                  ngram_range=(1, 2)), 'title'),
        ('num', StandardScaler(), ['tpf', 'bpf', 'sign']) # variabili numeriche
    ])

classifier = Pipeline([
    ('preprocessor', preprocessor),
    ('clf', SVC(probability=True, C=10, shrinking=True, kernel="linear")) # iperparametri ottimali risultanti da grid selection
])

# statistiche prestazionali
classifier.fit(xTrain, yTrain)
predicted = classifier.predict(xTest)
cm = confusion_matrix(yTest, predicted)
print(cm)
print(accuracy_score(yTest, predicted))
print(classification_report(yTest, predicted))

# salvataggio modello addestrato
dump(classifier, 'SVM100.joblib')

# monitoraggio tempo di esecuzione
end_time = time.time()
elapsed_time = end_time - start_time
hours, remainder = divmod(elapsed_time, 3600)
minutes, seconds = divmod(remainder, 60)
print(f"Tempo totale di esecuzione: {int(hours)} ore e {int(minutes)} minuti")



