import pandas as pd

df = pd.read_csv("FollowersScrapped.csv", index_col=0, sep=";")

df['date'] = pd.to_datetime(df['last_post_date'], format='%d/%m/%Y', dayfirst=True)
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month

print(df['username'].count())

df = df[df['year'] >= 2023 or df['is_private'] == "True"]

print(df['username'].count())