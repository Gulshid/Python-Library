import matplotlib.pyplot as plt

# SImple Line Plot

x = [1,2,3,4,5]
y = [1.4,3.2,5.5,8,9.4]

plt.plot(x, y, color = "red", linestyle= "--", marker = "o")

plt.title("*** Simple Line Plot ***")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.show()