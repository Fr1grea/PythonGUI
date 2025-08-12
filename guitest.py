import tkinter as tk
import subprocess
from tkinter import PhotoImage, font

root = tk.Tk()
root.geometry("500x145") #set window size

#background
backgroundImage = PhotoImage(file='BackgroundImagePy.png')
backgroundLavel = tk.Label(root, image=backgroundImage)
backgroundLavel.place(relwidth=1, relheight=1) #stretch to fill

root.title("Basic GUI Example")

label = tk.Label(root, text="Automation Scripts", font = ("Times New Roman", 16, "bold"))
label.pack(pady=15)

#scripts
def runAutomationScript():
   subprocess.run(['./root/harvester test/Automation.sh'])

def runDestroyScript():
    subprocess.run(['./root/harvester test/Destroy.sh'])

#buttons
button1 = tk.Button(root, 
                    text="Automation Script",
                    font = ("Times New Roman", 12),
                    bg = "white",
                    fg = "darkblue",
                    width = 10,
                    height = 1,
                    padx = 20,
                    pady = 1,
                    relief = "raised",
                    command = runAutomationScript)
button1.pack(pady=10)
button1.place(x=65, y = 80)


button2 = tk.Button(root, 
                    text="Destroy Script",
                    font = ("Times New Roman", 12),
                    bg = "white",
                    fg = "darkblue",
                    width = 10,
                    height = 1,
                    padx = 20,
                    pady = 1,
                    relief = "raised",
                    command = runDestroyScript)
button2.pack(pady=10)
button2.place(x=300, y = 80)

#run the application
root.mainloop()