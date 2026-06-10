import numpy as np

# np.mean(scores)
# np.median(scores)
# np.percentile(scores, 25)
# np.var(scores)

scores = np.array([10, 20, 30, 40 , 50])

print(scores)

print("============")
# Mean Operation in Statistics
print("Mean of scores :")
print(np.mean(scores)) # 10 + 20 + 30 + 40 + 50 / 5

print("============")
# Median Operation in Statistics
print("Median of scores :")
print(np.median(scores)) # 10 , 20 , 30 , 40 , 50

print("============")
# Persentile Operation in Statistics
print("Persentile of scores :")
print(np.percentile(scores, 25))

print("============")
# variance Operation in Statistics
print("variance of scores :")
print(np.var(scores))


