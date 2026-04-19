import matplotlib.pyplot as plt
import numpy as np

years = np.array([2021, 2022, 2023, 2024, 2025])
sales = np.array([1000, 2000, 2500, 2700, 2800])

# plt.plot(years, sales)
# plt.show()

# 2. A bar chart comparing values accross 5 categories
girls = ['Mia', 'Jenna', 'Sally', 'Emma']
time_spent = [20, 25, 15, 19]

plt.bar(girls, time_spent)
plt.title("Time spent with girls (hrs/week)", color="red")
plt.show()
