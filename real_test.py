import joblib
from sklearn.metrics import accuracy_score
import pandas as pd
import time

start_time = time.time()

# Carica il modello dal file
loaded_model = joblib.load('SVM100.joblib')

# Carica il nuovo set di dati
new_data = pd.read_csv("data.fe.csv")

# Estrai le etichette corrette dalla colonna 'label'
new_labels = new_data['polarity']

# Rimuovi la colonna 'label' dal nuovo set di dati
new_data = new_data.drop('polarity', axis=1)

# Utilizza il modello caricato su un nuovo set di dati
predictions = loaded_model.predict(new_data)

# Calcola l'accuratezza del modello
accuracy = accuracy_score(new_labels, predictions)

# Stampa l'accuratezza del modello
print(f'L\'accuratezza del modello sui nuovi dati è: {accuracy}')

# monitoraggio tempo di esecuzione
end_time = time.time()
elapsed_time = end_time - start_time
hours, remainder = divmod(elapsed_time, 3600)
minutes, seconds = divmod(remainder, 60)
print(f"Tempo totale di esecuzione: {int(hours)} ore e {int(minutes)} minuti")
