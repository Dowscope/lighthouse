import pandas as pd

df = pd.read_csv('fc_barcelona.csv')  # File not available
df.head()

points = df.Pts.max()
points_min = df.Pts.min()
games_played = df.MP.max()
wins = df.W.median()
wins_min = df.W.min()
losses = df.L.median()
attendance = df.Attendance.dropna().mean() # skipping missing values (NaN) because there were no fans during 2020-2021 season because of COVID

print(games_played)                 # 42
print(round(attendance, 2))         # 72580
print(round(wins - losses))         # 19
print(wins_min)                     # 15
print(points-points_min)            # 54
