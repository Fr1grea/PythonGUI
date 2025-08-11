import tkinter as tk
from tkinter import PhotoImage, font

def update_label():
    user_input = entry.get()
    label.config(text=user_input)

#comment for github test

root = tk.Tk()
root.geometry("500x200") #set window size

#frame
#frame = tk.Frame(root, width = 500, height = 200, bg = "lightblue")
#frame.pack()

#background
backgroundImage = PhotoImage(file='BackgroundImagePy.png')
backgroundLavel = tk.Label(root, image=backgroundImage)
backgroundLavel.place(relwidth=1, relheight=1) #stretch to fill

root.title("Basic GUI Example")

label = tk.Label(root, text="Centered Title", font = ("Times New Roman", 16, "bold"))
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root, text="Update Label", command=update_label)
button.pack(pady=10)

#run the application
root.mainloop()