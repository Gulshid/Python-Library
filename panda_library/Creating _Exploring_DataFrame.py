import pandas as pd

data = {
    "Name" : ["Charlie", "Bob", "Diana", "ALice"],
    "Age" : [23, 20, 24, 28],
    "City" : ["New York", "Tokyo", "London", "Paris"],
    "Salary": ["24000", "30000", "34000", "40000"]
}

df = pd.DataFrame(data)

print("Dataframe of Data :")
print(df)

print("===============")

print("Properties of DataFrame:")
# Shape of Data
print("Shape of data :", df.shape)

print("===============")
# Column of Data
print("Column of data :", df.columns.tolist())

print("===============")
# dtypes of Data
print("Datatype of Data:\n", df.dtypes)

print("===============")
# first 2 row  of Data
print("First 2 row of data :\n", df.head(2))

print("===============")
#  Only Specific Column values   of Data
print("Name Values :\n", df['City'])

print("===============")
#  Only row  at index 1    of Data
print("At index 1\n", df.iloc[1])

print("===============")
#  Statistics   of Data
print("Describes :\n", df.describe())




