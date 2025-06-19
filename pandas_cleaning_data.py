import pandas as pd

df = pd.read_csv('data.csv')

new_df = df.dropna()
print(new_df.to_string())

# df.fillna(130, inplace = True)
# print(df.to_string())

x = df["Calories"].mean()
df.fillna({"Calories": x}, inplace=True)
print(df.to_string())

df['Date'] = pd.to_datetime(df['Date'], format='mixed')
df.dropna(subset=['Date'], inplace = True)
print(df.to_string())

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120
print(df.to_string())

print(df.duplicated())

df.drop_duplicates(inplace = True)
print(df.to_string())