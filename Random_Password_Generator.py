import tkinter as tk
import random
import string

def generate_password():
    pass_len = int(entry_length.get())  # Get the password length from the input field
    char_values = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(char_values) for _ in range(pass_len))
    entry_result.delete(0, tk.END)  # Clear any existing password
    entry_result.insert(0, password)  # Insert the generated password into the entry box

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")

# Create and place widgets
label_prompt = tk.Label(root, text="Enter Length of password:", font=("Arial", 12, "bold"))
label_prompt.pack(pady=5)

entry_length = tk.Entry(root)
entry_length.pack(pady=5)

# Create a larger "Generate Password" button
button_generate = tk.Button(root, text="Generate Password", command=generate_password, width=20, height=2, font=("Arial", 14))
button_generate.pack(pady=5)

# Entry field for displaying the generated password
entry_result = tk.Entry(root, width=30, font=("Arial", 14))
entry_result.pack(pady=20)

# Start the GUI loop
root.mainloop()

