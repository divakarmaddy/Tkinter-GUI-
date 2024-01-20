from tkinter import *
def add():
    num1 = number1.get()
    num2 = number2.get()
    result = num1+num2
    resultlabel.config(text='Result:%d'%result)

def sub():
    num1 = number1.get()
    num2 = number2.get()
    result = num1-num2
    resultlabel.config(text='Result:%d'%result)

def mul():
    num1 = number1.get()
    num2 = number2.get()
    result = num1*num2
    resultlabel.config(text='Result:%d'%result)

def div():
    num1 = number1.get()
    num2 = number2.get()
    result = num1/num2
    resultlabel.config(text='Result:%f'%result)
    
obj = Tk()
obj.geometry('400x400')
obj.title('operations')
obj.configure(bg='aqua')

Label(obj,text='Enter Value A :',font=('calibri',20),bg ='lightblue').grid(row=1,column=1)
Label(obj,text='Enter Value B :',font=('calibri',20),bg ='lightblue').grid(row=2,column=1)

number1 = IntVar()
number2 = IntVar()

Entry(obj,textvariable=number1,font=('calibri',16)).grid(row=1,column=2)
Entry(obj,textvariable=number2,font=('calibri',16)).grid(row=2,column=2)

Button(obj,text = 'ADD',command = add,font=('calibri',15),bg ='blue',fg='white',width='10',height='1').grid(row=4,column=1)
resultlabel=Label(obj,font=('calibri',20),bg='aqua',fg='red')
resultlabel.grid(row=5,column=2)

Button(obj,text = 'SUBTRACT',command = sub,font=('calibri',15),bg ='blue',fg='white',width='10',height='1').grid(row=4,column=2)
resultlabel=Label(obj,font=('calibri',20),bg='aqua',fg='red')
resultlabel.grid(row=5,column=2)

Button(obj,text = 'MULTIPLY',command = mul,font=('calibri',15),bg ='blue',fg='white',width='10',height='1').grid(row=5,column=1)
resultlabel=Label(obj,font=('calibri',20),bg='aqua',fg='red')
resultlabel.grid(row=5,column=2)

Button(obj,text = 'DIVISION',command = div,font=('calibri',15),bg ='blue',fg='white',width='10',height='1').grid(row=5,column=2)
resultlabel=Label(obj,font=('calibri',20),bg='aqua',fg='red')
resultlabel.grid(row=6,column=2)

obj.mainloop()
