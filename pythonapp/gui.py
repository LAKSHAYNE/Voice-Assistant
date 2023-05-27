from tkinter import *
import tkinter as tk
# from Voice_Assistant_Mini_Project import *
import customtkinter


class Gui:
    def __init__(self, func):
        self.window = customtkinter.CTk()
        self.window.geometry('450x200')
        self.window.title('ASSISTANT')
        self.window.grid_columnconfigure(0, weight=1)
        self.window.title("Voice Assist 😀")
        # f1 = customtkinter.CTkFrame(
        #     master=self.window, height=300, width=250)
        # f1.grid(row=0, padx=10, pady=20)
        # can_wid=Canvas(f1,height=300,width=270,bg='black')
        # can_wid.grid(row=1,column=0)
        self.l1 = customtkinter.CTkTextbox(
            master=self.window, height=110, width=250, wrap=WORD)
        self.l1.grid(row=0, padx=10, pady=20)
        self.l1.insert(index=0.0,
                       text='GREETINGS!\nWelcome to Voice Assist\nThis Application was created by Lakshay ,Harsh, Mani and Ginni. \nPlease press Listen button to use the application')
        b1 = customtkinter.CTkButton(self.window, height=3, text="Listen",
                                     command=func)
        b1.grid(row=1, padx=2, pady=4)
        self.window.mainloop()

    def checking(self):
        print('🎈🎈🎈🎈🎈🎈🎈')

    def assistant_text(self, stri):
        self.l1.delete("0.0", "end")
        self.l1.insert(index=0.0, text=stri)
        self.window.update()
