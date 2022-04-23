import pandas as pd
df = pd.read_csv('aus_weather.csv')
df.head()
seasons_filter = (df['season'] == 'winter') | (df['season'] == 'summer')
filtered = df[seasons_filter]
grouped = filtered.groupby(['season', 'Location'])[['Temp9am']].mean()
# print(grouped)
unstacked_df = grouped.unstack(level=1)
total = unstacked_df.diff(periods=-1)
print(total)

# 10.712865  7.3952  14.257001