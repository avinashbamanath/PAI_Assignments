
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV dataset
df = pd.read_csv("customer_churn - customer_churn.csv")

# Display basic dataset information
print("First 5 Records:")
print(df.head())

print("\nDataset Shape:", df.shape)
print("\nColumn Names:", df.columns.tolist())
print("\nDataset Information:")
df.info()

# Check and remove duplicates
print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:", df.duplicated().sum())
df = df.drop_duplicates()

# Fill missing values
numeric_columns = df.select_dtypes(include=np.number).columns
categorical_columns = df.select_dtypes(include="object").columns

for col in numeric_columns:
    df[col] = df[col].fillna(df[col].mean())

for col in categorical_columns:
    df[col] = df[col].fillna(df[col].mode()[0])

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Calculate summary statistics
print("\nSummary Statistics:")
print(df.describe())

print("\nAverage Monthly Charges:", np.mean(df["MonthlyCharges"]))
print("Average Customer Tenure:", np.mean(df["Tenure"]))

# Analyze customer churn
print("\nCustomer Churn Count:")
print(df["Churn"].value_counts())

print("\nChurn Percentage:")
print(df["Churn"].value_counts(normalize=True) * 100)

# Plot churn count
df["Churn"].value_counts().plot(kind="bar")
plt.title("Customer Churn Count")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.show()

# Plot monthly charges distribution
plt.hist(df["MonthlyCharges"], bins=10)
plt.title("Distribution of Monthly Charges")
plt.xlabel("Monthly Charges")
plt.ylabel("Number of Customers")
plt.show()

# Plot customer tenure distribution
plt.hist(df["Tenure"], bins=10)
plt.title("Distribution of Customer Tenure")
plt.xlabel("Tenure")
plt.ylabel("Number of Customers")
plt.show()

# Analyze churn by contract type
contract_churn = pd.crosstab(df["Contract"], df["Churn"])
print("\nChurn by Contract:")
print(contract_churn)

contract_churn.plot(kind="bar")
plt.title("Customer Churn by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.show()

# Compare average charges by churn
average_charges = df.groupby("Churn")["MonthlyCharges"].mean()
print("\nAverage Monthly Charges by Churn:")
print(average_charges)

average_charges.plot(kind="bar")
plt.title("Average Monthly Charges vs Churn")
plt.xlabel("Churn")
plt.ylabel("Average Monthly Charges")
plt.xticks(rotation=0)
plt.show()

# Calculate and visualize correlation
correlation = df[numeric_columns].corr()
print("\nCorrelation Matrix:")
print(correlation)

plt.imshow(correlation, cmap="coolwarm")
plt.colorbar()
plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=45)
plt.yticks(range(len(correlation.columns)), correlation.columns)
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()
