import pandas as pd

data = {
    "Name" : ["Ali", "Ahmad", "Usman"],
    "Marks" :[80, 90, 85]
}

df = pd.DataFrame(data)
print("DateFrame of Data")
print(df)

print("===== Data Store in csv File ===========")
df.to_csv("panda_library/students.csv", index=False)
print("Data is successfully store in csv file ===>")

print("===== Read Data from  csv File ===========")
df = pd.read_csv("panda_library/students.csv")
print("Read data from csv file :")
print(df)

