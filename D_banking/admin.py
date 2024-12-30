# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 21:17:25 2024

@author: ANAND KUMAR K
"""
import os
from load_accounts import load_accounts
from save_accounts import save_accounts
from admin_transaction import log_admin_transaction,ADMIN_TRANSACTIONS_FILE
from admin_login import ADMIN_USERNAME
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

def view_admin_transactions():
    if not os.path.exists(ADMIN_TRANSACTIONS_FILE):
        print("No admin transactions found.")
        return
    print("\nAdmin Transaction History:")
    with open(ADMIN_TRANSACTIONS_FILE, "r") as file:
        for line in file:
            print(line.strip())

# Function to delete an account
def delete_account():
    account_number = input("Enter the account number to delete: ")
    accounts = load_accounts()

    if account_number not in accounts:
        print("Account not found.")
        return

    reason = input("Enter reason for deleting the account: ")
    
    # Log the account deletion in the admin transaction file
    log_admin_transaction(ADMIN_USERNAME, "Delete Account", account_number, reason)
    
    # Remove the account from the account data
    del accounts[account_number]
    save_accounts(accounts)
    print(f"Account {account_number} has been deleted and the reason has been recorded.")


# Admin menu
def admin_menu():
    while True:
        print("\nAdmin Panel:")
        print("1. View All Accounts")
        print("2. View Transactions")
        print("3. View Admin Transactions (Account Deletions)")
        print("4. Delete Account")
        print("5. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_all_accounts()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            view_admin_transactions()
        elif choice == "4":
            delete_account()
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")
