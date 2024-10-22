import numpy as np
from faker import Faker

# Initialize Faker
fake = Faker()

def generate_user_data(num_entries=1000):
    """
    Generates a dataset of random user data including name, age, income, and country.
    """
    data = {
        "name": [],
        "age": [],
        "income": [],
        "country": []
    }
    
    for _ in range(num_entries):
        data["name"].append(fake.name())
        data["age"].append(np.random.randint(18, 80))  # Random age between 18 and 80
        data["income"].append(np.random.randint(30000, 150000))  # Random income
        data["country"].append(fake.country())
    
    # Convert to NumPy array
    names = np.array(data["name"])
    ages = np.array(data["age"])
    incomes = np.array(data["income"])
    countries = np.array(data["country"])
    
    return names, ages, incomes, countries

if __name__ == "__main__":
    names, ages, incomes, countries = generate_user_data(1000)
    np.savez("user_data.npz", names=names, ages=ages, incomes=incomes, countries=countries)
    print("Data generated and saved to 'user_data.npz'")
