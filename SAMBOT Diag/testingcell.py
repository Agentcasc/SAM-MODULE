import tkinter as tk
import tkinter.ttk as ttk


class NewprojectApp:
    def __init__(self, master=None):
        # build ui
        toplevel_3 = tk.Toplevel(master)
        label_1_2 = ttk.Label(toplevel_3)
        label_1_2.config(background='#ffffff', font='{Alte DIN 1451 Mittelschrift} 12 {}', foreground='#ff3352', text='Im sorry to hear that ')
        label_1_2.place(anchor='center', relx='.5', rely='0.65', x='0', y='0')
        toplevel_3.config(height='750', width='500')

        # Main widget
        self.mainwindow = toplevel_3


    def run(self):
        self.mainwindow.mainloop()

if __name__ == '__main__':
    app = NewprojectApp()
    app.run()

