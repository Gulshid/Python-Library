import matplotlib.pyplot as plt

# Horizental Chart (Countires ===> Populations)
countires = ["Pakistan", "India", "China", "Iran"]
populations = [230, 1400, 1440, 85]

plt.barh(countires, populations)

plt.title("*** Countries Populations ***")

plt.xlabel("Populations")

plt.ylabel("Countries")

plt.show()