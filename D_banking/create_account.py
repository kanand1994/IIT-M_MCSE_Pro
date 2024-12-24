# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 08:53:29 2024

@author: ANAND KUMAR K
"""
from masked_input import masked_input
import time
import bcrypt
from save_accounts import save_accounts
# Function to create a new account
def create_account(accounts):
    print("Enter your name:")
    name = input()
    #print("Enter your password:")
    password = masked_input("Enter your password: ")
    print("Enter the initial deposit amount:")
    initial_balance = float(input())

    # Hash the password
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # Generate a unique account number (using current timestamp for simplicity)
    account_number = str(int(time.time()))

    # Add the account to the accounts dictionary
    accounts[account_number] = {
        'name': name,
        'password_hash': password_hash,
        'balance': initial_balance
    }

    # Save the new account to the file
    save_accounts(accounts)
    print(f"Account created successfully! Your account number is {account_number}")
