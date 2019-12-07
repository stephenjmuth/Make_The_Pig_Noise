#!/usr/bin/env python3
from playsound import playsound
import tkinter as tk

def make_pig_noise():
    playsound('mp3_466297.mp3')

mpn = tk.Tk(className='mpn')
mpn.title('make the pig noise') 
mpn_button = tk.Button(mpn, text='MPN', width=25, command=make_pig_noise)
quit_button = tk.Button(mpn, text='Quit', width=25, command=mpn.destroy)
mpn_button.pack()
quit_button.pack()
mpn.mainloop()
