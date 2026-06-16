import numpy as np

# 1. Savetxt
# 2 loadtxt

# 2 X 3 Matrix
sample_data = np.array([
    [1,2,3],
    [4,5,6]
])

print("Matrix 2 X 3:")
print(sample_data)

print("===================")
# 1. Savetxt
np.savetxt('numpy_library/sample_date.csv', sample_data, delimiter=',', fmt="%d")

print("===================")
# 2 loadtxt
load_data = np.loadtxt('sample_date.csv', delimiter=',')
print("Load data from csv file :\n", load_data)