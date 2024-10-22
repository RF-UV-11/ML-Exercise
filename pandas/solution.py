# solution.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load employee and department data
employee_df = pd.read_csv("employee_data.csv")
department_df = pd.read_csv("department_data.csv")

# -----------------------------
# 1. Basic Data Exploration
# -----------------------------

# Q1: Display the first 5 records of the employee dataset.
print("First 5 records of employee dataset:\n", employee_df.head())

# Q2: Display the shape of both datasets (number of rows and columns).
print(f"Employee Data Shape: {employee_df.shape}")
print(f"Department Data Shape: {department_df.shape}")

# Q3: Check for missing values in both datasets.
print("Missing values in employee data:\n", employee_df.isnull().sum())
print("Missing values in department data:\n", department_df.isnull().sum())

# -----------------------------
# 2. Handling Missing Data
# -----------------------------

# Q4: Drop rows with missing values in the 'Name' column (essential info).
cleaned_employee_df = employee_df.dropna(subset=['Name'])
print(f"Shape after dropping rows with missing 'Name': {cleaned_employee_df.shape}")

# Q5: Fill missing values in 'Salary' with the average salary.
avg_salary = cleaned_employee_df['Salary'].mean()
cleaned_employee_df['Salary'].fillna(avg_salary, inplace=True)
print(f"Number of missing salaries after filling: {cleaned_employee_df['Salary'].isnull().sum()}")

# Q6: Fill missing values in the 'Department' column with 'Unknown'.
cleaned_employee_df['Department'].fillna('Unknown', inplace=True)
print(f"Number of missing departments after filling: {cleaned_employee_df['Department'].isnull().sum()}")

# Q7: Fill missing values in 'Age' and 'Experience' with median values.
median_age = cleaned_employee_df['Age'].median()
median_experience = cleaned_employee_df['Experience'].median()
cleaned_employee_df['Age'].fillna(median_age, inplace=True)
cleaned_employee_df['Experience'].fillna(median_experience, inplace=True)
print(f"Missing values in 'Age': {cleaned_employee_df['Age'].isnull().sum()}")
print(f"Missing values in 'Experience': {cleaned_employee_df['Experience'].isnull().sum()}")

# Q8: Drop rows with missing 'JoiningDate' (critical info).
cleaned_employee_df = cleaned_employee_df.dropna(subset=['JoiningDate'])
print(f"Shape after dropping rows with missing 'JoiningDate': {cleaned_employee_df.shape}")

# -----------------------------
# 3. Grouping and Aggregation
# -----------------------------

# Q9: Find the average salary for each department.
avg_salary_by_dept = cleaned_employee_df.groupby('Department')['Salary'].mean()
print("Average salary by department:\n", avg_salary_by_dept)

# Q10: Find the total number of employees in each country.
employee_count_by_country = cleaned_employee_df['Country'].value_counts()
print("Total number of employees by country:\n", employee_count_by_country)

# -----------------------------
# 4. Merging DataFrames
# -----------------------------

# Q11: Merge employee data with department data on 'Department'.
merged_df = pd.merge(cleaned_employee_df, department_df, left_on='Department', right_on='DepartmentName', how='left')
print("Merged employee and department data:\n", merged_df.head())

# Q12: Fill missing 'Location' values in the merged data with 'Unknown'.
merged_df['Location'].fillna('Unknown', inplace=True)
print("Missing values in 'Location' after filling:\n", merged_df['Location'].isnull().sum())

# -----------------------------
# 5. Statistical and Descriptive Analysis
# -----------------------------

# Q13: Find the mean, median, and standard deviation of employee salaries.
mean_salary = cleaned_employee_df['Salary'].mean()
median_salary = cleaned_employee_df['Salary'].median()
std_salary = cleaned_employee_df['Salary'].std()
print(f"Mean Salary: {mean_salary}, Median Salary: {median_salary}, Std Salary: {std_salary}")

# Q14: Count the number of employees in each age group (binned in 10-year intervals).
age_bins = [20, 30, 40, 50, 60, 70]
age_group = pd.cut(cleaned_employee_df['Age'], bins=age_bins)
age_group_count = cleaned_employee_df.groupby(age_group)['EmployeeID'].count()
print("Number of employees by age group:\n", age_group_count)

# -----------------------------
# 6. Data Visualization (Optional)
# -----------------------------

# You can add optional plots here using matplotlib or seaborn.
# Example: Plot distribution of salaries or experience by department.

# Q15: Plot a histogram of employee salaries.
plt.figure(figsize=(8, 6))
sns.histplot(cleaned_employee_df['Salary'], bins=30, kde=True)
plt.title('Salary Distribution')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()

# Q16: Plot a bar graph of employee count by department.
plt.figure(figsize=(8, 6))
cleaned_employee_df['Department'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Employee Count by Department')
plt.xlabel('Department')
plt.ylabel('Count')
plt.show()
