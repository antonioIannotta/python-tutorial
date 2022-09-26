import numpy as np
import pandas as pd

g7_pop = pd.Series([35.467, 63.951, 80.940, 60.665, 127.061, 64.511, 318.523])
print(g7_pop)

g7_pop.name = "G7 population in millions"
print(g7_pop)

g7_pop.index = [
    "Canada",
    "France",
    "Germany",
    "Italy",
    "Japan",
    "United Kingdom",
    "United States"
]

print(g7_pop)

print("Canada population: " + str(g7_pop["Canada"]) + " millions")
print(g7_pop["Canada": "Italy"])

for country in g7_pop.index:
    if g7_pop[country] > 80:
        print(country + ": " + str(g7_pop[country]))


