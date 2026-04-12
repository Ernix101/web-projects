import csv
import pandas as pd
import numpy as np

# Data loading test


favorite_foods = {
    "protein": ['beef', 'fish', 'potato'],
    "carbs": ['cereal', 'pancakes', 'rice'],
    "veggies": ['lettuce', '', 'tomatoes'],
    "fruits": ['apple', 'orange', 'banana'],
    "calories": [1000, 2000, 2500]
}

foods_df = pd.DataFrame(favorite_foods)

# print(foods_df['protein'].dtype)
# print(foods_df['calories'].dtype)
# print(foods_df.describe())



ufo_path = r"C:\Users\ERNEST\Downloads\archive\scrubbed.csv"

df = pd.read_csv(ufo_path)


# Selection and filtering!

df['duration(seconds)'] = pd.to_numeric(df['duration(seconds)'], errors='coerce')

# first_secs = df['duration(seconds)'].head(5)
# their_mean = first_secs.mean()
# print(float(their_mean))

mean_secs = df['duration(seconds)'].mean()
above_mean = df[df['duration(seconds)'] > mean_secs]

print(f"Mean: {mean_secs:.2f}")
print(above_mean[['city', 'state', 'shape', 'duration(seconds)']])

