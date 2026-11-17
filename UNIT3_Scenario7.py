import csv
import re
import os

FILENAME = "customers.csv"
ACCOUNT_PATTERN = r"^ACC\d{6}$"

def initialize_csv():
    if not os.path.exists(FILENAME):
        sample_customers = [
            {"Account Number": "ACC100001", "Name": "Aarav Sharma", "Account Type": "Savings", "Balance": "54200.50"},
            {"Account Number": "ACC100002", "Name": "Priya Patel", "Account Type": "Current", "Balance": "125000.00"},
            {"Account Number": "ACC100003", "Name": "Rohan Verma", "Account Type": "Savings", "Balance": "32150.75"},
            {"Account Number": "ACC100004", "Name": "Sneha Nair", "Account Type": "Savings", "Balance": "89400.00"},
            {"Account Number": "ACC100005", "Name": "Vikram Rao", "Account Type": "Current", "Balance": "210500.25"}
        ]
        with open(FILENAME, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["Account Number", "Name", "Account Type", "Balance"])
            writer.writeheader()
            writer.writerows(sample_customers)

def read_customers():
    customers = []
    with open(FILENAME, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            customers.append(row)
    return customers

def validate_account_number(acc_num):
    return bool(re.match(ACCOUNT_PATTERN, acc_num.strip()))

def display_all_customers(customers):
    print("\n--- All Customer Records ---")
    for customer in customers:
        print(f"Account Number: {customer['Account Number']} | Name: {customer['Name']} | Type: {customer['Account Type']} | Balance: ₹{customer['Balance']}")

def search_by_account_number(customers, acc_num):
    acc_num = acc_num.strip()
    if not validate_account_number(acc_num):
        print("\nInvalid Account Number format. Expected format: ACC followed by 6 digits (e.g., ACC100001).")
        return

    print(f"\n--- Search Result for Account Number: {acc_num} ---")
    for customer in customers:
        if customer["Account Number"].strip() == acc_num:
            print(f"Account Number: {customer['Account Number']} | Name: {customer['Name']} | Type: {customer['Account Type']} | Balance: ₹{customer['Balance']}")
            return
    print("Customer record not found.")

def main():
    initialize_csv()
    customers = read_customers()

    while True:
        print("\n=== Bank Customer Record System ===")
        print("1. Display all customer details")
        print("2. Search customer by Account Number")
        print("3. Validate Account Number format")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            display_all_customers(customers)
        elif choice == "2":
            acc_num = input("Enter Account Number (e.g., ACC100001): ")
            search_by_account_number(customers, acc_num)
        elif choice == "3":
            acc_num = input("Enter Account Number to validate: ")
            if validate_account_number(acc_num):
                print("Valid Account Number format.")
            else:
                print("Invalid Account Number format. Expected format: ACC followed by 6 digits (e.g., ACC100001).")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
