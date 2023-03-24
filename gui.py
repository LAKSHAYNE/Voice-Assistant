from tkinter import *
import tkinter as tk
# from Voice_Assistant_Mini_Project import *


class Gui:
    def __init__(self, func):
        print('sadkjashdkjahsdkjah')
        self.window = Tk()
        self.window.geometry('450x200')
        self.window.title('ASSISTANT')
        f1 = Frame(self.window, height=300, width=250,
                   borderwidth=5, relief=SUNKEN, bg='black')
        f1.pack(side=TOP)
        # can_wid=Canvas(f1,height=300,width=270,bg='black')
        # can_wid.grid(row=1,column=0)
        self.l1 = Label(f1, height=3, text='hey there i am your assistant press listen to perform action',
                        font='16', fg='white', bg='black')
        self.l1.pack(side=TOP)
        f2 = Frame(self.window, height=400, width=200,
                   borderwidth=5, relief=SUNKEN, bg='black')
        f2.pack(side=BOTTOM, fill=X)
        b1 = Button(f2, height=3, text="Listen",
                    bg='grey', command=func)
        b1.pack(side=BOTTOM, fill=X)
        self.window.mainloop()

    def checking(self):
        print('🎈🎈🎈🎈🎈🎈🎈')

    def assistant_text(self, stri):
        self.l1.configure(text=stri)
        self.window.update()
