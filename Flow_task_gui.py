from tkinter import * 
import tkinter as tk

#window 
window = tk.Tk()
window.title("Flow Hub Remote")

#title widget
title_main = tk.Label(
    text="Flow GUI",
    foreground = "white", #text color
    background = "black", #background color
    width = 20,
    height = 10
)

#canvas 
canvas_1 = tk.Canvas(window,width=400,height=300)
canvas_1.pack()

#entry box 
entry_1 = tk.Entry(window)
canvas_1.create_window(200,140,window=entry_1)


#kg to lb converter
def kg_to_lb():
    user_input = entry_1.get()
    label_1 = tk.Label(window,text= float(user_input)* 2.2046)
    canvas_1.create_window(200,230,window=label_1)
    
calculate_btn = tk.Button(text="calculate",command=kg_to_lb)
canvas_1.create_window(200,180,window=calculate_btn)
    
    
title_main.pack() #adding the title to the window
window.mainloop()
