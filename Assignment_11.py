import numpy as np
import pandas as pd

values = pd.Series(np.random.randint(1, 101, size=10))

print("Generated Series:")
print(values)

print("\nValue at index 0:", values.iloc[0])
print("Values between index 2 and 5:")
print(values.iloc[2:6])

above_50 = values[values > 50]
print("\nValues above 50:")
print(above_50)

print("\nAverage:", values.mean())
print("Middle value (Median):", values.median())
print("Lowest:", values.min())
print("Highest:", values.max())
