from tkinter import *
import customtkinter
import webbrowser
from PIL import ImageTk, Image


class LoginGui:
    def __init__(self, func):
        self.app = customtkinter.CTk()
        self.app.geometry("300x500")
        self.app.title("Voice Assist Login Page")
        resized = Image.open("logo.jpeg").resize((100, 100), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(resized)
        imgframe = Frame(master=self.app, width=100, height=100)
        imgframe.pack(pady=5, padx=2)
        imglabel = Label(imgframe, image=img)
        imglabel.pack()
        # imglabel.place(anchor='center', relx=0.5, rely=0.5)
        self.appLabel = customtkinter.CTkLabel(
            master=self.app, text="Please Login to continue")
        self.appLabel.pack(pady=5)
        self.alertLabel = customtkinter.CTkLabel(
            master=self.app, text="Invalid email or password !", text_color="red")

        # self.alertLabel.pack(pady=5)
        root = customtkinter.CTkFrame(master=self.app)
        root.pack(padx=20, pady=10, fill='both', expand=True)
        button = customtkinter.CTkButton(
            master=root, text='Login!', command=func)
        emailLabel = customtkinter.CTkLabel(master=root, text='Email')
        self.emailInput = customtkinter.CTkEntry(
            master=root, placeholder_text="Email")
        self.passInput = customtkinter.CTkEntry(
            master=root, placeholder_text="Password", show='*')
        passLabel = customtkinter.CTkLabel(master=root, text='Password')
        # root.grid_rowconfigure(0, weight=1)
        regButton = customtkinter.CTkButton(
            master=root, text='Register!', command=self.openweb)
        root.grid_columnconfigure(0, weight=1)
        emailLabel.grid(row=0, pady=(40, 0),)
        self.emailInput.grid(row=1, pady=(5, 0),)
        passLabel.grid(row=2, pady=(20, 0),)
        self.passInput.grid(row=3, pady=(5, 0),)
        button.grid(row=4, pady=(20, 0),)
        regButton.grid(row=5, pady=(10, 0))
        self.app.mainloop()

    def update(self):
        self.alertLabel.pack(side='top', pady=2, after=self.appLabel)
        self.app.update()

    def openweb(self):
        webbrowser.open('https://voice-assist.onrender.com/', new=1)
