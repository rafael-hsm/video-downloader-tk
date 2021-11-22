from tkinter import *


class Downloader:

    def __init__(self):
        self.window = Tk()
        self.window.title('Youtube Downloader')
        self.window.resizable(0, 0)
        self.window.geometry("680x480+300+150")

        self.img_logo = PhotoImage(file='assets/logo.png')

        self.frame = Frame(self.window, bg="#3b3b3b", pady=30)
        self.frame.pack(fill='x')

        self.label_logo = Label(self.frame, image=self.img_logo, bg='#3b3b3b')
        self.label_logo.pack()

        self.frame2 = Frame(self.window)
        self.frame2.pack()

        self.label_insert = Label(self.frame2, text='  Insert Link:  ', font='arial 12')
        self.label_insert.pack(side='left')

        self.link = Entry(self.frame2)
        self.link.pack(side='left')

        self.play = Button(self.frame2, bg='red', text='>', bd=1, command=None)
        self.play.pack(side='left')

        self.window.mainloop()


Downloader()
