import tkinter as tk

def update_label():
    user_input = entry.get()
    label.config(text=user_input)

root = tk.Tk()
root.title("Basic GUI Example")

label = tk.Label(root, text="Enter something: ")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root, text="Update Label", command=update_label)
button.pack(pady=10)

root.mainloop()