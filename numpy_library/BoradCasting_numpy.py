import numpy as np

# BroadCasting:
        # NumPy automatically adjusts shapes for operations.

# 2 X 3 Matrix
matrix = np.array([
    [1,2,3],
    [4,5,6]
])

# 1 X 3 Matrix
vector = np.array([10, 20, 30])

print("Matrix :\n", matrix)
print("============")
print("Vector : ", vector)

print("============")
print("Matric + Vector :")
print(matrix + vector)



