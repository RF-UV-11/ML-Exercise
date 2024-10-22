import numpy as np

# Load user data for certain exercises
data = np.load("user_data.npz")
names = data["names"]
ages = data["ages"]
incomes = data["incomes"]
countries = data["countries"]

# NumPy Exercises

# -----------------------------
# 1. Array Creation and Properties
# -----------------------------

# Q1: Create an array of 10 zeros, an array of 10 ones, and an array of 10 fives.
# Write your code below

# Q2: Create an array of integers from 10 to 50.
# Write your code below

# Q3: Create a 3x3 matrix with values ranging from 0 to 8.
# Write your code below

# Q4: Find the shape, size, and data type of the following array:
sample_array = np.array([10, 20, 30, 40, 50])
# Write your code below


# -----------------------------
# 2. Array Indexing and Slicing
# -----------------------------

# Q5: Extract the first 10 names and their respective ages from the user data.
# Write your code below

# Q6: Given the array [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], reverse the array.
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# Write your code below


# -----------------------------
# 3. Array Shape Manipulation
# -----------------------------

# Q7: Reshape an array of size 9 (from 0 to 8) into a 3x3 matrix.
# Write your code below

# Q8: Flatten a 2D array into a 1D array:
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Write your code below


# -----------------------------
# 4. Mathematical and Statistical Operations
# -----------------------------

# Q9: Find the mean, median, standard deviation, and sum of ages from the user data.
# Write your code below

# Q10: Compute the dot product of two arrays:
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
# Write your code below


# -----------------------------
# 5. Broadcasting
# -----------------------------

# Q11: Add 10 to all elements of the following array using broadcasting:
arr = np.array([10, 20, 30, 40, 50])
# Write your code below

# Q12: Multiply each age in the user data by 2 (without using a loop).
# Write your code below


# -----------------------------
# 6. Boolean Indexing
# -----------------------------

# Q13: Find all users whose age is greater than 40.
# Write your code below

# Q14: Find all users whose income is between 50,000 and 100,000.
# Write your code below


# -----------------------------
# 7. Linear Algebra
# -----------------------------

# Q15: Solve the following system of linear equations:
# 2x + 3y = 5
# 4x + y = 6
A = np.array([[2, 3], [4, 1]])
B = np.array([5, 6])
# Write your code below


# -----------------------------
# 8. Random Sampling and Seeding
# -----------------------------

# Q16: Generate a random array of size 10 using a random seed of 42.
# Write your code below

# Q17: Shuffle the following array randomly:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# Write your code below
