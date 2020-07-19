import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter.ttk import Progressbar
import time

root = tk.Tk()

B1 = 'SAM MODULE'
B2 = 'COVID-19 TESTING SITES'
B3 = 'COVID-19 SYMPTOMS'
B4 = 'FAQ'
T1 = 'Self'
T3 = 'Assessment'
T4 = 'Machine'



def hover(counter=1):
        label_1.config(text=T1[:counter])
        label_3.config(text=T3[:counter])
        label_4.config(text=T4[:counter])
        root.after(150, lambda: hover(counter+1))

def b1event(counter=1):
        button_8.config(text=B1[:counter])
        button_9.config(text=B3[:counter])
        root.after(150, lambda: b1event(counter-1))

def toMAINMOD():
    root.destroy()
    import MainModule
    

def toSymptoms():
    root.destroy()
    import symptoms

 # build ui
print('startsamhubmain')
frame_3 = tk.Frame(root)
frame_4 = tk.Frame(frame_3)
frame_4.config(background='#ffffff', height='750', width='500')
frame_4.pack(side='top')
label_1 = tk.Label(frame_3)
label_1.config(background='#ffffff', borderwidth='0', compound='bottom', font='{Alte DIN 1451 Mittelschrift} 36 {}')
label_1.config(foreground='#ff3352', height='0', justify='right', relief='sunken')
label_1.config(state='normal', takefocus=True, text=T1, width='0')
label_1.place(anchor='center', relheight='0.55', relwidth='0.81', relx='0.92', rely='0.79', x='0', y='0')
button_8 = tk.Button(frame_3)
button_8.config(activebackground='#ffffff', activeforeground='#000000', background='#3a3597', disabledforeground='#ffffff')
button_8.config(font='{Alte DIN 1451 Mittelschrift} 20 {}', foreground='#ffffff', highlightbackground='#ffffff', highlightcolor='#ffffff')
button_8.config(justify='center', relief='flat', text=B1,command=lambda: [hover(),b1event(), toMAINMOD()])
button_8.place(anchor='center', relheight='.1', relwidth='.5', relx='.5', rely='.55', x='0', y='0')
button_9 = tk.Button(frame_3)
button_9.config(activebackground='#ffffff', activeforeground='#000000', background='#3a3597', font='{Alte DIN 1451 Mittelschrift} 20 {}')
button_9.config(foreground='#ffffff', highlightbackground='#ffffff', highlightcolor='#ffffff', relief='flat')
button_9.config(text=B3,command=lambda: [hover(),b1event(), toSymptoms()])
button_9.place(anchor='center', relheight='.1', relwidth='.5', relx='.5', rely='.75', x='0', y='0')
label_3 = tk.Label(frame_3)
label_3.config(background='#ffffff', font='{Alte DIN 1451 Mittelschrift} 36 {}', foreground='#ff3352', text=T3)
label_3.place(anchor='center', relx='0.74', rely='0.86', x='0', y='0')
label_4 = tk.Label(frame_3)
label_4.config(background='#ffffff', font='{Alte DIN 1451 Mittelschrift} 36 {}', foreground='#ff3352', text=T4)
label_4.place(anchor='center', relx='0.82', rely='0.935', x='0', y='0')
SAMLAB = tk.Label(frame_3)
SAMLAB.config(background='#ffffff', cursor='arrow', font='{Alte DIN 1451 Mittelschrift} 100 {}', foreground='#ff3352')
SAMLAB.config(text='SAM')
SAMLAB.place(anchor='center', relheight='0.36', relwidth='0.77', relx='.5', rely='.2', x='0', y='0')
ALPHA = ttk.Label(frame_3)
ALPHA.config(background='#ffffff', font='{Alte DIN 1451 Mittelschrift} 12 {}', foreground='#ff3352', text='ALPHA V1.0')
ALPHA.place(anchor='center', relx='.85', rely='.02', x='0', y='0')
frame_3.config(background='#ffffff', height='600', width='500')
frame_3.pack(side='top')
root.mainloop()

