from tkinter import * 
import tkinter as tk


window = tk.Tk()
window.geometry("500x300")
#add widget codes here

#title widget
title_main = tk.Label(
    text="KG to LB converter",
    foreground = "white", #text color
    background = "black", #background color
    width = 20,
    height = 10
)

#buttons

b1 = Button(window, text="Calculate")
b2 = Button(window, text="Clear")

title_main.pack() #adding the title to the window
b1.pack(side=LEFT)
b2.pack(side=LEFT)
window.mainloop()
