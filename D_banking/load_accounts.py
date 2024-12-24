# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 08:55:11 2024

@author: ANAND KUMAR K
"""
import os

ACCOUNTS_FILE = 'accounts.txt'

# Helper function to read all accounts from the file
def load_accounts():
    accounts = {}
    if os.path.exists(ACCOUNTS_FILE):
        with open(ACCOUNTS_FILE, 'r') as file:
            for line in file:
                account_number, name, password_hash, balance = line.strip().split(', ')
                accounts[account_number] = {
                    'name': name,
                    'password_hash': password_hash,
                    'balance': float(balance)
                }
    return accounts