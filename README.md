# Banking-Automation-System
Developed Graphical User Interface (GUI) application using Python and SQL for admin to manage automatic Transaction
Allowing administrators to login, reset passwords, search, update and delete existing databases with a single click
Web Application was made in Python using HTML, CSS at frontend embedded with SQL to connect database

This project is a simple banking automation application using Tkinter for GUI and SQLite for database management. The application allows users to create and manage accounts, log in, view account details, update profiles, and perform basic banking transactions.

Database Design Table: accounts The accounts table is designed to store essential information about each user account.

acn: Account number, an integer that serves as the primary key with auto-increment. name: User's full name, stored as text. pass: Password for account login, stored as text. email: User's email address, stored as text. mob: User's mobile number, stored as text. bal: Account balance, stored as a floating-point number. type: Account type (e.g., "Saving" or "Current"), stored as text. opendate: Date of account creation, stored as text. Features Account Creation: Users can create a new account by entering required information. Login: Users log in with their account number and password. Forgot Password: Users can recover their password by providing account number, email, and mobile number. Account Details: View account number, balance, type, and opening date. Profile Update: Users can update their name, password, email, and mobile number. Deposit: Users can deposit an amount to their account balance. Withdraw: Users can withdraw an amount from their account balance if funds are sufficient. Transfer: Users can transfer money to another account within the system. Project Structure Database Initialization: The SQLite database is initialized upon running the code, creating the accounts table if it doesn't already exist. GUI: The Tkinter library is used to create a user-friendly graphical interface. Functions: newuserscreen(): Handles new account creation. login(): Authenticates users based on account number and password. fpscreen(): Allows users to retrieve their password. homescreen(): Main menu after logging in, offering options for viewing details, updating profile, deposit, withdraw, and transfer. details(), profile(), deposit(), withdraw(), transfer(): Each function performs the corresponding action for logged-in users. Setup Install Dependencies:

Tkinter: GUI library for Python. SQLite: Included with Python but requires sqlite3 for database operations. Run the Application:

Run the Python script directly. The main window will open, allowing you to interact with the application. Database:

A SQLite database (banking.sqlite) will be created in the local directory. Future Improvements Enhanced Security: Implement hashing for passwords. Additional Account Types: Add more options for account types. Transaction History: Track deposits, withdrawals, and transfers.
