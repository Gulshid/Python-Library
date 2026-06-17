import matplotlib.pyplot as plt

x = [1,2,3,4]
y1 = [2,3,4,5]
y2 = [5,4,3,2]

plt.subplot(1,2,1)
plt.plot(x, y1)

plt.title("Increasing")


# +===================

plt.subplot(1,2,2)
plt.plot(x, y2)
plt.title("Decreasing")



plt.show()

