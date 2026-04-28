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

fig1, ax1 = plt.subplots(2, 2, figsize=(10, 5))           # <-- The figsize increases the size of dimensions

ax1[0, 0].plot(exercise_days, weight_reduction, color='blue', linestyle='dashdot')
ax1[0, 0].set_title("exercise days Vs weight reduction")
ax1[0, 0].set_facecolor('grey')         # <-- This sets the color of the face

ax1[0, 1].bar(exercise_days, increased_years, color='green')
ax1[0, 1].set_title("exercise days Vs increased years")
ax1[0, 1].set_facecolor('antiquewhite')


ax1[1, 0].scatter(exercise_days, strength)
ax1[1, 0].set_title("exercise days Vs strength")
ax1[1, 0].set_facecolor('aquamarine')

ax1[1, 1].hist(mood, bins=10, color='cyan', edgecolor='black')
ax1[1, 1].set_title("mood distribution")
ax1[1, 1].set_facecolor('magenta')

fig1.set_facecolor('lightblue')
plt.tight_layout()      # <-- Fixes spacing between layouts



# 6. Plot 2 separate lines on the same chart
fig2, ax2 = plt.subplots()          #   <-- New single axis, not 2x2

ax2.plot(exercise_days, strength, color='blue', linestyle='--', label='Strength')
ax2.plot(exercise_days, mood, color='green', linestyle='-', label='Mood')
ax2.set_facecolor('yellow')

# Find the peak of the mood
peak_x = exercise_days[np.argmax(mood)]
peak_y = mood[np.argmax(mood)]

ax2.annotate('Peak mood',
            xy=(peak_x, peak_y),            # <-- The actual point
            xytext=(peak_x-2, peak_y-1),       # <-- Where the text sits
            arrowprops=dict(arrowstyle='->'))

ax2.legend()
ax2.set_title("Strength Vs Mood")
plt.grid(axis='x', color='black', linestyle='-.')
plt.show()






# # An example from google on how to plot multiple lines together
# x = np.arange(0, 10, 1)
# y1 = [2, 3, 5, 8, 4, 3, 2, 1, 0, 1]
# y2 = [1, 2, 4, 6, 10, 8, 5, 3, 2, 2]

# # 1. Plot the 2 separate lines
# plt.plot(x, y1, label='line 1', color='blue')
# plt.plot(x, y2, label='line 2', color='green')

# # 2. Annotate the highest point (Using line 2 as the example)
# ymax = max(y2)
# xmax = x[np.argmax(y2)]

# plt.annotate(f'Max : {ymax}',
#              xy=(xmax, ymax),
#              xytext=(xmax + 1, ymax + 0.5),
#              arrowprops=dict(facecolor='black', shrink=0.05))

# plt.legend()
# plt.show()
