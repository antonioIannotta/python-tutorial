import numpy as np
import pandas as pd
import matplotlib

dataframe = pd.DataFrame({
    "Population": [10, 20, 30, 40, 50],
    "GPD": [100, 200, 300, 400, 500],
    "Surface": [120, 220, 320, 420, 520]
}, columns=["Population", "GPD", "Surface"])

print(dataframe)

dataframe.index = [
    "Italy",
    "France",
    "Spain",
    "Germany",
    "UK"
]

print(dataframe)
print(dataframe.loc["Germany"])

print(dataframe.loc["Italy" : "Spain"])
print(dataframe["Population"] > 15)

print(dataframe[["Population", "GPD"]] / 100)
print(dataframe.drop("Spain"))

dataframe.plot()
print(dataframe.head(3))