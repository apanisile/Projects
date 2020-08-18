import tkinter as tk
from tkinter import *

# Function to convert weight 
# given in kg to grams, pounds 
# and ounces 
def convert(): 
      
    # convert kg to gram 
    gram = float(entry2_value.get())*1000
      
    # convert kg to pound 
    pound = float(entry2_value.get())*2.20462 
      
    # convert kg to ounce 
    ounce = float(entry2_value.get())*35.274 
      
    # Enters the converted weight to  
    # the text widget 
    text1.delete("1.0", END) 
    text1.insert(END,gram) 
      
    text2.delete("1.0", END) 
    text2.insert(END,pound) 
      
    text3.delete("1.0", END) 
    text3.insert(END,ounce) 
  

HEIGHT = 300
WIDTH = 800
root = tk.Tk()

canvas = tk.Canvas(root, height= HEIGHT, width= WIDTH)
canvas.pack()


labelframe = tk.LabelFrame(root, text="Weight converter", bg='#80c1ff')
labelframe.place(relx=0.06, rely=0.01, relheight= 0.8, relwidth = 0.8)

label = tk.Label(labelframe, text = "Enter your weight:")

entry3 = Label(labelframe, text = 'Gram') 
entry4 = Label(labelframe, text = 'Pounds') 
entry5 = Label(labelframe, text = 'Ounce') 

#Create the button widget
button = tk.Button(labelframe, text="Check weight", command = convert)

#Empty text boxes to be filled
text1 = Text(labelframe, height = 1, width = 20) 
text2 = Text(labelframe, height = 1, width = 20) 
text3 = Text(labelframe, height = 1, width = 20) 


#grids
label.grid(row=0, column=0)

entry3.grid(row=1, column=0) 
entry4.grid(row=1, column=1) 
entry5.grid(row=1, column = 2)
text1.grid(row = 2, column = 0) 
text2.grid(row = 2, column = 1) 
text3.grid(row = 2, column = 2) 
button.grid(row=0, column=2)



root.mainloop()