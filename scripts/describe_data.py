import pandas as pd

df = pd.read_csv("../data/car-sales.csv")
print("====="*10)
print("Getting data types of Car Sales data frame")
print(df.dtypes)
print("====="*10)

column_names = df.columns
column_index = df.index

print(f"Column Names: {column_names}")
print(f"Column Index: {column_index}")

# Functions we can call on our df
print(f"\nUsing the .describe() function\n{df.describe()}")
print(f"\nUsing the .info() function\n{df.info()}\n")
print(f"Mean df values:\n{df.mean()}\n")

car_prices = pd.Series([3000, 1500, 111250])
print(car_prices.mean())

print(f"\nSum of values in df: {df['Doors'].sum()}")
print(f"Length of our df: {len(df)}")

