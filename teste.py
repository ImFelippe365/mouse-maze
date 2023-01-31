from tkinter import *

class Application:
    def __init__(self, master = None): 
        self.master = master 
        
        self.create() 
    def create(self): 
        
        self.canvas = Canvas(self.master) 
        for x in range(20):
            prev = x*15 - 15 if not x == 0 else 0
            print(prev, x*15)
            self.canvas.create_rectangle(prev, 15, x*15, 0,outline="blue", fill = "blue", 
                                width = 1)
        for x in range(20):
            prev = x*15 - 15 if not x == 0 else 0
            print(prev, x*15)
            self.canvas.create_rectangle(0, x*15, 15, prev, outline="blue", fill = "blue", 
                                width = 1)

        self.canvas.pack(fill = BOTH, expand = 1) 
root = Tk()
Application(root)
root.mainloop()