# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 09:05:15 2024

@author: ANAND KUMAR K
"""
from masked_input import masked_input
import bcrypt

# Function to login a user
def login(accounts):
    print("Enter your account number:")
    account_number = input()
    #print("Enter your password:")
    password = masked_input("Enter your password: ")

    if account_number in accounts:
        # Retrieve the stored password hash
        stored_hash = accounts[account_number]['password_hash']

        # Compare the entered password with the stored hash
        if bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8')):
            print(f"Welcome back, {accounts[account_number]['name']}!")
            return account_number
        else:
            print("Invalid password. Please try again.")
            return None
    else:
        print("Invalid account number. Please try again.")
        return None