import tkinter as tk
from tkinter import PhotoImage, font

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

#me when i customized buttons
button1 = tk.Button(root, 
                    text="Button 1",
                    font = ("Times New Roman", 13),
                    bg = "white",
                    fg = "darkblue",
                    padx = 25,
                    pady = 5,
                    relief = "raised"
                    )
button1.pack(pady=10, padx = 10)

button2 = tk.Button(root, 
                    text="Button 2",
                    font = ("Times New Roman", 13),
                    bg = "white",
                    fg = "darkblue",
                    padx = 25,
                    pady = 5,
                    relief = "raised")
button2.pack(pady=10)

#run the application
root.mainloop()