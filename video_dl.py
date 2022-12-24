import os
from tkinter import *
from tkinter import filedialog, IntVar

from pytube import YouTube
from pytube.cli import on_progress


class Downloader:

    def __init__(self):
        self.window = Tk()
        self.window.title('Youtube Downloader')
        self.window.resizable(0, 0)
        self.window.geometry("680x480+300+150")
        


        self.img_logo = PhotoImage(file='assets/logo.png')

        self.audio = True
        self.video = False

        self.frame = Frame(self.window, bg="#3b3b3b", pady=30)
        self.frame.pack(fill='x')

        self.label_logo = Label(self.frame, image=self.img_logo, bg='#3b3b3b')
        self.label_logo.pack()

        self.frame2 = Frame(self.window, pady=20)
        self.frame2.pack()

        self.label_insert = Label(self.frame2, text='  Insert Link:  ', font='arial 12')
        self.label_insert.pack(side='left')

        self.link = Entry(self.frame2, font='arial 20', width=30)
        self.link.pack(side='left')

        self.play = Button(self.frame2, bg='brown1', fg='white', text='>', bd=1,
                           width=4, height=2, command=lambda: self.download(self.link.get())).pack(side='left')

        self.frame3 = Frame(self.window)
        self.frame3.pack()

        # Setting Radio Button select default
        button_default = IntVar()
        
        # General setting radio button
        self.radio1 = Radiobutton(self.frame3, text='Áudio', value=0, variable=button_default,
                                  command=self.validate_audio).pack(side='left')
        self.radio2 = Radiobutton(self.frame3, text='Vídeo', value=1, variable=button_default,
                                  command=self.validate_video).pack(side='left')
        self.radio3 = Radiobutton(self.frame3, text='Áudio e Vídeo', value=2, variable=button_default,
                                  command=self.validate_all).pack(side='left')

        # Message download finished
        
        self.frame4 = Frame(self.window)
        self.frame4.pack()
        
        self.message = Label(self.frame4, text='Not started!', font="arial 12")
        self.message.pack(side="left")
        
        self.window.mainloop()

    def validate_audio(self):
        self.audio = True
        self.video = False

    def validate_video(self):
        self.audio = False
        self.video = True

    def validate_all(self):
        self.audio = False
        self.video = False

    def format_change(self, pasta, link):
        yt = YouTube(link)
        old_file = pasta + os.sep + yt.title
        print(f"Old_file {old_file}")
        new_file = old_file[:-3] + ".mp3"
        print(f"New_file {new_file}")
        print(old_file, new_file)
        os.rename(old_file, new_file)
    
    def download(self, link):
        if self.audio:
            pasta = filedialog.askdirectory()
            YouTube(link).streams.filter(only_audio=True).get_audio_only().download(pasta)
            self.format_change(pasta=pasta, link=link)
            self.message.config(text='Successfully downloaded')
            self.message.pack(side="right")
            
                        
        elif self.video:
            pasta = filedialog.askdirectory()
            YouTube(link).streams.filter(only_video=True).first().download(pasta)
            self.message.config(text='Successfully downloaded')
            self.message.pack(side="right")

        else:
            pasta = filedialog.askdirectory()
            YouTube(link).streams.get_highest_resolution().download(pasta)
            self.message.config(text='Successfully downloaded')
            self.message.pack(side="right")

Downloader()
