import numpy as np

# TODO Build notes website + health data pipeline concepts

array = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12],
                 [13, 14, 15, 16]])

# * NOTE: array[start:end:step]
print(array[:, 2])      # Returns [3, 7, 11, 15] cause ':' selects all rows then ',' separates to the columns
print(array[:, 1:4])    # Returns columns 1 to 4 with all the rows 
print(array[0:2, 0:2])  # Returned the first 2 rows [1, 2] and the [5, 6] as like a quadrant
