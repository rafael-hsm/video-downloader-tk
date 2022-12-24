from pytube import YouTube
from tkinter import *
from tkinter import Tk, font



def download():
    hide()
    a = (str(linkbruh.get()))
    try:
        vid = YouTube(a)
        down = vid.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
              
        title.config(text=f'title: {vid.title}')
        title.place(x=220, y=230)   

        
        down.download(r'\downloads')   # give your path here              

        error.config(text='Successfully downloaded')
        error.place(x=220, y=210)

        
    except:
        error.config(text='error: Unable to download the video')
        error.place(x=220, y=210)
        return 

def hide():
    title.place_forget()
    error.place_forget()

root = Tk()
root.geometry('700x250')
root.title('YouTube Downloader')

link_here = Label(root, text="Paste Here", font=("courier",40,))
link_here.place(x=220,y=40)

title = Label(root, text='')
title.place(x=220, y=230)

error = Label(root, text='')
error.place(x=220, y=210)

linkbruh = StringVar()
pasted = Entry(root,width=60,textvariable=linkbruh)
pasted.place(x=80,y=120)

Button(root,text="Download Video", width=20, bg="black", fg="gray", command=download).place(x=250,y=170)

root.mainloop()