import pandas as pd
import numpy as np

data = {
    "Employee" : ["Charlie", "Bob", "Frank", "ALice"],
    "Salary": [45000, 50000, 57000, 60000]
}

df = pd.DataFrame(data)
print("DataFrame of Data:")
print(df)

print("========= Adding and Modifying Column ==========")
print("Adding Bonus Column :")
df["Bonus"] = df["Salary"] * 0.10
print(df)

print("======================")
print("Add Another column Total Salary :")
df["Total_Salary"] = df["Salary"] + df["Bonus"]
print(df)

print("======================")
print("Increase Salary by 5% :")
df["Salary"] = df["Salary"] * 1.05 # 5%
print(df)

print("======================")
print("Check if Employee > 50000:")
df["High_Salary"] = np.where(
    df["Total_Salary"] > 50000,
        "Yes",
        "No" 
)

print("Updated DataFrame :")
print(df)

