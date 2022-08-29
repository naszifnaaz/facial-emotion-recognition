import os
from PIL import ImageTk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from PIL import Image
import vlc
import live_emotion
import time

def main():
    cwd = os.getcwd()
    root = Tk()
    root.config(bg="green")
    #root = Toplevel()
    frame = Frame(root)
    frame.pack()

    label1 = Label(root, text='FACIAL EMOTION RECOGNITION',font=("Arial Bold", 14))
    label1.config(fg="red")
    label1.pack()

    label1 = Label(root, text='', font=("Arial Bold", 14))
    label1.config(fg="red", bg="green")
    label1.pack()

    image = Image.open(cwd+"/bg2.jpg")
    photo = ImageTk.PhotoImage(image)
    label = Label(root, image=photo)
    root.image = photo  # keeping a reference!
    label.pack()

    label1 = Label(root, text='', font=("Arial Bold", 14))
    label1.config(fg="cyan", bg="green")
    label1.pack()

    def callback():
        res = live_emotion.main()
        print(res)
        image = Image.open(cwd+"/output.jpg")
        photo = ImageTk.PhotoImage(image)
        label = Label(root, image=photo)
        root.image = photo  # keep a reference!
        label.pack()
        label1 = Label(root, text=res, font=("Arial Bold", 14))
        label1.config(fg="green")
        label1.pack()

    def callback2():
        root.destroy()
        main()

    root.title('EMOLAYER')
    root.geometry('400x600')  # Size 200, 200
    root.resizable(width=True, height=True)

    Button(text='Start', command=callback).pack(side=TOP, padx=10)
    label1 = Label(root, text='', font=("Arial Bold", 14))
    label1.config(fg="cyan", bg="green")
    label1.pack()
    Button(text='Refresh', command=callback2).pack(side=TOP, padx=10)
    root.mainloop()  
main()
