import pandas as pd
import statistics
df = pd.read_csv("data1.csv")
data = df["Weight(Pounds)"].tolist()
data.sort()
med1indx =len(data)/2-1
med2indx = len(data)/2
median1 = data[int(med1indx)]
median2 = data[int(med2indx)]

median=(median1+median2)/2
print(median)

md = statistics.median(data)
print(md)

