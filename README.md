# IIT-M_MCSE_Pro
**E-D Banking: Console-based Online Banking System**
E-D Banking is a simple, console-based banking application that simulates the functionalities of a real banking system. It provides core banking features like account management, transaction handling, and account activity for both the administrator and customers. The system is built using Python and a text-based interface.

**Features**
**Admin Features**
Manage Accounts: The admin can create new customer accounts, view customer details, and deactivate accounts.
Transaction Monitoring: Admin can view the details of all transactions, including deposits, withdrawals, and transfers.

**User (Customer) Features**
Account Overview: Customers can view their balance, recent transactions, and account details.
Deposit Funds: Customers can deposit money into their accounts.
Withdraw Funds: Customers can withdraw money from their accounts.
Transfer Funds: Customers can transfer money to another account within the same bank.

**Console-based Interface**
Text-based UI: The system uses a command-line interface (CLI) for interaction, where users input commands to perform various actions.

**Tech Stack**
Backend: Python (No external web framework, designed as a console-based application)
Data Storage: Txt or JSON files for persistent data storage
Authentication: Password Masked, encoded and hashed login for both admin and customer accounts

**Core Components**
Admin Module: Responsible for managing customers, viewing transactions.
Customer Module: Provides functionalities like account overview, deposits, withdrawals, and transfers.
Bank Module: Handles the logic for processing transactions and managing accounts.

**Console Commands**

**Admin Commands**
view_account_details <account_number>: View details of a specific customer account.
view_all_transactions: View all transactions in the bank system.

**Customer Commands**
check_balance: Check current account balance.
deposit <amount>: Deposit funds into the account.
withdraw <amount>: Withdraw funds from the account.
transfer <amount> <recipient_account>: Transfer funds to another customer.
transaction_history: View a history of transactions on the account.

**Security and Authentication**
Masked login: To access both admin and customer modules, the user must input a valid password. Each account (admin or customer) has a unique password.

**Example Interaction**

Welcome to E-D Banking System!

1. Create Account
2. Login
3. Banking Login
4. Exit
Enter choice: 1

Enter your name:
AK
Enter your password: *****
Enter the initial deposit amount:
1000
Account created successfully! Your account number is 1735307011(Auto-Genereted)

Enter admin username: admin
Enter admin password: ********
Admin login successful!

Admin Panel:
1. View All Accounts
2. View Transactions
3. Delete Account
4. Logout
Enter your choice: 4
Logging out...

1. Create Account
2. Login
3. Banking Login
4. Exit
Enter choice: 2

Enter your choice: 2
Enter your account number:
1735307011
Enter your password: *****
Welcome back, AK!

Account Menu:
1. Check Balance
2. Deposit
3. Withdraw
4. Logout
Enter your choice: 4
Logging out...

1. Create Account
2. Login
3. Banking Login
4. Exit
Enter your choice: 4
Thank you for using the banking system!

**Run Locally**
1. Clone the repository
git clone https://github.com/nz-m/eD-Banking.git

2. Navigate to the project directory
cd eD-Banking

3. Install Dependencies
There are no external dependencies for this console-based banking system, as it uses standard Python libraries for file handling and data storage.

4. Run the Program
python main.py

This will start the banking system, and you will be prompted the menus and enter your choice.


Feel free to fork the repository, submit issues, and open pull requests for improvements, new features, or bug fixes. Contributions are welcome!
