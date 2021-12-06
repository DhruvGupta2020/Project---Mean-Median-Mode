import pandas as pd
import statistics

df = pd.read_csv("data1.csv")
data = df["Weight(Pounds)"].tolist()

mode = statistics.mode(data)
print(mode)