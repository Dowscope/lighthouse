import pandas as pd
df = pd.read_csv('wine.csv')

alcohol_filter = df['Class'] == 3
filtered = df[alcohol_filter]
df[filtered]                # 86
print(len(filtered))        # 48