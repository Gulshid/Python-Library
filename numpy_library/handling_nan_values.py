import numpy as np

# np.isnan(data) 
# np.nanmean(data)
# np.where(np.isnan(data), mean_val, data)

array_1 = np.array([1,2,np.nan, 4, 5])
print("Array :", array_1)

print("=====================")
# np.isnan(data)  ===> detect array / list not in number
print("Isnan :", np.isnan(array_1))

print("=====================")
# np.nanmean(data)
print("nanmean :", np.nanmean(array_1)) # 1 + 2 + 4 + 5 / 4


print("=====================")
# np.where(np.isnan(data), mean_val, data)
clean_data = np.where(np.isnan(array_1), 3, array_1)
print("Clean data array :", clean_data)
