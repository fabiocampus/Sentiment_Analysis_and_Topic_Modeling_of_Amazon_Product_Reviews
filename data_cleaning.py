import pandas as pd
import re

# apriamo i tre dataset
df1 = pd.read_csv("amz_mac_us.csv", encoding='utf-8', low_memory=None)
df2 = pd.read_csv("amz_mac_uk.csv", encoding='utf-8', low_memory=None)
df3 = pd.read_csv("amz_mac_in.csv", encoding='utf-8', low_memory=None)

# li uniamo
df = pd.concat([df1, df2, df3])


# estraiamo la località

location = []
for i in df["location_date"]:

    match = re.search(r'in (.*?) on', i)
    l = match.group(1)
    location.append(l)


# estraiamo il numero di persone che
# hanno reputato utile la recensione

helpful = []
for i in df["helpful"]:

    i = str(i)
    if re.search(r'(.*?) people', i):
        match = re.search(r'(.*?) people', i)
        h = match.group(1)
        h = h.replace(",","")
        helpful.append(int(h))
    elif re.search(r'One person', i):
        helpful.append(1)
    else:
        helpful.append(0)


# etichettiamo bene le recensioni verificate da quelle non verificate

verified = []
for i in df.verified:

    if i == "Verified Purchase":
        i = True
    else:
        i = False
    verified.append(i)


# sistemiamo il rating

rating = []
for i in df["rating"]:

    i = str(i)
    if re.search(r'(.*?) out', i):
        match = re.search(r'(.*?) out', i)
        r = match.group(1)
        rating.append(float(r))
    else:
        rating.append(0)


# correggiamo eventuale contenuto mancante o
# incompatabile nel corpo delle recensioni

body_review = []
for i in df.body_review:

    if type(i) != str:
        i = ""
        body_review.append(i)
    else:
        body_review.append(i)


# correggiamo eventuale contenuto mancante o
# incompatabile nel titolo delle recensioni

title_review = []
for i in df.title_review:

    if type(i) != str:
        i = ""
        title_review.append(i)
    else:
        title_review.append(i)


# eliminiamo le vecchie colonne e le sostituiamo
# con nuove colonne coi valori appena rielaborati

df = df.drop('title_review', axis=1)
df['title_review'] = title_review

df = df.drop('body_review', axis=1)
df['body_review'] = body_review

df = df.drop('rating', axis=1)
df['rating'] = rating

df = df.drop('helpful', axis=1)
df['helpful'] = helpful

df = df.drop('location_date', axis=1)
df['location'] = location

df = df.drop('verified', axis=1)
df['verified'] = verified

df = df.drop('Unnamed: 0', axis=1)


# esportiamo il dataframe editato in csv e xlsx
df.to_csv("mac_edited.csv", encoding="utf-8", index=False)
df.to_excel('mac_edited.xlsx', index=False)
