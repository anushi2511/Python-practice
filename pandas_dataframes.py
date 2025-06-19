import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)
print(df) 
print(df.loc[[0,1]])

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df) 

df = pd.read_csv('data.csv')
print(df)
print(df.to_string()) 
print(df.head(10))
print(df.tail(10))
print(df.info()) 

print(pd.options.display.max_rows)