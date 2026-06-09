import numpy as np;

# shape, ndim, dtype, size, nbyte

arr_2d = np.array(([1,2,3],[4,5,6])) # 2 X 3 => 2D Array

print("2D Array :")
print(arr_2d)
print("==============")

print("Array Properties :")
# Array Shape
print("Array Shape :")
print(arr_2d.shape)

print("==============")
# Array ndim
print("Array ndim :")
print(arr_2d.ndim)

print("==============")
# Array dtype
print("Array dtype :")
print(arr_2d.dtype)

print("==============")
# Array Size 
print("Array Size :")
print(arr_2d.size)

print("==============")
# Array nbyte 
print("Array nbyte :")
print(arr_2d.nbytes)