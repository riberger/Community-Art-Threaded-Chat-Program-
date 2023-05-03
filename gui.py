from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import askcolor
import tkinter as tk
from PIL import Image, ImageTk


class GUI:
    def __init__(self):
        #Creates Window/Canvas Object
        self.window = Tk()
        self.window.geometry("500x700")
        self.window.title("Community Pixel Art")

        #Opens the two starter images
        self.Pokemon = Image.open('init.png')
        self.PacGrid = Image.open('GridPacman.png')
        
        #Upscales the two images and combines the pokeball image with the grid
        self.Upscale_Pokeball = self.Pokemon.resize((450,450),resample=Image.NEAREST)
        self.Upscale_Grid = self.PacGrid.resize((475,475),resample=Image.NEAREST)
        self.Upscale_Grid.paste(self.Upscale_Pokeball, (28, 28), self.Upscale_Pokeball)
        self.display = ImageTk.PhotoImage(self.Upscale_Grid)

        #Creates variables for the 3 input fields
        self.color_var= tk.StringVar()
        self.x_var= tk.StringVar()
        self.y_var= tk.StringVar()

        #Creates the labels for the text entries and color picker
        self.label = Label(self.window, image=self.display)
        self.x_label = Label(self.window, text = 'X', font=('calibre',20, ))
        self.y_label = Label(self.window, text = 'Y', font=('calibre',20, ))
        self.color_label = Label(self.window, text = 'Color', font=('calibre',20, ))

        #Creates the text entry labels
        self.x_entry = Entry(self.window,textvariable = self.x_var, font=('calibre',20,'normal'))
        self.y_entry = Entry(self.window,textvariable = self.y_var, font=('calibre',20,'normal'))


        #Packs the window with the image, labels, and entries.
        self.label.pack()
        self.label.place(anchor = 'center', relx=0.5, rely=0.4)
        self.x_label.place(relx=0.02,rely=.75)
        self.x_entry.place(relx =0.2, rely = .75)
        self.y_label.place(relx=0.02,rely=.81)
        self.y_entry.place(relx =0.2, rely = .81)
        
        #Creates a button for the Send Function and places it in the window
        self.send_btn=Button(self.window,text = 'Send', command = self.submit)
        self.send_btn.place(relx=0.02, rely=.87)
        
        self.window.mainloop()
    
    '''
    Takes in the data entered in the text entry 
    and the color chosen. Preps them to be sent to over the socket.
    Resets the textfield

    @params
        self
   
    '''
    def send_bits(self):
        #Takes in the values from the fields
        x = self.x_var.get()
        y = self.y_var.get()
        
        #Makes the values 1 indexed for easier display
        x = int(x) - 1
        y = int(y) - 1
        
        if x < 0 or x > 15 or y < 0 or y > 15:
            x = -1
            y = -1
        
        #Resets entry fields to 0 for future use
        self.x_var.set("")
        self.y_var.set("")
        
        return x, y
    
    def submit(self):
        pass

    '''
    Refreshes the canvas to reflect a new image. 
    
    @params
        self
    '''
    def change_img(self):
        
        #Opens the two Images
        Pepe = Image.open('test.png')
        PacGrid = Image.open('GridPacman.png')
        
        #Upscales and combines them
        Upscale_Pokeball = Pepe.resize((450,450),resample=Image.NEAREST)
        Upscale_Grid = PacGrid.resize((475,475),resample=Image.NEAREST)
        Upscale_Grid.paste(Upscale_Pokeball, (28, 28), Upscale_Pokeball)
        
        #Replaces the images in the windows
        Upscale_Grid = ImageTk.PhotoImage(Upscale_Grid)
        self.label.configure(image=Upscale_Grid)
        self.label.image=Upscale_Grid




