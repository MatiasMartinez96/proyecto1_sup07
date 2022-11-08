import pandas as pd

df_netflix = pd.read_csv('../proyecto1_sup07/csv/netflix.csv', sep=',', encoding='latin-1')

df_netflix.head()

df_netflix.dtypes

df_netflix[['date_added']] = df_netflix[['date_added']].apply(pd.to_datetime)

df_netflix = df_netflix.sort_values(by=['date_added'])

df_netflix = df_netflix.replace({'director':'Not Given'}, None)


mask2019 = df_netflix['release_year'] == 2019
df2019 = df_netflix[mask2019]

mask2020 = df_netflix['release_year'] == 2020
df2020 = df_netflix[mask2020]

mask2021 = df_netflix['release_year'] == 2021
df2021 = df_netflix[mask2021]


dict19 = df2019.reset_index().to_dict(orient="index")

dict20 = df2020.reset_index().to_dict(orient="index")

dict21 = df2021.reset_index().to_dict(orient="index")