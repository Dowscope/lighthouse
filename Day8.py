import pandas as pd
df = pd.read_csv('paris_landmarks.csv') # No access to this file.

# we sort our data by queue_time, starting from the longest 
df.sort_values(by="queue_time",ascending=False).head()


df.iloc[df['price'].idxmax()]['landmark']
df['queue_time'].mean()