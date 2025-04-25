import tkinter as tk
from tkinter import ttk

def menu():
    global rect, rect2
    km_entry.delete(0, 'end')
    km_entry.insert(0, '0')

    mile_entry.delete(0, 'end')
    mile_entry.insert(0, '0')

    metr_to_km_button.place(x=2, y=125)
    rect = canvas.create_rectangle(0, 0, 500, 40, fill='mediumslateblue', outline='mediumslateblue')
    rect2 = canvas.create_rectangle(0, 0, 77, 500, fill='mediumslateblue', outline='mediumslateblue')
    text.place(x=120, y=3)
    channels_button.place(x=2, y=50)
    mile_entry.place_forget()
    mile_text.place_forget()
    km_entry.place_forget()
    km_text.place_forget()
    rest_button.place_forget()
    convert_button.place_forget()
    menu_return_button.place_forget()
    window.config(bg='aliceblue')
    canvas.config(bg='aliceblue')

def mile_to_km_mode():
    km_entry.delete(0, 'end')
    km_entry.insert(0, '0')

    mile_entry.delete(0, 'end')
    mile_entry.insert(0, '0')
    menu_return_button.place(x=135, y=399)
    metr_to_km_button.place_forget()
    canvas.delete(rect, rect2)
    text.place_forget()
    channels_button.place_forget()
    mile_entry.place(x=75, y=100)
    mile_text.place(x=90, y=50)
    km_entry.place(x=300, y=100)
    km_text.place(x=335, y=50)
    rest_button.place(x=300, y=200)
    convert_button.place(x=30, y=200)
    window.config(bg='mediumspringgreen')
    canvas.config(bg='mediumspringgreen')


def convert():
    km = float(km_entry.get())
    mile = float(mile_entry.get())
    tm = km
    km = mile * 1.6
    mile = tm / 1.6

    km_entry.delete(0, 'end')
    km_entry.insert(0, str(km))

    mile_entry.delete(0, 'end')
    mile_entry.insert(0, str(mile))


def rest():
    km_entry.delete(0, 'end')
    km_entry.insert(0, '0')

    mile_entry.delete(0, 'end')
    mile_entry.insert(0, '0')


def show_channels():
    if verb.get() == 'show \n channels':
        verb.set('dont \n show \n channels')
        metr_to_km_button.place(x=2, y=125)
    else:
        verb.set('show \n channels')
        metr_to_km_button.place_forget()

window = tk.Tk()

window.geometry('500x500')
window.title('menu design test')
window.wm_maxsize(500, 500)
window.config(bg='aliceblue')

canvas = tk.Canvas(master=window, height=500, width=500, background='aliceblue')
rect = canvas.create_rectangle(0, 0, 500, 40, fill='mediumslateblue', outline='mediumslateblue')
rect2 = canvas.create_rectangle(0, 0, 77, 500, fill='mediumslateblue', outline='mediumslateblue')
text = ttk.Label(text='menu design test', font='Arial 20 bold', background='mediumslateblue', foreground='white')


text.place(x=120, y=3)

verb = tk.StringVar()
verb.set('show \n channels')


canvas.pack()
metr_to_km_button = tk.Button(
master=window,
    text='  miles \n to \n km',
    width=5,
    font='Arial 16 bold',
    fg='white',
    bg='mediumslateblue',
    borderwidth=0,
    activebackground='mediumslateblue',
    activeforeground='white',
    command=mile_to_km_mode)

channels_button = tk.Button(
master=window,
    text='show \n channels',
    width=7,
    font='Arial 12 bold',
    fg='navy',
    bg='mediumslateblue',
    borderwidth=0,
    activebackground='mediumslateblue',
    activeforeground='navy',
    command=show_channels,
    textvariable=verb)
channels_button.place(x=2, y=50)

mile_entry = tk.Entry(master=window, background='white')
mile_text = ttk.Label(text='miles', font='Arial 20 bold', background='mediumspringgreen', foreground='white')

km_entry = tk.Entry(master=window, background='white')
km_text = ttk.Label(text='kms', font='Arial 20 bold', background='mediumspringgreen', foreground='white')

convert_button = tk.Button(
    master=window,
    text='convert',
    width=10,
    font='Arial 25 bold',
    fg='white',
    bg='mediumspringgreen',
    borderwidth=0,
    activebackground='mediumspringgreen',
    activeforeground='white',
    command=convert)

rest_button = tk.Button(
    master=window,
    text='rest',
    width=10,
    font='Arial 25 bold',
    fg='white',
    bg='mediumspringgreen',
    borderwidth=0,
    activebackground='mediumspringgreen',
    activeforeground='white',
    command=rest)

menu_return_button = tk.Button(master=window,
    text='back to menu',
    width=10,
    font='Arial 25 bold',
    fg='white',
    bg='mediumspringgreen',
    borderwidth=0,
    activebackground='mediumspringgreen',
    activeforeground='white',
    command=menu)
window.mainloop()
