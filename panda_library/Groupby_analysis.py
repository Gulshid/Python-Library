import pandas as pd

data = {
    "Name" : ["Ali", "Ahmad", "Ali", "Ahmad", "Ali"],
    "Marks" : [56, 60, 78, 90, 95]
}

# find the dataframe of data
df = pd.DataFrame(data)

print("DataFrame of Data :")
print(df)

print("======= Groupby Anaysis =========")
print("Group by name and Calculate total marks :")
result = df.groupby("Name")["Marks"].sum()
print(result)


print("======================")
print("Average / mean of Marks :")
print(df.groupby("Name")["Marks"].mean())

print("======================")
print("Count of Marks :")
print(df.groupby("Name")["Marks"].count())

print("======================")
print("Multiple Statistics :")
print(df.groupby("Name")["Marks"].agg([
    "sum", "mean", "count", "min", "max"
]))


