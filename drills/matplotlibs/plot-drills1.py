import matplotlib.pyplot as plt
import numpy as np

years = np.array([2021, 2022, 2023, 2024, 2025])
sales = np.array([1000, 2000, 2500, 2700, 2800])

# plt.plot(years, sales)
# plt.show()

# 2. A bar chart comparing values accross 5 categories
girls = ['Mia', 'Jenna', 'Sally', 'Emma']
time_spent = [20, 25, 15, 19]
bar_colors = ['lightgreen', 'orange', 'pink', 'lightblue']

# plt.bar(girls, time_spent, color=bar_colors)
# plt.title("Time spent with girls (hrs/week)", color="red")
# plt.show()

# 3. A histogram generated from random numbers in numpy and divided into 20 bins

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
# plt.axvline(growth_mean, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {growth_mean:.2f}')

# plt.legend()
# plt.show()

# 4. A scatter plot of 2 related variables
# We'll compare my network providers daily bundle offers

price1 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
safaricom_bundles = np.array([20, 50, 120, 200, 300, 450, 550, 700, 850, 1000])

price2 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
airtel_bundles = np.array([30, 50, 60, 75, 150, 300, 550, 750, 1000, 2000])

# plt.scatter(price1, safaricom_bundles,  color='green',
#                                         alpha= 0.6,
#                                         s=200,
#                                         label='Safaricom')


# plt.scatter(price2, airtel_bundles,     color='red',
#                                         alpha= 0.6,
#                                         s=200,
#                                         label='Airtel')

# plt.title("Comparison btw Safaricom and Airtel's data deals", color='blue', fontfamily='sans')
# plt.xlabel("Price (ksh)")
# plt.ylabel("Amount given (MBs)")

# plt.legend()
# plt.show()

# 5. 2x2 grid of subplots - line, bar, scatter, histogram
# First, an example of a 2x2 subplot.
exercise_days = np.array([14, 15, 16, 17, 18, 19, 20])
weight_reduction = np.array([1, 2, 3, 4, 5, 7, 9])

increased_years = np.array([2, 3, 6, 7, 8, 9, 10])
strength = np.array([30, 40, 55, 65, 70, 78, 85])
mood = np.array([50, 55, 80, 90, 97, 100, 110])

fig, ax = plt.subplots(2, 2, figsize=(10, 5))           # <-- The figsize increases the size of dimensions

ax[0, 0].plot(exercise_days, weight_reduction, color='blue', linestyle='dashdot')
ax[0, 0].set_title("exercise days Vs weight reduction")

ax[0, 1].bar(exercise_days, increased_years, color='green')
ax[0, 1].set_title("exercise days Vs increased years")

ax[1, 0].scatter(exercise_days, strength)
ax[1, 0].set_title("exercise days Vs strength")

ax[1, 1].hist(mood, bins=10, color='aquamarine', edgecolor='black')
ax[1, 1].set_title("mood distribution")

plt.tight_layout()      # <-- Fixes spacing between layouts
plt.show()
