# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 22:00:00 2024

@author: ANAND KUMAR K
"""

from create_account import create_account
from load_accounts import load_accounts
from transaction import deposit,withdraw,check_balance
from login import login
from admin_login import admin_login
from admin import admin_menu


# Main function to run the banking system
def main():
    accounts = load_accounts()
    while True:
        print("Welcome to the E_D Banking System!")
        print("1. Create Account")
        print("2. Login")
        print("3. Banking Login")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            create_account(accounts)
        elif choice == '2':
            account_number = login(accounts)
            if account_number:
                while True:
                    print("\nAccount Menu:")
                    print("1. Check Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Logout")
                    operation_choice = input("Enter your choice: ")

                    if operation_choice == '1':
                        check_balance(accounts, account_number)
                    elif operation_choice == '2':
                        deposit(accounts, account_number)
                    elif operation_choice == '3':
                        withdraw(accounts, account_number)
                    elif operation_choice == '4':
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice, please try again.")
        elif choice == '3':
            if admin_login():
                admin_menu()
        elif choice == '4':
            print("Thank you for using the banking system!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()