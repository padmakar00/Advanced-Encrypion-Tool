import tkinter as tk
from tkinter import filedialog, messagebox
from encryption_tool import encrypt_file, decrypt_file  # Import the encryption/decryption functions

def select_file():
    file_path = filedialog.askopenfilename(title="Select a File")
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

def encrypt_action():
    file_path = file_entry.get()
    password = password_entry.get()
    if not file_path or not password:
        messagebox.showerror("Error", "Please provide a file path and password")
        return

    try:
        encrypted_file = encrypt_file(file_path, password)
        messagebox.showinfo("Success", f"File encrypted successfully! Saved as {encrypted_file}")
    except Exception as e:
        messagebox.showerror("Error", f"Encryption failed: {e}")

def decrypt_action():
    file_path = file_entry.get()
    password = password_entry.get()
    if not file_path or not password:
        messagebox.showerror("Error", "Please provide a file path and password")
        return

    try:
        decrypted_file = decrypt_file(file_path, password)
        messagebox.showinfo("Success", f"File decrypted successfully! Saved as {decrypted_file}")
    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed: {e}")

# Create the main window
root = tk.Tk()
root.title("Advanced Encryption Tool")

# File selection
file_label = tk.Label(root, text="Select File:")
file_label.grid(row=0, column=0, padx=10, pady=5)

file_entry = tk.Entry(root, width=40)
file_entry.grid(row=0, column=1, padx=10, pady=5)

select_button = tk.Button(root, text="Browse", command=select_file)
select_button.grid(row=0, column=2, padx=10, pady=5)

# Password input
password_label = tk.Label(root, text="Enter Password:")
password_label.grid(row=1, column=0, padx=10, pady=5)

password_entry = tk.Entry(root, show="*", width=40)
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Buttons for encryption and decryption
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_action)
encrypt_button.grid(row=2, column=0, padx=10, pady=5)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_action)
decrypt_button.grid(row=2, column=1, padx=10, pady=5)

root.mainloop()
