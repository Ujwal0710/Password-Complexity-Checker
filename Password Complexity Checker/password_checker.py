import re
import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    """
    Checks the strength of a password based on the following criteria:
    - Length: At least 8 characters
    - Uppercase letters: At least one
    - Lowercase letters: At least one
    - Numbers: At least one
    - Special characters: At least one
    """
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")

    if re.search(r"[^a-zA-Z0-9\s]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character.")

    if strength == 5:
        return "Strong password", []
    elif strength >= 3:
        return "Moderate password", feedback
    else:
        return "Weak password", feedback

def check_button_click():
    """Handles the check button click event."""
    password = password_entry.get()
    strength, feedback = check_password_strength(password)

    if strength == "Strong password":
        messagebox.showinfo("Password Strength", "Strong password")
    else:
        messagebox.showinfo("Password Strength", f"Password strength: {strength}\nSuggestions:\n" + "\n".join(feedback))

# Create the main window
root = tk.Tk()
root.title("Password Checker")

# Password label and entry
password_label = tk.Label(root, text="Password:")
password_label.grid(row=0, column=0, padx=10, pady=10)

password_entry = tk.Entry(root, width=40, show="*")
password_entry.grid(row=0, column=1, padx=10, pady=10)

# Check button
check_button = tk.Button(root, text="Check", command=check_button_click)
check_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Run the main loop
root.mainloop()
