import numpy as np
import pandas as pd

employee_names = ["Aarav", "Priya", "Rohan", "Sneha", "Vikram", "Ananya", "Karthik", "Meera"]
salaries = np.array([45000, 72000, 58000, 85000, 61000, 52000, 95000, 64000])

avg_salary = np.mean(salaries)
max_salary = np.max(salaries)
min_salary = np.min(salaries)

print(f"Average Salary: ₹{avg_salary:.2f}")
print(f"Maximum Salary: ₹{max_salary}")
print(f"Minimum Salary: ₹{min_salary}")

df = pd.DataFrame({
    "Employee Name": employee_names,
    "Salary": salaries
})

print("\nAll Employees:")
print(df)

high_earners = df[df["Salary"] > 60000]
print("\nEmployees earning more than ₹60,000:")
print(high_earners)
