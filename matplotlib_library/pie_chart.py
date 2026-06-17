import matplotlib.pyplot as plt


# PIe Plot 

labels = ["Android", "iOS", "Window", "Other"]
shares = [70, 20, 5, 5] # 100%

plt.pie(shares, labels = labels, autopct='%1.1f%%')

plt.title("*** Mobile OS MArket Shares ***")

plt.show()
