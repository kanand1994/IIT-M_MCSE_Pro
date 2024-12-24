# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 08:59:09 2024

@author: ANAND KUMAR K
"""
ACCOUNTS_FILE = 'accounts.txt'

# Helper function to save all accounts to the file
def save_accounts(accounts):
    with open(ACCOUNTS_FILE, 'w') as file:
        for account_number, account_info in accounts.items():
            file.write(f"{account_number}, {account_info['name']}, {account_info['password_hash']}, {account_info['balance']}\n")
