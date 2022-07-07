import pandas as pd

series = pd.Series(["BMW", "Ford", "Honda"])
# print(series)

# print("====="*10)

colors = pd.Series(["Red", "Blue", "White"])
# print(colors)
# print("====="*10)

car_data = pd.DataFrame({"Car make": series,
                         "Color": colors})
# print(car_data)
print("====="*10)

# import dataframe
df = pd.read_csv("../data/car-sales.csv")
print(df)
print("====="*10)

# Exporting a dataFrame
# df.to_csv("exported_cars.csv", index = False)

