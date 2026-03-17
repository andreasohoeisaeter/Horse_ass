# Importing keyboard module

import keyboard

# Print welcome message

print("Welcome to the horse race!\n")

# ASCII lol?

print("--oooo/-")
print("  | |  ")
print("\n")

# Printing guideliens

print("Press 'SPACE' for action, 'M' for control! 'ESC' for quitting.\n")

# Function for speed

def galopp():
    print("-")

keyboard.add_hotkey('space', galopp)

# Function for control

def control():
    print(">")

keyboard.add_hotkey('m', control)

# To quit

keyboard.wait('esc')

