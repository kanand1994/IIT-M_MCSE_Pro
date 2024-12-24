# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 09:01:28 2024

@author: ANAND KUMAR K
"""
import time
from save_accounts import save_accounts

TRANSACTIONS_FILE = 'transactions.txt'
# Helper function to log transactions
def log_transaction(account_number, transaction_type, amount):
    transaction_id = int(time.time())  # Simple unique transaction ID based on timestamp
    transaction_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(transaction_id))
    with open(TRANSACTIONS_FILE, 'a') as file:
        file.write(f"{transaction_id}, {account_number}, {transaction_type}, {amount}, {transaction_time}\n")

# Function to deposit money into an account
def deposit(accounts, account_number):
    print("Enter the amount to deposit:")
    amount = float(input())

    # Update the account balance
    accounts[account_number]['balance'] += amount

    # Log the transaction
    log_transaction(account_number, "Deposit", amount)

    # Save updated account information
    save_accounts(accounts)
    print(f"Deposited {amount} to your account. New balance: {accounts[account_number]['balance']}")

# Function to withdraw money from an account
def withdraw(accounts, account_number):
    print("Enter the amount to withdraw:")
    amount = float(input())

    # Check if the user has enough balance
    if amount <= accounts[account_number]['balance']:
        accounts[account_number]['balance'] -= amount
        log_transaction(account_number, "Withdrawal", amount)
        save_accounts(accounts)
        print(f"Withdrew {amount} from your account. New balance: {accounts[account_number]['balance']}")
    else:
        print("Insufficient balance!")

# Function to check balance
def check_balance(accounts, account_number):
    print(f"Your current balance is: {accounts[account_number]['balance']}")
