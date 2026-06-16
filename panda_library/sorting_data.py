import pandas as pd

data = {
    "Name": ["Ali", "Ahmad", "Usman", "Bilal"],
    "Age" : [24, 25, 30, 28]
}

df = pd.DataFrame(data)

print("DataFrame of data :")
print(df)

print("======= Sorting Data =========")
print("Sort by Age (Smallest to Largest)")
print(df.sort_values("Age", ascending= True))

print("=======================")
print("Sort by Age (largest to Smallest)")
print(df.sort_values("Age", ascending= False))
