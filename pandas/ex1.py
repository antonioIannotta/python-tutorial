import pandas as pd

series = pd.Series([1, 2, 3], index=["Verstappen", "Hamilton", "Leclerc"])
series.index.name = "Drivers"
print(series)
