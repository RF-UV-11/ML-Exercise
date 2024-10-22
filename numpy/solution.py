import numpy as np

# Load user data for certain exercises
data = np.load("user_data.npz")
names = data["names"]
ages = data["ages"]
incomes = data["incomes"]
countries = data["countries"]

# Solutions

# -----------------------------
# 1. Array Creation and Properties
# -----------------------------

# Q1: Create an array of 10 zeros, an array of 10 ones, and an array of 10 fives.
zeros = np.zeros(10)
ones = np.ones(10)
fives = np.full(10, 5)
print("Q1:", zeros, ones, fives)

# Q2: Create an array of integers from 10 to 50.
int_array = np.arange(10, 51)
print("Q2:", int_array)

# Q3: Create a 3x3 matrix with values ranging from 0 to 8.
matrix_3x3 = np.arange(9).reshape(3, 3)
print("Q3:", matrix_3x3)

# Q4: Find the shape, size, and data type of the following array:
sample_array = np.array([10, 20, 30, 40, 50])
shape = sample_array.shape
size = sample_array.size
dtype = sample_array.dtype
print(f"Q4: Shape: {shape}, Size: {size}, Data type: {dtype}")


# -----------------------------
# 2. Array Indexing and Slicing
# -----------------------------

# Q5: Extract the first 10 names and their respective ages from the user data.
first_10_names = names[:10]
first_10_ages = ages[:10]
print("Q5:", first_10_names, first_10_ages)

# Q6: Reverse the array.
array = np.array([1, 2, 3, 4, 5])  # Declaring an array to reverse
reversed_array = array[::-1]
print("Q6:", reversed_array)


# -----------------------------
# 3. Array Shape Manipulation
# -----------------------------

# Q7: Reshape an array of size 9 (from 0 to 8) into a 3x3 matrix.
reshaped_array = np.arange(9).reshape(3, 3)
print("Q7:", reshaped_array)

# Q8: Flatten a 2D array into a 1D array:
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # Declaring a matrix to flatten
flattened_array = matrix.flatten()
print("Q8:", flattened_array)


# -----------------------------
# 4. Mathematical and Statistical Operations
# -----------------------------

# Q9: Mean, median, standard deviation, and sum of ages.
mean_age = np.mean(ages)
median_age = np.median(ages)
std_age = np.std(ages)
sum_age = np.sum(ages)
print(f"Q9: Mean: {mean_age}, Median: {median_age}, Std: {std_age}, Sum: {sum_age}")

# Q10: Compute the dot product of two arrays.
array1 = np.array([1, 2, 3])  # Declaring arrays for dot product
array2 = np.array([4, 5, 6])
dot_product = np.dot(array1, array2)
print("Q10:", dot_product)


# -----------------------------
# 5. Broadcasting
# -----------------------------

# Q11: Add 10 to all elements of the array.
arr = np.array([1, 2, 3, 4, 5])  # Declaring an array for broadcasting
broadcast_add = arr + 10
print("Q11:", broadcast_add)

# Q12: Multiply each age in the user data by 2.
multiplied_ages = ages * 2
print("Q12:", multiplied_ages)


# -----------------------------
# 6. Boolean Indexing
# -----------------------------

# Q13: Find all users whose age is greater than 40.
age_filter = ages > 40
users_above_40 = names[age_filter]
print("Q13:", users_above_40)

# Q14: Find all users whose income is between 50,000 and 100,000.
income_filter = (incomes >= 50000) & (incomes <= 100000)
users_in_income_range = names[income_filter]
print("Q14:", users_in_income_range)


# -----------------------------
# 7. Linear Algebra
# -----------------------------

# Q15: Solve the system of linear equations.
A = np.array([[3, 1], [1, 2]])  # Declaring a system of linear equations
B = np.array([9, 8])
solution = np.linalg.solve(A, B)
print("Q15:", solution)


# -----------------------------
# 8. Random Sampling and Seeding
# -----------------------------

# Q16: Generate a random array of size 10 using seed 42.
np.random.seed(42)
random_array = np.random.rand(10)
print("Q16:", random_array)

# Q17: Shuffle the array randomly.
arr = np.array([10, 20, 30, 40, 50])  # Declaring an array to shuffle
np.random.shuffle(arr)
print("Q17:", arr)
