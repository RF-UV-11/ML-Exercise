# data_gen.py
import pandas as pd
from faker import Faker
import random
import numpy as np

# Initialize Faker
fake = Faker()

# Set random seed for reproducibility
random.seed(42)
np.random.seed(42)

# Generate synthetic employee data with some missing values
def generate_employee_data(num_records=1000):
    data = {
        "EmployeeID": [i for i in range(1, num_records + 1)],
        "Name": [fake.name() for _ in range(num_records)],
        "Age": [random.randint(22, 60) for _ in range(num_records)],
        "Department": [random.choice(['HR', 'IT', 'Finance', 'Sales', 'Marketing']) for _ in range(num_records)],
        "Salary": [round(random.uniform(40000, 120000), 2) for _ in range(num_records)],
        "JoiningDate": [fake.date_between(start_date='-10y', end_date='today') for _ in range(num_records)],
        "Gender": [random.choice(['Male', 'Female', 'Other']) for _ in range(num_records)],
        "Experience": [random.randint(1, 35) for _ in range(num_records)],
        "Country": [random.choice(['USA', 'UK', 'Canada', 'Germany', 'India']) for _ in range(num_records)]
    }
    
    # Create DataFrame
    df = pd.DataFrame(data)

    # Introduce random missing data in 'Salary', 'Age', 'Experience', and 'Department'
    for col in ['Salary', 'Age', 'Experience', 'Department']:
        df.loc[df.sample(frac=0.05).index, col] = None  # 5% missing values for these columns
    
    return df

# Generate synthetic department data with some missing values
def generate_department_data():
    department_data = {
        "DepartmentID": [1, 2, 3, 4, 5],
        "DepartmentName": ['HR', 'IT', 'Finance', 'Sales', 'Marketing'],
        "Manager": [fake.name() for _ in range(5)],
        "Location": [random.choice(['New York', 'London', 'Toronto', 'Berlin', 'Mumbai']) for _ in range(5)]
    }

    df_dept = pd.DataFrame(department_data)
    
    # Introduce missing values for 'Location'
    df_dept.loc[df_dept.sample(frac=0.20).index, 'Location'] = None  # 20% missing in Location

    return df_dept

# Save to CSV
def save_to_csv(dataframe, filename):
    dataframe.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

# Main function to generate and save the data
if __name__ == "__main__":
    num_records = 1000  # Number of records to generate
    employee_df = generate_employee_data(num_records)
    department_df = generate_department_data()
    
    save_to_csv(employee_df, "employee_data.csv")
    save_to_csv(department_df, "department_data.csv")
