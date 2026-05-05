import numpy as np

# TODO Build notes website + health data pipeline concepts

array = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12],
                 [13, 14, 15, 16]])

# * NOTE: array[start:end:step]
# print(array[:, 2])      # Returns [3, 7, 11, 15] cause ':' selects all rows then ',' separates to the columns
# print(array[:, 1:4])    # Returns columns 1 to 4 with all the rows 
# print(array[0:2, 0:2])  # Returned the first 2 rows [1, 2] and the [5, 6] as like a quadrant




# 1. 1D array of 20 patients of ages between 18 and 80
np.random.seed(1)
patient_ages = np.random.randint(18, 80, 20)

# print(patient_ages)
# Calculate the mean, median and min/maximum ages

mean = np.mean(patient_ages)
median = np.median(patient_ages)
min = np.min(patient_ages)
max = np.max(patient_ages)

print(f"Summary of ages-> Mean:{mean}, Median:{median}, min:{min}, max{max}")


# 2. Daily patient visits per day for 4 weeks
record = np.random.randint(10, 60, size=(4, 7))
busiest_day_count = np.max(record)
day_number = np.argmax(record)
print(f"The busiest day was DAY NO: {day_number} with a total of {busiest_day_count} visits")