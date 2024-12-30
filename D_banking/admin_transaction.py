# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 21:04:58 2024

@author: ANAND KUMAR K
"""
import time
# File paths for storing account and transaction data
ADMIN_TRANSACTIONS_FILE = "admin_transactions.txt"  # File for admin transactions


# Function to log admin transactions to a separate file
def log_admin_transaction(admin_username, action, account_number, reason=None):
    with open(ADMIN_TRANSACTIONS_FILE, "a") as file:
        reason_str = f", Reason: {reason}" if reason else ""
        file.write(f"{action},{account_number},{admin_username},{time.strftime('%Y-%m-%d %H:%M:%S')}{reason_str}\n")
