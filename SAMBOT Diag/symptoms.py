import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter.ttk import Progressbar
import time

root = tk.Tk()


T1 = 'Self'
T3 = 'Assessment'
T4 = 'Machine'
def selfdestruct():
    root.destroy()
    import SAMMODHUB
     # build ui

def toMAINMOD():
    root.destroy()
    import SAMMODHUB

def toTesting_Centers():
    root.destroy()
    import Testing_centers

def toSymptoms():
    root.destroy()
    import symptoms

def tofaq():
    root.destroy()
    import faq

def info():
    symptomlist_18 = tk.Label(frame_3)
    symptomlist_18.config(background='#ffffff', font='{Alte DIN 1451 Mittelschrift} 24 {}', foreground='#1d1a53', justify='center')
    symptomlist_18.config(takefocus=False, text='Dry coughing')
    symptomlist_18.place(anchor='center', relheight='.1', relwidth='.87', relx='.5', rely='.44', x='0', y='0')
    symptomlist_18_24 = tk.Label(frame_3)
    symptomlist_18_24.config(background='#ffffff', font='{Alte DIN 1451 Mittelschrift} 24 {}', foreground='#1d1a53', justify='center')
    symptomlist_18_24.config(takefocus=False, text='Shortness of breath')
    symptomlist_18_24.place(anchor='center', relheight='.1', relwidth='.87', relx='.5', rely='.28', x='0', y='0')
    symptomlist_18_25 = tk.Label(frame_3)
    symptomlist_18_25.config(background='#ffffff', font='{Alte DIN 1451 Mittelschrift} 24 {}', foreground='#1d1a53', justify='center')
    symptomlist_18_25.config(takefocus=False, text='Chills / Fevers')
    symptomlist_18_25.place(anchor='center', relheight='.1', relwidth='0.87', relx='.5', rely='.36', x='0', y='0')
    symptomlist_18_24_26 = tk.Label(frame_3)
    symptomlist_18_24_26.config(background='#ffffff', font='{Alte DIN 1451 Mittelschrift} 24 {}', foreground='#1d1a53', justify='center')
    symptomlist_18_24_26.config(takefocus=False, text='Fatigue')
    symptomlist_18_24_26.place(anchor='center', relheight='.05', relwidth='.27', relx='.5', rely='.76', x='0', y='0')
    symptomlist_18_24_26_27 = tk.Label(frame_3)
    symptomlist_18_24_26_27.config(background='#ffffff', font='{Alte DIN 1451 Mittelschrift} 24 {}', foreground='#1d1a53', justify='center')
    symptomlist_18_24_26_27.config(takefocus=True, text='Muscle / Body aches')
    symptomlist_18_24_26_27.place(anchor='center', relheight='.1', relwidth='.87', relx='.5', rely='.2', x='0', y='0')
    symptomlist_18_24_26_27_28 = tk.Label(frame_3)
    symptomlist_18_24_26_27_28.config(background='#ffffff', font='{Alte DIN 1451 Mittelschrift} 24 {}', foreground='#1d1a53', justify='center')
    symptomlist_18_24_26_27_28.config(takefocus=True, text='Headache')
    symptomlist_18_24_26_27_28.place(anchor='center', relheight='.1', relwidth='.87', relx='.5', rely='.6', x='0', y='0')
    symptomlist_18_24_26_27_28_29 = tk.Label(frame_3)
    symptomlist_18_24_26_27_28_29.config(background='#ffffff', font='{Alte DIN 1451 Mittelschrift} 24 {}', foreground='#1d1a53', justify='center')
    symptomlist_18_24_26_27_28_29.config(takefocus=True, text='Sore throat')
    symptomlist_18_24_26_27_28_29.place(anchor='center', relheight='.1', relwidth='.87', relx='.5', rely='.52', x='0', y='0')
    symptomlist_18_24_26_27_28_29_30 = tk.Label(frame_3)
    symptomlist_18_24_26_27_28_29_30.config(background='#ffffff', cursor='arrow', font='{Alte DIN 1451 Mittelschrift} 24 {}', foreground='#1d1a53')
    symptomlist_18_24_26_27_28_29_30.config(justify='center', takefocus=True, text='Nausea')
    symptomlist_18_24_26_27_28_29_30.place(anchor='center', relheight='.1', relwidth='.27', relx='.5', rely='.68', x='0', y='0')

def destroymod():
    button_2.destroy()

     # build ui
frame_3 = tk.Frame(root)
frame_4 = tk.Frame(frame_3)
frame_4.config(background='#ffffff', height='750', width='500')
frame_4.pack(side='top')
label_1 = tk.Label(frame_3)
label_1.config(background='#ffffff', borderwidth='0', compound='bottom', font='{Alte DIN 1451 Mittelschrift} 36 {}')
label_1.config(foreground='#ff3352', height='0', justify='right', relief='sunken')
label_1.config(state='normal', takefocus=True, text=T1, width='0')
label_1.place(anchor='center', relheight='0.55', relwidth='0.81', relx='0.92', rely='0.74', x='0', y='0')

label_4 = tk.Label(frame_3)
label_4.config(background='#ffffff', font='{Alte DIN 1451 Mittelschrift} 36 {}', foreground='#ff3352', text=T4)
label_4.place(anchor='center', relx='0.82', rely='0.885', x='0', y='0')
frame_8 = tk.Frame(frame_3)
frame_8.config(background='#1d1a53', height='200', width='200')
frame_8.place(anchor='nw', relheight='1.0', relwidth='0.03', x='0', y='0')
button_2 = tk.Button(frame_3)
button_2.config(background='#1d1a53', font='{Alte DIN 1451 Mittelschrift} 24 {}', foreground='#ffffff', relief='flat')
button_2.config(text='LOAD',command=lambda:[destroymod(),info()])
button_2.place(anchor='center', relheight='0.08', relwidth='0.57', relx='.5', rely='0.6', x='0', y='0')
SYMPTOMLIST = tk.Label(frame_3)
SYMPTOMLIST.config(background='#ffffff', font='{Alte DIN 1451 Mittelschrift} 36 {}', foreground='#ff3352', justify='left')
SYMPTOMLIST.config(text='COVID-19 SYMPTOMS')
SYMPTOMLIST.place(anchor='center', relheight='.1', relwidth='.87', relx='.5', rely='.1', x='0', y='0')
label_3 = tk.Label(frame_3)
label_3.config(background='#ffffff', font='{Alte DIN 1451 Mittelschrift} 36 {}', foreground='#ff3352', text=T3)
label_3.place(anchor='center', relx='0.74', rely='0.81', x='0', y='0')
hub = tk.Button(frame_3)
hub.config(text='BACK TO HUB',command=toMAINMOD)
hub.place(anchor='center', relheight='.075', relwidth='1.1', relx='.5', rely='0.97', x='0', y='0')
hub.config(background='#ff3352', foreground='#ffffff',font='{Alte DIN 1451 Mittelschrift} 15 {}')
hub.config(overrelief='flat', relief='flat')
frame_3.config(background='#ffffff', height='600', width='500')
frame_3.pack(side='top')



root.mainloop()