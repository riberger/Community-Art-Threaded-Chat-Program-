from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk


window = Tk()
window.geometry("500x700")
window.title("Community Pixel Art")



Pokemon = Image.open('init.png')
PacGrid = Image.open('GridPacman.png')
#Pepe = Image.open("PEPE.png")
Upscale_Pokeball = Pokemon.resize((450,450),resample=Image.NEAREST)
Upscale_Grid = PacGrid.resize((475,475),resample=Image.NEAREST)
Upscale_Grid.paste(Upscale_Pokeball, (28, 28), Upscale_Pokeball)

display = ImageTk.PhotoImage(Upscale_Grid)

color_var= tk.StringVar()
x_var= tk.StringVar()
y_var= tk.StringVar()

label = Label(window, image=display)
x_label = Label(window, text = 'X', font=('calibre',20, ))
y_label = Label(window, text = 'Y', font=('calibre',20, ))
color_label = Label(window, text = 'Color', font=('calibre',20, ))

x_entry = Entry(window,textvariable = x_var, font=('calibre',20,'normal'))
y_entry = Entry(window,textvariable = y_var, font=('calibre',20,'normal'))
color_entry = Entry(window,textvariable = color_var, font=('calibre',20,'normal'))


#label.image = display
label.pack()
label.place(anchor = 'center', relx=0.5, rely=0.4)
x_label.place(relx=0.02,rely=.75)
x_entry.place(relx =0.2, rely = .75)
y_label.place(relx=0.02,rely=.81)
y_entry.place(relx =0.2, rely = .81)
color_label.place(relx=0.02,rely=.87)
color_entry.place(relx = 0.2, rely= .87)




def submit():
    color= color_var.get()
    x = x_var.get()
    y = y_var.get()
     
    #Send Variables to server

    x_var.set("")
    y_var.set("")
    color_var.set("")

send_btn=Button(window,text = 'Send', command = submit)

def change_img():
   Pepe=ImageTk.PhotoImage(Image.open("PEPE.png"))
   label.configure(image=Pepe)
   label.image=Pepe

Var = input()

if Var == "1":
    change_img()

#window.mainloop()


