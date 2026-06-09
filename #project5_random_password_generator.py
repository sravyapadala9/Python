# Project 5 - Random Password Generator

import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password = ""

for i in range(8):
    password += random.choice(characters)

print("Generated Password:", password)