import pandas as pd
df = pd.read_csv('dubai_properties_data.csv')
df.head()
new_df = df.groupby(['neighborhood']).agg({'price' : ['max','min']})
total = new_df['price']['max'] - new_df['price']['min']
total.sort_values(ascending=False).head(5)