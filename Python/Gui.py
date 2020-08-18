import tkinter as tk


HEIGHT = 300
WIDTH = 400
root = tk.Tk()

canvas = tk.Canvas(root, height= HEIGHT, width= WIDTH)
canvas.pack()



labelframe = tk.LabelFrame(root, text="Weight converter")
labelframe.pack(fill="both", expand="yes")

button = tk.Button(labelframe, text="Check weight")
button.pack(fill='x')

entry = tk.Entry(labelframe, bg='grey')
entry.pack()

label = tk.Label(labelframe, text = "Enter your weight:")
label.pack(side='left')

root.mainloop()