import tkinter as tk
win = tk.Tk()
win.title("welcom to python.hub")
var = tk.IntVar()
class1 = tk.Radiobutton(win, text="one", value=1, variable=var).pack()
class2 = tk.Radiobutton(win, text="two", value=1, variable=var).pack()
class3 = tk.Radiobutton(win, text="three", value=1, variable=var).pack()
win.mainloop()