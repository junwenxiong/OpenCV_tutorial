from tkinter import *
import os
from datetime import datetime

root = Tk()

root.configure(background="black")

def function1():
    os.system('py Feature_Detection_and_Description\Haar_Feature_Detection\Car_Detection\Car_Detection1.py')


def exit():
    root.destroy()


root.title('Detections')

Button(root, text="Car Detection", font=("times new roman",20),bg="#000000",fg="green",command=function1).grid(row=4,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

root.mainloop()