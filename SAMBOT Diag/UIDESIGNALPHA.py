import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter.ttk import Progressbar
import time

root = tk.Tk()

CONTINUE = 'CONTINUE'
SAM = 'SAM'
LABEL2TEXT = 'Welcome to...'
ENTER = 'ENTER'



def go(counter=1):
    label_2.config(text=LABEL2TEXT[:counter])
    label_1.config(text=SAM[:counter])
    button_5.config(text=CONTINUE[:counter])
    button_5.config(foreground='#ffffff')
    root.after(150, lambda: go(counter+1))

def bad(counter=1):
    button_4.config(text=ENTER[:counter])
    root.after(150, lambda: bad(counter-1))
    button_4.config(background='#1d1a53')



    

    
progress=Progressbar(root,orient=HORIZONTAL,length=500,mode='determinate')
def bar():
    progress['value']=0
    root.update_idletasks()
    progress['value']=10
    root.update_idletasks()
    time.sleep(.1)
    progress['value']=20
    root.update_idletasks()
    time.sleep(.1)
    progress['value']=30
    root.update_idletasks()
    time.sleep(.1)
    progress['value']=40
    root.update_idletasks()
    time.sleep(.1)
    progress['value']=50
    root.update_idletasks()
    time.sleep(.1)
    progress['value']=60
    root.update_idletasks()
    time.sleep(.1)
    progress['value']=70
    root.update_idletasks()
    time.sleep(.3)
    progress['value']=80
    root.update_idletasks()
    time.sleep(.4)
    progress['value']=90
    root.update_idletasks()
    time.sleep(.7)
    progress['value']=10
    root.update_idletasks()
    time.sleep(1)
    progress['value']=100
    root.update_idletasks()
progress.pack()


def selfdestruct():
    root.destroy()
    import SAMMODHUB
    


def createNewWindow():
    newWindow = tk.Toplevel(root)


frame_3 = tk.Frame(root)
frame_4 = tk.Frame(frame_3)
frame_4.config(background='#1d1a53', height='650', width='500')
frame_4.pack(side='top')
label_1 = tk.Label(frame_3)
label_1.config(background='#1d1a53', borderwidth='0', compound='bottom', font='{Alte DIN 1451 Mittelschrift} 72 {}')
label_1.config(foreground='#ff3352', height='0', justify='right', relief='sunken')
label_1.place(anchor='center', relheight='0.37', relwidth='0.81', relx='0.5', rely='0.47', x='0', y='0')
label_2 = tk.Label(frame_3)
label_2.config(activebackground='#000000', background='#1d1a53', disabledforeground='#000000', font='{Alte DIN 1451 Mittelschrift} 48 {bold}')
label_2.config(foreground='#ffffff', justify='left', relief='flat', takefocus=False)
label_2.place(anchor='nw', relx='0.051', rely='0.88', x='0', y='0')
button_4 = tk.Button(frame_3)
button_4.config(activebackground='#1d1a53', anchor='n', background='#332e92', borderwidth='0')
button_4.config(cursor='arrow', font='{Bahnschrift Light SemiCondensed} 36 {}', foreground='#ffffff', highlightbackground='#1d1a53')
button_4.config(highlightcolor='#ffffff', highlightthickness='0', relief='flat', takefocus=True)
button_4.config(text=ENTER,command=lambda:[go(), bad(),bar(),CONTINUE()])
button_4.place(anchor='center', relheight='0.1', relwidth='0.55', relx='.5', rely='0.65', x='0', y='0')
frame_3.config(background='#1d1a53', height='750', width='500')
frame_3.pack(side='top')
button_5 = tk.Button(frame_3)
button_5.config(activebackground='#1d1a53', anchor='n', background='#1d1a53', font='{Bahnschrift Light SemiCondensed} 36 {}')
button_5.config(foreground='#1d1a53', highlightbackground='#1d1a53', highlightcolor='#ffffff', highlightthickness='0')
button_5.config(justify='left', relief='flat', takefocus=True, text=CONTINUE,command=selfdestruct)
button_5.place(anchor='center', relheight='0.11', relwidth='0.6', relx='.5', rely='0.76', x='0', y='0')
ALPHA = ttk.Label(frame_3)
ALPHA.config(background='#1d1a53', font='{Alte DIN 1451 Mittelschrift} 12 {}', foreground='#ff3352', text='ALPHA V1.0')
ALPHA.place(anchor='center', relx='.85', rely='.02', x='0', y='0')
frame_8 = tk.Frame(frame_3)
frame_8.config(background='#ff3352', height='200', width='200')
frame_8.place(anchor='nw', relheight='1.0', relwidth='0.03', x='0', y='0')

root.mainloop()

