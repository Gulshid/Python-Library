import numpy as np

# np.sum(data, axis=0)
# np.mean(data)
# np.dot(A,B)
# np.linalg.det(A)
# np.linalg.inv(A)

# np.min(data)
# np.max(data)

# 2 X 3 Matrix
data = np.array([
    [1,2,3],
    [5,6,7]
])

# 2 X 2
A = np.array([
    [2,3],
    [5,6]
])

# 2 X 2
B = np.array([
    [1,4],
    [7,8]
])

print("Matrix 2 X 3 :")
print(data)

print("===============")
# Sum Operation
print("Sum of data :")
print(np.sum(data, axis= 1))

print("===============")
# mean Operation
print("mean of data :")
print(np.mean(data))


print("===============")
# dot product Operation
print(A)
print(B)
print("Dot Product of   A and B :")
print(np.dot(A , B))

print("===============")
# Det Operation
print("Determinent of A :")
print(np.linalg.det(B))

print("===============")
# Inverse Operation
print("Inverse of B :")
print(np.linalg.inv(B))

print("===============")
# Min Operation
print("Min of data :")
print(np.min(data))

print("===============")
# Max Operation
print("Max of data :")
print(np.max(data))