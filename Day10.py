import pandas as pd
df = pd.read_csv('dubai_properties_data.csv')

new_df = df.groupby(['neighborhood'])[['price','size_in_sqft']].mean()
price = new_df.sort_values(by='price', ascending=False).head(1)
size = new_df.sort_values(by='size_in_sqft', ascending=False).head(1)
print(price,size)

#  Palm Jumeirah  4.379435e+06   2084.134831
#  Dubai Festival City  2445000.0        2778.4