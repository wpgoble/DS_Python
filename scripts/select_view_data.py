import pandas as pd
from matplotlib import pyplot as plt

file = "../data/car-sales.csv"
df = pd.read_csv(file)

print("Head values: ")
print(df.head())
print("Tail values: ")
print(df.tail())

print("====="*10)

# .loc & .iloc
temp = pd.Series(["cat", "dog", "bird", "panda", "snake"],
                 index= [0, 3, 9, 8, 3])
print(temp)
# .loc refers to the index number
print(temp.loc[3])
print(f"\n{temp.loc[9]}")

print(f"\n{df.loc[3]}")

# .iloc refers to the position in the list, starting with zero
print(f"\n{temp.iloc[3]}")

print(f"\n{df.iloc[3]}")

print(f"\n grabbing a sequence from the original car df:\n{df.loc[:3]}")

print("More data\n")
print(df["Make"])
# which can also be
print(df.Make)

print("====="*10)
print(df[df.Make == "Toyota"])

# Using cross tab
# This aggreates the two columns together and compares the data against each other
print(pd.crosstab(df.Make, df.Doors))

# Groups the data frame by the car make, and then calcualtes the mean values.
print(df.groupby(["Make"]).mean())

print("====="*15)
print(df[df["Colour"] == "White"].groupby(["Make"]).mean())

# Simple plot of the Odometer reading
df["Odometer (KM)"].plot()
plt.show()

# Histogram, allows us to see the distribution of the data
df["Odometer (KM)"].hist()
plt.show()

df["Price"] = df["Price"].str.replace('[\$\,]', '').astype(float)
print(df)
df["Price"].plot()
plt.show()