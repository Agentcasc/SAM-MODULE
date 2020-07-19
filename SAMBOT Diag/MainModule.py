import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter.ttk import Progressbar
import time

root = tk.Tk()


COVID_SYMP = ['FEVER','CHILLS','COUGH','SHORTNESS OF BREATH','BREATHING DIFFICULTY'
,'FATIGUE','MUSCLE' ,'BODY ACHES','HEADACHE','SORE THROAT','LOSS OF TASTE','LOSS OF SMELL','CONGESTION','NAUSEA' ,'VOMITING',]

questionlist = ['a','Hello,have you been well?','have you had any chills lately?','have you had a fever in the past week?','Have you been dry coughing this week?','Have you been experiencing shortness of breath?',
'Have you been experiencing fatigue?','Have you had muscle or body aches this week?','Do you have headaches often?','Have you had a sore throat?','Are you experiencing nausea?' 
]


#print(','.join(COVID_SYMP))
YES = 'Yes'
ALIL = 'A little bit.'
NO = 'No'

Sorry = StringVar()
ls = 1
MAINTEXT = StringVar()
MAINTEXT.set(questionlist[ls])
LASTTEXT = 'My algorithm shows you might have COVID-19 :/'
LASTTEXTOC2 = 'My Algorithm does not flag you as a possible COVID-19 patient'
NEWLABELEND = 'Please choose how you would like to proceed'
SCNYES = 'Check Symptoms'
SCNYES2 = 'Find Testing sites'
SCNO1 = 'Return to HUB'
SCNO2 = 'Exit '

ovscore = 0
i = 0
CC = 0
newtexts = ['COVID-19 TESTING SITES','FAQ','SYMPTOMS']


def everyclick():
    global ls
    ls = ls + 1

def go(counter=1):
    label_2.config(text=LABEL2TEXT[:counter])
    label_1.config(text=SAM[:counter])
    button_5.config(text=CONTINUE[:counter])
    button_5.config(foreground='#ffffff')
    root.after(150, lambda: go(counter+1))

def toHUB():
    root.destroy()
    import SAMMODHUB
def toSYMPTOMS():
    root.destroy()
    import symptoms
def toT_C():
    root.destroy()
    import Testing_centers

def NEWBOXMODULESCno():
    if ls == 11 and ovscore < 50:
        ###SECOND BUTTON
        button_newbig1 = tk.Button(frame_3)
        button_newbig1.config(anchor='n', background='#eeeeee', foreground='#000000',font='{Alte DIN 1451 Mittelschrift} 24 {}', justify='center')
        button_newbig1.config(relief='flat', text=SCNO1,command=toHUB)
        button_newbig1.place(anchor='center', bordermode='inside', relheight='.07', relwidth='0.76', relx='.5', rely='0.8', x='0', y='0')
        ###SECOND BUTTON
        button_newbig2 = tk.Button(frame_3)
        button_newbig2.config(anchor='n', background='#eeeeee', foreground='#000000',font='{Alte DIN 1451 Mittelschrift} 24 {}', justify='center')
        button_newbig2.config(relief='flat', text=SCNO2,command = lambda: root.destroy())
        button_newbig2.place(anchor='center', bordermode='inside', relheight='.07', relwidth='0.76', relx='.5', rely='0.9', x='0', y='0')

def NEWBOXMODULESCyes():
    if ls == 11 and ovscore >= 55:
    ###SECOND BUTTON
        button_newbig1 = tk.Button(frame_3)
        button_newbig1.config(anchor='n', background='#eeeeee', foreground='#000000',font='{Alte DIN 1451 Mittelschrift} 24 {}', justify='center')
        button_newbig1.config(relief='flat', text=SCNYES,command=toSYMPTOMS)
        button_newbig1.place(anchor='center', bordermode='inside', relheight='.07', relwidth='0.76', relx='.5', rely='0.8', x='0', y='0')
        ###SECOND BUTTON
        button_newbig2 = tk.Button(frame_3)
        button_newbig2.config(anchor='n', background='#eeeeee', foreground='#000000',font='{Alte DIN 1451 Mittelschrift} 24 {}', justify='center')
        button_newbig2.config(relief='flat', text=SCNO2,command=lambda: root.destroy())
        button_newbig2.place(anchor='center', bordermode='inside', relheight='.07', relwidth='0.76', relx='.5', rely='0.9', x='0', y='0')


def newbox(counter=1):
    if ls == 11 and ovscore >= 55:
        message_1.destroy()
        message_v2 = tk.Message(frame_3)
        message_v2.config(background='#ffffff', font='{Alte DIN 1451 Mittelschrift} 39 {}', foreground='#ff3352', relief='flat')
        message_v2.config(takefocus=False, text=LASTTEXT)
        message_v2.place(anchor='center', height='10', relheight='0.5', relwidth='.9', relx='0.5', rely='0.33', width='10', x='0', y='0')
        message_v2.config(text=LASTTEXT[:counter])
        label_1.destroy()
        label_v1 = ttk.Label(frame_3)
        label_v1.config(background='#ffffff', font='{Alte DIN 1451 Mittelschrift} 12 {}', foreground='#ff3352', text=NEWLABELEND)
        label_v1.place(anchor='center', relx='.5', rely='0.65', x='0', y='0')
        label_v1.config(text=NEWLABELEND[:counter])
        button_11.destroy()
        button_12.destroy()
        button_13.destroy()
        root.after(50, lambda: newbox(counter+1))
    elif ls == 11 and ovscore < 50:
        message_1.destroy()
        message_v2 = tk.Message(frame_3)
        message_v2.config(background='#ffffff', font='{Alte DIN 1451 Mittelschrift} 39 {}', foreground='#ff3352', relief='flat')
        message_v2.config(takefocus=False, text=LASTTEXTOC2)
        message_v2.place(anchor='center', height='10', relheight='0.5', relwidth='.9', relx='0.5', rely='0.33', width='10', x='0', y='0')
        message_v2.config(text=LASTTEXTOC2[:counter])
        label_1.destroy()
        label_v1 = ttk.Label(frame_3)
        label_v1.config(background='#ffffff', font='{Alte DIN 1451 Mittelschrift} 12 {}', foreground='#ff3352', text=NEWLABELEND)
        label_v1.place(anchor='center', relx='.5', rely='0.65', x='0', y='0')
        label_v1.config(text=NEWLABELEND[:counter])
        button_11.destroy()
        button_12.destroy()
        button_13.destroy()
        root.after(50, lambda: newbox(counter+1))
        pass
    pass

def changetext(counter=1):  #MAINMODULE
    if ls == 11 and ovscore >= 55:
        MAINTEXT.set('My algorithm shows you might have COVID-19, please choose how you would like to proceed')
        button_12.config(text=ALIL[:counter])
        button_11.config(text=YES[:counter])
        button_13.config(text=NO[:counter])
        root.after(150, lambda: changetext(counter-1))
        YES.replace(YES, newtexts[1])
        ALIL.replace(ALIL,newtexts[0])
        NO.replace(NO,newtexts[0])

    elif ls == 11 and ovscore < 50:
        button_12.config(text=ALIL[:counter])
        button_11.config(text=YES[:counter])
        button_13.config(text=NO[:counter])
        root.after(150, lambda: changetext(counter-1))
        YES.replace(YES, newtexts[1])
        ALIL.replace(ALIL,newtexts[0])
        NO.replace(NO,newtexts[0])

    elif ls == 2 and ovscore == 0:
        Sorry.set('I am sorry about that :(')
        MAINTEXT.set(questionlist[ls])
        button_12.config(background='#eeeeee',foreground='#000000')
    elif ls > 2:
        Sorry.set('')
        MAINTEXT.set(questionlist[ls])
    elif ls == 2 and ovscore == 10:
        Sorry.set('Great to hear!')
        button_12.config(background='#eeeeee',foreground='#000000')
        MAINTEXT.set(questionlist[ls])
    else:
        MAINTEXT.set(questionlist[ls])
        print(ls)

def counterpos():
    if ls >= 2:
        global ovscore
        ovscore = ovscore + 10
        print(ovscore)
    

def OVCOUNT2():
    global ovscore
    ovscore = ovscore + 5
    print(ovscore)


##NOTE TO JJ COMING AWAKE, USE TEXT/MESSAGE ELEMENT INSTEAD OF LABEL
frame_3 = tk.Frame(root)
frame_4 = tk.Frame(frame_3)
frame_4.config(background='#ffffff', height='750', width='500')
frame_4.pack(side='top')
label_1 = ttk.Label(frame_3)
label_1.config(background='#ffffff', font='{Alte DIN 1451 Mittelschrift} 12 {}', foreground='#ff3352', textvariable=Sorry)
label_1.place(anchor='center', relx='.5', rely='0.65', x='0', y='0')
message_1 = tk.Message(frame_3)
message_1.config(background='#ffffff', font='{Alte DIN 1451 Mittelschrift} 39 {}', foreground='#ff3352', relief='flat')
message_1.config(takefocus=False, textvariable=MAINTEXT)
message_1.place(anchor='center', height='10', relheight='0.5', relwidth='.9', relx='0.5', rely='0.33', width='10', x='0', y='0')
button_11 = tk.Button(frame_3)
button_11.config(anchor='center', background='#eeeeee', font='{Alte DIN 1451 Mittelschrift} 20 {}', justify='center')
button_11.config(relief='flat', text=YES,command=lambda:[everyclick(),counterpos(),changetext(),newbox(),NEWBOXMODULESCno(),NEWBOXMODULESCyes()])
button_11.place(anchor='center', bordermode='inside', relheight='.07', relwidth='.35', relx='0.30', rely='0.8', x='0', y='0')
button_12 = tk.Button(frame_3)
button_12.config(anchor='n', background='#ffffff', foreground='#ffffff',font='{Alte DIN 1451 Mittelschrift} 24 {}', justify='center')
button_12.config(relief='flat', text=ALIL,command=lambda:[everyclick(),OVCOUNT2(),changetext()])
button_12.place(anchor='center', bordermode='inside', relheight='.07', relwidth='0.76', relx='.5', rely='0.9', x='0', y='0')
button_13 = tk.Button(frame_3)
button_13.config(anchor='center', background='#eeeeee', font='{Alte DIN 1451 Mittelschrift} 20 {}', justify='center')
button_13.config(relief='flat', text=NO,command=lambda:[everyclick(),changetext(),newbox(),NEWBOXMODULESCno(),NEWBOXMODULESCyes()])
button_13.place(anchor='center', bordermode='inside', relheight='.07', relwidth='.35', relx='0.70', rely='.8', x='0', y='0')
ALPHA = ttk.Label(frame_3)
ALPHA.config(background='#ffffff', font='{Alte DIN 1451 Mittelschrift} 12 {}', foreground='#ff3352', text='ALPHA V1.0')
ALPHA.place(anchor='center', relx='.85', rely='.02', x='0', y='0')
frame_8 = tk.Frame(frame_3)
frame_8.config(background='#ff3352', height='200', width='200')
frame_8.place(anchor='nw', relheight='1.0', relwidth='0.03', x='0', y='0')
frame_3.config(background='#ffffff', height='600', width='500')
frame_3.pack(side='top')

root.mainloop()