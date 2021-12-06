import pandas as pd
import statistics
df = pd.read_csv("data1.csv")
data = df["Weight(Pounds)"].tolist()
sum = 0

for i in data:
    sum = i+sum

num=len(data)
avg = sum/num

mean = statistics.mean(data)

print(avg)
print(mean)