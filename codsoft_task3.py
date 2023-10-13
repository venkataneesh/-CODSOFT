import tkinter as tk
import random
import string

def generate_password(length, complexity):
    characters = ""
    if complexity == 1:
        characters = string.ascii_letters
    elif complexity == 2:
        characters = string.ascii_letters + string.digits
    elif complexity == 3:
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def generate_and_display_password():
    length = int(length_entry.get())
    complexity = int(complexity_entry.get())
    password = generate_password(length, complexity)
    password_text.delete(1.0, tk.END)  
    password_text.insert(tk.END, password)


root = tk.Tk()
root.title("Password Generator")


root.geometry("400x300")


length_label = tk.Label(root, text="Password Length:")
length_entry = tk.Entry(root)
complexity_label = tk.Label(root, text="Complexity Level (1, 2, or 3):")
complexity_entry = tk.Entry(root)
generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password)
password_text = tk.Text(root, height=5, width=40)


length_label.pack()
length_entry.pack()
complexity_label.pack()
complexity_entry.pack()
generate_button.pack()
password_text.pack()


root.mainloop()
