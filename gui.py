from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import askcolor
import tkinter as tk
from PIL import Image, ImageTk


class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("500x700")
        self.window.title("Community Pixel Art")

        self.Pokemon = Image.open('init.png')
        self.PacGrid = Image.open('GridPacman.png')
        #Pepe = Image.open("PEPE.png")
        self.Upscale_Pokeball = self.Pokemon.resize((450,450),resample=Image.NEAREST)
        self.Upscale_Grid = self.PacGrid.resize((475,475),resample=Image.NEAREST)
        self.Upscale_Grid.paste(self.Upscale_Pokeball, (28, 28), self.Upscale_Pokeball)

        self.display = ImageTk.PhotoImage(self.Upscale_Grid)

        self.color_var= tk.StringVar()
        self.x_var= tk.StringVar()
        self.y_var= tk.StringVar()

        self.label = Label(self.window, image=self.display)
        self.x_label = Label(self.window, text = 'X', font=('calibre',20, ))
        self.y_label = Label(self.window, text = 'Y', font=('calibre',20, ))
        self.color_label = Label(self.window, text = 'Color', font=('calibre',20, ))

        self.x_entry = Entry(self.window,textvariable = self.x_var, font=('calibre',20,'normal'))
        self.y_entry = Entry(self.window,textvariable = self.y_var, font=('calibre',20,'normal'))


        #label.image = display
        self.label.pack()
        self.label.place(anchor = 'center', relx=0.5, rely=0.4)
        self.x_label.place(relx=0.02,rely=.75)
        self.x_entry.place(relx =0.2, rely = .75)
        self.y_label.place(relx=0.02,rely=.81)
        self.y_entry.place(relx =0.2, rely = .81)
        
        self.send_btn=Button(self.window,text = 'Send', command = self.submit)
        
        self.send_btn.place(relx=0.02, rely=.87)
        
        # self.change_img()
        
        self.window.mainloop()
    
    def send_bits(self):
        x = self.x_var.get()
        y = self.y_var.get()
        
        x = int(x) - 1
        y = int(y) - 1
        
        if x < 0 or x > 15 or y < 0 or y > 15:
            x = -1
            y = -1
        
        #Send Variables to server
        self.x_var.set("")
        self.y_var.set("")
        
        return x, y
    
    def submit(self):
        pass

    def change_img(self):
        # Pokemon = Image.open('test.png')
        
        Pepe = Image.open('test.png')
        PacGrid = Image.open('GridPacman.png')
        
        Upscale_Pokeball = Pepe.resize((450,450),resample=Image.NEAREST)
        Upscale_Grid = PacGrid.resize((475,475),resample=Image.NEAREST)
        Upscale_Grid.paste(Upscale_Pokeball, (28, 28), Upscale_Pokeball)
        
        Upscale_Grid = ImageTk.PhotoImage(Upscale_Grid)
        self.label.configure(image=Upscale_Grid)
        self.label.image=Upscale_Grid



# Var = input()

# if Var == "1":
#     change_img()

# #window.mainloop()


