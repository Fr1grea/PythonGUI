import tkinter as tk
import subprocess
from tkinter import PhotoImage, font
from tkinter.font import Font

root = tk.Tk()
root.geometry("500x160") #set window size
root.resizable(False, False)

#BAH Colors
strongCyan = "#00a5b5"
electricGreen = "#bad63a"
darkCyan = "#00838F"
magenta = "#e55ed6"
lightCyan = "#23d2d7"


#background
backgroundImage = PhotoImage(file='for_the_slide_show.png')
backgroundLavel = tk.Label(root, image=backgroundImage)
backgroundLavel.place(relwidth=1, relheight=1) #stretch to fill


root.title("Automation GUI")

label = tk.Label(root, text="Automation Scripts", font = ("Constantia", 16, "bold"), fg = darkCyan, bg="white",borderwidth = 0, highlightthickness=0)
label.pack(pady=15)

#scripts
def runAutomationScript():
  subprocess.run(['./automation.sh'])

def runDestroyScript():
   subprocess.run(['./destroy.sh'])


#buttons
image1 = PhotoImage(file = "buttonCreate.png")

createButton = tk.Button(root, 
                    image = image1,
                    command = runAutomationScript
                    )
createButton.pack(pady=10)
createButton.place(x=30, y = 65)

image2 = PhotoImage(file = "destroyButton.png")

destroyButton = tk.Button(root, 
                    image = image2,
                    command = runDestroyScript
                    )
destroyButton.pack(pady=10)
destroyButton.place(x=270, y = 65)

#run the application
root.mainloop()