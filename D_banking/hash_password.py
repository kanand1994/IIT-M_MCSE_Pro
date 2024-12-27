# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 21:08:09 2024

@author: ANAND KUMAR K
"""
import hashlib

# Utility function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Predefined admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD_HASH = hash_password("admin123")  # Admin password (hashed)
