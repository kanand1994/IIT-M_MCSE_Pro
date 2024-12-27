# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 21:17:25 2024

@author: ANAND KUMAR K
"""
import os
from load_accounts import load_accounts
from save_accounts import save_accounts

TRANSACTIONS_FILE = "transactions.txt"
# Admin panel functions
def view_all_accounts():
    accounts = load_accounts()
    if not accounts:
        print("No accounts found.")
        return
    print("\nAll Accounts:")
    for acc_number, details in accounts.items():
        print(f"Account Number: {acc_number}, Name: {details['name']}, Balance: {details['balance']}")

def view_transactions():
    if not os.path.exists(TRANSACTIONS_FILE):
        print("No transactions found.")
        return
    print("\nTransaction History:")
    with open(TRANSACTIONS_FILE, "r") as file:
        for line in file:
            print(line.strip())

def delete_account():
    account_number = input("Enter the account number to delete: ")
    accounts = load_accounts()

    if account_number not in accounts:
        print("Account not found.")
        return

    del accounts[account_number]
    save_accounts(accounts)
    print(f"Account {account_number} has been deleted.")

# Admin menu
def admin_menu():
    while True:
        print("\nAdmin Panel:")
        print("1. View All Accounts")
        print("2. View Transactions")
        print("3. Delete Account")
        print("4. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_all_accounts()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            delete_account()
        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")