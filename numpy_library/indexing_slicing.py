import numpy as np

# 3 X 3 matrix
matrix = np.array([
    [1,2,3], # 0 
    [4,5,6], # 1
    [7,8,9], # 2
])
print("Matrix 3 X 3 :")
print(matrix)

print("===============")
# Specific Element in matrix
print("Matric element 9 :")
print(matrix[2,2])

print("===============")
# : Element in matrix
print("Matrix all col: :")
print(matrix[:,1])

print("===============")
# : Element in matrix
print("Matrix all row: :")
print(matrix[2, :])

print("===============")
# : Element in matrix
print("Matrix indexing and Slicing :")
print(matrix[:2, -1:])