import pandas as pd

series_1 = pd.Series([1, 2, 3], index=["Verstappen", "Hamilton", "Leclerc"])
series_2 = pd.Series(["Red Bull", "Mercedes", "Ferrari"], index=["Verstappen", "Hamilton", "Leclerc"])

frame = pd.DataFrame({"Position": series_1, "Team": series_2})
print(frame)


data = {"Points": [25, 18, 15], "Team": ["Red Bull", "Mercedes", "Ferrari"]}
frame_2 = pd.DataFrame(data, index=["Verstappen", "Hamilton", "Leclerc"])
champion = pd.Series(["Yes", "No", "No"], index=["Verstappen", "Hamilton", "Leclerc"])
frame_2["World Champion"] = champion
print(frame_2)
print(frame_2["Team"])
print(frame_2.iloc[:, 0])
print(frame_2.loc["Verstappen"])
print(frame_2.loc[frame_2["Points"] > 15])
print(frame_2.head(2))


