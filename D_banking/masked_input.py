# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 09:04:16 2024

@author: ANAND KUMAR K
"""
import keyboard

def masked_input(prompt=''):
    password = []
    print(prompt, end='', flush=True)
    while True:
        event = keyboard.read_event()  # Wait for a key press
        if event.event_type == keyboard.KEY_DOWN:  # Only handle key down events
            char = event.name
            if char == 'enter':  # End input on Enter key
                break
            elif char == 'backspace':  # Handle backspace
                if password:
                    password.pop()  # Remove last character
                    print('\b \b', end='', flush=True)  # Delete the * on screen
            elif len(char) == 1:  # Only process characters (not special keys)
                password.append(char)
                print('*', end='', flush=True)  # Print a * for each typed character

    print()  # Move to the next line after password input
    return ''.join(password)