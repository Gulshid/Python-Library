import numpy as np;

# Array / list  Creation
# 1D Array Creation
print("1D Array  :")
# Method 1
print("Method 1 :")
my_list = [1,2,3,4,5] # 1D array
a = np.array(my_list)

print(my_list)
print(a)

# Method 2
print("Method 2 :")
b = np.array([1,2,3,4,5,6,7,8]) #  1D array
print(b)
print("=======")


print("2D Array  :")
# 2D Array Creation
array_1 = np.array(([1,2,3], [4,5,6], [7,8,9])) # 3 X 3 array
print(array_1)

print("==========")
# Zero  Array Creation
print("Zero Array :")
arr_zero = np.zeros((4,4)) # 4 X 4
print(arr_zero)

print("==========")
# Ones  Array Creation
print("Once Array :")
arr_one = np.ones((3,3)) # 3 X 3
print(arr_one)

print("==========")
# Arrange  Array Creation
print("Arange Array :")
arr_arange = np.arange(1,11, 2) # Even / odd
print(arr_arange)

print("==========")
# Random  Array Creation
print("Random Array :")
arr_random = np.random.random((3,3)) # 2 X 3
print(arr_random)
