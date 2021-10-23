import pandas as pd


df = pd.read_csv("/Users/ahmed/Desktop/coronaProject/time_series_covid19_confirmed_global.csv")

df = df.drop(columns=['Province/State', 'Lat', 'Long'])
df_t = df.T

df_t.to_csv("out.csv")