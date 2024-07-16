import pandas as pd

df = pd.read_csv("mac_edited.csv", encoding='utf-8', low_memory=None)

df = df[df["verified"] == True]
df = df.drop('verified', axis=1)

ll = []
for i in df["body"]:
    l = len(i)
    ll.append(l)

df['len'] = ll

print(df["len"].mean())
print(df["len"].quantile(.75))

# df = df[df["helpful"] > 0]
df = df[df["len"] < 250]

df.to_csv("mac_filtered.csv", encoding="utf-8", index=False)
df.to_excel('mac_filtered.xlsx', index=False)

print(len(df))