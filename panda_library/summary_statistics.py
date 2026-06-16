import pandas as pd

data = {
    "Marks" : [80, 90, 60, 50, 40, 65, 99, 35, 80, 36] # 10 marks store 
}

df = pd.DataFrame(data)
print("Dataframe of data :\n", df)

print("======= SUmmary of Statistics ========== ")
print(df.describe())