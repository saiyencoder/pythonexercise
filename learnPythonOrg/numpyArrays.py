# Numpy Arrays are great alternatives to Python Lists. Some of the key advatages is that they are fast and easy to work with and can perform
# calculations across entire arrays.

# Create 2 new lists height and weight
height = [1.87, 1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Import the numpy package as np
import numpy as np

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)

# We can verify the type with the following command
print(type(np_height))

# Now we can perform element wise-calculations on height and weight.
# For example we could take all 6 of the height and weight observations and calculate the BMI for each observation with a single equation.
bmi = np_weight / np_height ** 2
print(bmi)

# Another great feature of Numpy arrays is the ability to subset.
print(bmi > 25)       # Outputs true for all bmi that are over 25 and false for the ones under 
print(bmi[bmi > 25])  # Outputs an array that shows only the bmi's > 25

