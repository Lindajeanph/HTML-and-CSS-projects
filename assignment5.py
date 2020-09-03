import shutil
import os
import time
import sys
import datetime
import glob
from datetime import timedelta
destination = 'C:/Users/bposs/Documents/MonitoredFiles/'
source = 'C:/Users/bposs/Documents/DailyFiles/'

    #a list of files
a = os.listdir(source)

for i in a:
    b = os.path.join(source, i)
    c = datetime.datetime.now() - timedelta(hours=24)
    d = os.path.getmtime(b)
    e = datetime.datetime.fromtimestamp(d)
    if e >= c:
        shutil.move(b, destination)
        print(i)

from tkinter import *
win = Tk()
b1 = Button(win, text="Check files")
b2 = Button(win, text="Copy Files")
b3 = Button(win, text="Initiate")
b1.pack()
b2.pack()
b3.pack()
b1.pack(side=LEFT, padx = 20)
b2.pack(side=LEFT, padx = 20)
b3.pack(side=LEFT, padx = 20)

       #check files
def but1():
    print(a)
b1.configure(command=but1)
    #Copy files
def but2():
    print(destination)
b2.configure(command=but2)

    #Initiate
def but3():
    print(i)
b3.configure(command=but3)

    




