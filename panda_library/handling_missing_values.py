import pandas as pd
import numpy as np

data = {
    "Name" : ["Charlie", "Bob", "Frank", "Diana"],
    "Age" : [25, np.nan, 30, np.nan]
}

df = pd.DataFrame(data)

print("Dataframe of Data:")
print(df)

print("====== Handling Missing Values ==========")
# Check missing Values
print("Check missing Values in data :\n")
print(df.isnull())

print("===================")
# Count missing Values
print("Count missing Values in data :\n")
print(df.isnull().sum())

# print("===================")
# # Remove  missing Values
# print("Remove missing Values in data :\n")
# print(df.dropna())

print("===================")
# Change missing Values with 20
print("Change missing Values in data with 20 :\n")
df["Age"] = df["Age"].fillna(20)
print(df)

