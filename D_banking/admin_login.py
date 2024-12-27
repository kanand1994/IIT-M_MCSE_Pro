# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 21:11:26 2024

@author: ANAND KUMAR K
"""
from hash_password import hash_password,ADMIN_USERNAME,ADMIN_PASSWORD_HASH
from masked_input import masked_input
# Admin login function
def admin_login():
    username = input("Enter admin username: ")
    password = masked_input("Enter admin password: ")
    
    if username == ADMIN_USERNAME and hash_password(password) == ADMIN_PASSWORD_HASH:
        print("Admin login successful!")
        return True
    else:
        print("Invalid admin credentials!")
        return False