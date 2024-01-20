import tkinter.messagebox
from tkinter import*
import mysql.connector

db = mysql.connector.connect(host='localhost', user='root', password='', db='access')
cursor = db.cursor()

def calculate():
    product_tot.set(product_price.get() * product_qty.get())

def add():
    id = product_id.get()
    name = product_name.get()
    price = product_price.get()
    qty = product_qty.get()
    tot = product_tot.get()

    cursor.execute('insert into details values(%s,%s,%s,%s,%s)', [id, name, price, qty, tot])
    db.commit()
    tkinter.messagebox.showinfo('Access', 'Product added')

def view():
        id = product_id.get()
        cursor.execute('select * from details where ProId=%s', [id])
        data = cursor.fetchone()
        if data != None:
            product_name.set(data[1])
            product_price.set(data[2])
            product_qty.set(data[3])
            product_tot.set(data[4])

        else:
            tkinter.messagebox.showinfo('Access', 'No Data')

 
def update():
    id = product_id.get()
    name = product_name.get()
    price = product_price.get()
    qty = product_qty.get()
    tot = product_tot.get()
    cursor.execute('Update details set ProName=%s, ProPrice=%s, ProQty=%s, Protot=%s where ProId=%s', [name, price, qty, tot, id])
    db.commit()
    tkinter.messagebox.showinfo('Access', 'Product updated')


def delete():
    id = product_id.get()
    cursor.execute('delete from details where ProId=%s', [id])
    db.commit()
    tkinter.messagebox.showinfo('Access', 'Product deleted')

def clear():
    product_id.set('')
    product_name.set('')
    product_price.set('')
    product_qty.set('')
    product_tot.set('')

def overall():
    global viewpage
    viewpage = Toplevel(obj)
    viewpage.geometry('1000x500')
    viewpage.title('Product lits')
    viewpage.configure(bg='lightblue')
    cursor.execute('select * from details')
    data = cursor.fetchall()
    rows = len(data)
    cols = len(data[0])
    Label(viewpage, text ='ProId', font=('calibri',20,'bold'),bg='lightgreen').grid(row=0,column=0)
    Label(viewpage, text='ProName', font=('calibri', 20, 'bold'), bg='lightgreen').grid(row=0, column=1)
    Label(viewpage, text='ProPrice', font=('calibri', 20, 'bold'), bg='lightgreen').grid(row=0, column=2)
    Label(viewpage, text='ProQty', font=('calibri', 20, 'bold'), bg='lightgreen').grid(row=0, column=3)
    Label(viewpage, text='ProTotalPrice', font=('calibri', 20, 'bold'), bg='lightgreen').grid(row=0, column=4)

    for i in range(rows):
        for j in range(cols):
            s = Entry(viewpage, font=('calibri', 13))
            s.grid(row=i+1, column=j)
            s. insert(END, data[i][j])


obj = Tk()
obj.geometry('1000x650')
obj.title('Access control matrix')
obj.configure(bg='lightblue')

Label(obj,
      text='Products Entry',
      font=('calibri', 35)).place(x=400, y=20)

product_id_label = Label(obj,
                         text='Product id',
                         font=('calibri', 25, 'bold'),
                         bg='lightblue')
product_id_label.place(x=300, y=100)
product_id = StringVar()
product_id_entry = Entry(obj,
                         textvariable=product_id,
                         font=('calibri', 20, 'bold'))
product_id_entry.place(x=550, y=100)

product_name_label = Label(obj,
                         text='Product Name',
                         font=('calibri', 25, 'bold'),
                         bg='lightblue')

product_name_label.place(x=300, y=150)
product_name = StringVar()
product_name_entry = Entry(obj,
                         textvariable=product_name,
                         font=('calibri', 20, 'bold'))
product_name_entry.place(x=550, y=150)

product_price_label = Label(obj,
                         text='Product Price',
                         font=('calibri', 25, 'bold'),
                         bg='lightblue')

product_price_label.place(x=300, y=200)
product_price = IntVar()
product_price_entry = Entry(obj,
                         textvariable=product_price,
                         font=('calibri', 20, 'bold'))
product_price_entry.place(x=550, y=200)

product_qty_label = Label(obj, text='Product Quality', font=('calibri', 25, 'bold'), bg='lightblue')

product_qty_label.place(x=300, y=250)
product_qty = IntVar()
product_qty_entry = Entry(obj, textvariable=product_qty, font=('calibri', 20, 'bold'))
product_qty_entry.place(x=550, y=250)

product_tot_label = Label(obj, text='Product Total', font=('calibri', 25, 'bold'), bg='lightblue')

product_tot_label.place(x=300, y=300)
product_tot = IntVar()
product_tot_entry = Entry(obj, textvariable=product_tot, font=('calibri', 20, 'bold'))
product_tot_entry.place(x=550, y=300)


but_cal =Button(obj,
                text='Calculate',
                command=calculate,
                font=('calibri', 15, 'bold'),
                bg='lightblue',
                fg='white',
                width='10',
                height='1')
but_cal.place(x=850, y=250)

but_add =Button(obj,
                text='ADD',
                command=add,
                font=('calibri', 15, 'bold'),
                bg='lightblue',
                fg='white',
                width='10',
                height='1')
but_add.place(x=300, y=400)

but_view =Button(obj,
                text='VIEW',
                command=view,
                font=('calibri', 15, 'bold'),
                bg='lightblue',
                fg='white',
                width='10',
                height='1')
but_view.place(x=500, y=400)

but_upd =Button(obj,
                text='UPDATE',
                command=update,
                font=('calibri', 15, 'bold'),
                bg='lightblue',
                fg='white',
                width='10',
                height='1')
but_upd.place(x=700, y=400)

but_del =Button(obj,
                text='DELETE',
                command=delete,
                font=('calibri', 15, 'bold'),
                bg='lightblue',
                fg='white',
                width='10',
                height='1')
but_del.place(x=300, y=500)

but_clr = Button(obj,
                text='CLEAR',
                command=clear,
                font=('calibri', 15, 'bold'),
                bg='lightblue',
                fg='white',
                width='10',
                height='1')
but_clr.place(x=500, y=500)

but_ovr =Button(obj,
                text='OVER ALL',
                command=overall,
                font=('calibri', 15, 'bold'),
                bg='lightblue',
                fg='white',
                width='10',
                height='1')
but_ovr.place(x=700, y=500)


obj.mainloop()