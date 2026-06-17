import matplotlib.pyplot as plt

# Histogram Plot

ages = [18, 22, 45, 36, 40, 47, 58, 50, 44, 56, 34, 49, 60]

plt.hist(ages, bins= 5)

plt.title("*** Ages Distributions ***")

plt.xlabel("Ages")

plt.ylabel("Frequency")

plt.show()
