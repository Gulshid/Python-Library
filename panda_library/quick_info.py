import pandas as pd

data = {
    "Name" :["Ali", "Ahmad", "Usman"],
    "Marks" : [80, 90, 78]
}

df = pd.DataFrame(data)
print('dataFrame of data :')
print(df)

print("============== Quick  Information ========")
print(df.info())