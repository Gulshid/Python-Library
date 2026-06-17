import matplotlib.pyplot as plt

# Multiple line on same plot 

years = [2018, 2019, 2020, 2021, 2022]
sales_A = [50, 60, 65, 70, 80]
sales_B = [40, 55, 60, 68, 75]

plt.plot(years, sales_A, label = "Product A")
plt.plot(years, sales_B, label = "Product B")

plt.title(" *** Sales Comparison *** ")

plt.xlabel("Years")

plt.ylabel("Sales")

plt.legend()

plt.show()
