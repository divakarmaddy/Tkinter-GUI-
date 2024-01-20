from tkinter import *
from tkinter import ttk

def getvalues(selected):
    dropmenu2.set_menu(*option2.get(selected))

def getvalues1(selected):
    dropmenu3.set_menu(*option3.get(selected))

def getvalues2(selected):
    dropmenu4.set_menu(*option4.get(selected))

obj = Tk()
obj.geometry('600x600')
obj.title('operations')
obj.configure(bg='aqua')

Label(obj,text='Select Bus Name :',font=('calibri',20,'bold'),bg ='lightblue').place(x=30,y=50)
Label(obj,text='Select Starting Point :',font=('calibri',20,'bold'),bg ='lightblue').place(x=30,y=120)
Label(obj,text='Select Ending Point :',font=('calibri',20,'bold'),bg ='lightblue').place(x=30,y=190)
Label(obj,text='Select Price :',font=('calibri',20,'bold'),bg ='lightblue').place(x=30,y=260)

option1 = ['SETC','YBM','SRS','RedBus']
dropvar1 = StringVar()
dropmenu1 = ttk.OptionMenu(obj, dropvar1,'------Select-------',*option1,command=getvalues)
dropmenu1.place(x=300,y=50)

option2 = {
    'SETC':['Chennai','Bangalore','Mysore','Kerala'],
    'YBM':['Chennai','Bangalore','Mysore','Kerala'],
    'SRS':['Chennai','Bangalore','Mysore','Kerala'],
    'RedBus':['Chennai','Bangalore','Mysore','Kerala']
}
dropvar2 = StringVar()
dropmenu2 = ttk.OptionMenu(obj, dropvar2,'------Select-------',*option2,command=getvalues1)
dropmenu2.place(x=300,y=120)

option3 = {
    'Chennai':['Bangalore','Mysore','Kerala'],
    'Bangalore':['Chennai','Mysore','Kerala'],
    'Mysore':['Chennai','Bangalore','Kerala'],
    'Kerala':['Chennai','Bangalore','Mysore']
}
dropvar3 = StringVar()
dropmenu3 = ttk.OptionMenu(obj, dropvar3,'------Select-------',*option3,command=getvalues2)
dropmenu3.place(x=300,y=190)

option4 = {
    'Chennai':['Premium - 2000','Standard - 1200','Basic - 850'],
    'Bangalore':['Premium - 2000','Standard - 1200','Basic - 850'],
    'Mysore':['Premium - 2000','Standard - 1200','Basic - 850'],
    'Kerala':['Premium - 2000','Standard - 1200','Basic - 850']
}
dropvar4 = StringVar()
dropmenu4 = ttk.OptionMenu(obj, dropvar4,'------Select-------')
dropmenu4.place(x=300,y=260)

obj.mainloop()