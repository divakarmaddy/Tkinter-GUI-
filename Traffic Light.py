from tkinter import *
from time import sleep

def red():
    canvas1.create_oval(120,120,30,30, fill='red',outline='white',width=4)
    canvas2.create_oval(120, 120, 30, 30, fill='white', outline='white', width=4)
    canvas3.create_oval(120, 120, 30, 30, fill='white', outline='white', width=4)

def orange():
    canvas1.create_oval(120,120,30,30, fill='white',outline='white',width=4)
    canvas2.create_oval(120, 120, 30, 30, fill='orange', outline='white', width=4)
    canvas3.create_oval(120, 120, 30, 30, fill='white', outline='white', width=4)

def green():
    canvas1.create_oval(120,120,30,30, fill='white',outline='white',width=4)
    canvas2.create_oval(120, 120, 30, 30, fill='white', outline='white', width=4)
    canvas3.create_oval(120, 120, 30, 30, fill='green', outline='white', width=4)

count = 25
def start():
    counter(count)

def new(c):
    if c > 15:
        red()
        interval.config(text=c)
        play.update()
        sleep(1)
        counter(c)

    elif c > 10 and c<=15:
        orange()
        interval.config(text=c)
        play.update()
        sleep(1)
        counter(c)

    elif c > 0 and c<=10:
        green()
        interval.config(text=c)
        play.update()
        sleep(1)
        counter(c)

    elif c == 0:
        red()
        interval.config(text=c)
        play.update()
        sleep(1)
        count = 25
        counter(count)

def counter(value):
    if value > 0:
        value = value -1
        new(value)

play = Tk()
play.geometry('300x500')
play.title('Traffic Lights')
play.configure(bg='#32a834')

Button(play, text='Start',font=('calibri',12),bg='gray',fg='white',command=start,width='10',height='3').place(x=20,y=30)
interval = Label(play,font=('calibri',35,'bold'),bg='black',fg='red')
interval.place(x=30,y=300)

canvas1 = Canvas(play,height=140,width=150, bg='black')
canvas1.place(x=140,y=30)

canvas2 = Canvas(play,height=140,width=150, bg='black')
canvas2.place(x=140,y=175)

canvas3 = Canvas(play,height=140,width=150, bg='black')
canvas3.place(x=140,y=320)

play.mainloop()