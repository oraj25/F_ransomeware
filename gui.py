#The GUI library in Python. Used to create windows, labels, buttons
import tkinter as tk 

def fake_decrypt(root_window):
    root_window.destroy()

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

    # Decrypt button
    decrypt_button = tk.Button(
        root, text="I've Paid! Decrypt Files", command= lambda: fake_decrypt(root),
        font=("Arial", 16), bg="red", fg="white"
    )
    decrypt_button.pack(pady=20)
    #This line stops the user from closing the window using the "X" button in the corner.
    root.protocol("WM_DELETE_WINDOW", lambda: None)
    root.mainloop()

show_ransom_screen()
