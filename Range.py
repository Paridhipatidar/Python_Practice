import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Use raw string to avoid escape character issues
dataset = pd.read_csv(r"C:\Users\parid\Documents\Excel Work\Practice1.csv")
d = dataset.head(3)
print(d)

min_r=dataset["Marks"].min()
max_r=dataset["Marks"].max()

print(min_r,max_r)
range=max_r-min_r
print(range)