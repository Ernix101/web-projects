import matplotlib.pyplot as plt
import numpy as np

# This is a rebuilt plot of how my real restaurant business is performing.

foods = np.array(["pilau", "pizza", "chicken", "burger", "beef", "githeri"])
sales = np.array([25000, 25000, 30000, 28000, 27000, 28000])

plt.bar(foods, sales, color="brown")
plt.title("My restaurant sales this quarter so far", fontsize="16",family="Arial")
plt.xlabel("Foods", color='orange')
plt.ylabel("Sales made", color='green')
plt.show()

