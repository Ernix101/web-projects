import matplotlib.pyplot as plt
import numpy as np

years = np.array([2021, 2022, 2023, 2024, 2025])
sales = np.array([1000, 2000, 2500, 2700, 2800])

# plt.plot(years, sales)
# plt.show()

# 2. (i) A bar chart comparing values accross 5 categories
girls = ['Mia', 'Jenna', 'Sally', 'Emma']
time_spent = [20, 25, 15, 19]
bar_colors = ['lightgreen', 'orange', 'pink', 'lightblue']

# plt.bar(girls, time_spent, color=bar_colors)
# plt.title("Time spent with girls (hrs/week)", color="red")
# plt.show()

# (ii) A histogram generated from random numbers in numpy and divided into 20 bins

rng = np.random.default_rng()
youtube_growth = rng.integers(low=1, high=100, size=1000)
# print(random_numbers)

# plt.hist(youtube_growth, bins=20, color='aquamarine', edgecolor='black')
# plt.title("Histogram with 20 bins (my youtube activity)")
# plt.xlabel("Frequency per 20 months")
# plt.ylabel("subscribers (per 1000)")
# plt.show()

# (iii) Plotting an axvline at the mean of the data
growth_mean = np.mean(youtube_growth)
plt.axvline(growth_mean, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {growth_mean:.2f}')

# plt.legend()
# plt.show()
