import tkinter.messagebox
from tkinter import *
import mysql.connector

db = mysql.connector.connect(host='localhost', user='root', password='', db='authenticate')
cursor = db.cursor()

def admin():
    global admin_frame, admin_username, admin_password
    admin_frame = Frame(homepage, width=350, height=200)
    admin_frame.place(x=100, y=150)
    admin_username = StringVar()
    admin_password = StringVar()
    Label(admin_frame,
          text='Username',
          font=('Impact', 14)).place(x=30, y=30)
    Label(admin_frame,
          text='Password',
          font=('Impact', 14)).place(x=30, y=80)
    Entry(admin_frame,
          textvariable=admin_username,
          font=('Impact', 12),
          bg='lightblue').place(x=150, y=30)
    Entry(admin_frame,
          textvariable=admin_password,
          font=('Impact', 12),
          bg='lightblue').place(x=150, y=80)
    Button(admin_frame,
           text='Login',
           command=admin_login,
           font=('Impact',14),
           bg='blue',
           fg='white',
           width='8',
           height='1').place(x=220,y=130)

def admin_login():
    username = admin_username.get()
    password = admin_password.get()
    if username == 'admin' and password == 'admin':
        tkinter.messagebox.showinfo('Authenticate' , 'Welcome Admin ')
        admin_home()
    else:
        tkinter.messagebox.showinfo('Authenticate' , 'Invalid')

def admin_home():
    global admin_page
    admin_page = Toplevel(homepage)
    admin_page.geometry('1000x500')
    admin_page.title('Admin Home')
    admin_page.configure(bg='lightblue')
    pending = Button(admin_page, text='Pending list', command=pending_data, font=('Impact',15), bg='blue', fg='white', width='12', height='1')
    pending.grid(row=0,column=0)
    approved = Button(admin_page, text='Approved list', command=approve_data, font=('Impact', 15), bg='blue', fg='white', width='12', height='1')
    approved.grid(row=0, column=1)


def pending_data():
    cursor.execute('select * from details where Status=%s',['Pending'])
    data = cursor.fetchall()
    rows = len(data)
    cols = len(data[0])
    Label(admin_page, text='Name', font=('Impact',13,'bold'), bg='lightgreen').grid(row=1,column=0)
    Label(admin_page, text='Mail', font=('Impact',13,'bold'), bg='lightgreen').grid(row=1,column=1)
    Label(admin_page, text='Address', font=('Impact',13,'bold'), bg='lightgreen').grid(row=1,column=2)
    Label(admin_page, text='Gender', font=('Impact',13,'bold'), bg='lightgreen').grid(row=1,column=3)
    Label(admin_page, text='Username', font=('Impact',13,'bold'), bg='lightgreen').grid(row=1,column=4)
    Label(admin_page, text='Password', font=('Impact',13,'bold'), bg='lightgreen').grid(row=1,column=5)
    Label(admin_page, text='Status', font=('Impact',13,'bold'), bg='lightgreen').grid(row=1,column=6)
    Label(admin_page, text='Action', font=('Impact',13,'bold'), bg='lightgreen').grid(row=1,column=7)

    for i in range(rows):
        for j in range(cols):
            s = Entry(admin_page, font=('Impact',11))
            s.grid(row=i+2,column=j)
            s.insert(END,data[i][j])
        b1 = Button(admin_page, text='Approved', command=lambda: approve(data[i][0]), font=('Impact',10),
                    width='8', height='1')
        b1.grid(row=i+2,column=cols+1)
        b2 = Button(admin_page, text='Delete', command=lambda: delete(data[i][0]), font=('Impact', 10),
                     width='8', height='1')
        b2.grid(row=i + 2, column=cols + 2)

def approve(name):
    cursor.execute('update details set Status=%s where Name=%s', ['Approved', name])
    db.commit()
    tkinter.messagebox.showinfo('Authorize', 'Status Updataed')

def delete(name):
    cursor.execute('delete from details where Name=%s', [name])
    db.commit()
    tkinter.messagebox.showinfo('Authorize', 'Record Deleted')

def approve_data():
        cursor.execute('select * from details where Status=%s', ['Approved'])
        data = cursor.fetchall()
        rows = len(data)
        cols = len(data[0])
        Label(admin_page, text='Name', font=('Impact', 13, 'bold'), bg='lightgreen').grid(row=1, column=0)
        Label(admin_page, text='Mail', font=('Impact', 13, 'bold'), bg='lightgreen').grid(row=1, column=1)
        Label(admin_page, text='Address', font=('Impact', 13, 'bold'), bg='lightgreen').grid(row=1, column=2)
        Label(admin_page, text='Gender', font=('Impact', 13, 'bold'), bg='lightgreen').grid(row=1, column=3)
        Label(admin_page, text='Username', font=('Impact', 13, 'bold'), bg='lightgreen').grid(row=1, column=4)
        Label(admin_page, text='Password', font=('Impact', 13, 'bold'), bg='lightgreen').grid(row=1, column=5)
        Label(admin_page, text='Status', font=('Impact', 13, 'bold'), bg='lightgreen').grid(row=1, column=6)


        for i in range(rows):
            for j in range(cols):
                s = Entry(admin_page, font=('Impact', 11))
                s.grid(row=i + 2, column=j)
                s.insert(END, data[i][j])



def user():
    global user_frame, user_username, user_password
    user_frame = Frame(homepage, width=350, height=200)
    user_frame.place(x=500, y=150)
    user_username = StringVar()
    user_password = StringVar()
    Label(user_frame,
          text='Username',
          font=('Impact', 14)).place(x=30, y=30)
    Label(user_frame,
          text='Userpassword',
          font=('Impact', 14)).place(x=30, y=80)

    Entry(user_frame,
          textvariable=user_username,
          font=('Impact', 12),
          bg='lightblue').place(x=150, y=30)
    Entry(user_frame,
          textvariable=user_password,
          font=('Impact', 12),
          bg='lightblue').place(x=150, y=80)
    Button(user_frame,
           text='SignIn',
           command=register,
           font=('Impact', 14),
           bg='blue', fg='white',
           width='8',
           height='1').place(x=30, y=130)
    Button(user_frame,
           text='Login',
           command=user_login,
           font=('Impact', 14),
           bg='blue',
           fg='white',
           width='8',
           height='1').place(x=220, y=130)

def user_login():
    username = user_username.get()
    password = user_password.get()
    cursor.execute('select * from details where Username = %s and Password = %s', [username, password])
    data  = cursor.fetchone()
    if data  != None:
        status = data[6]
        if status == 'Approved':
            tkinter.messagebox.showinfo('Authenticate','Welcome User ')
        else:
            tkinter.messagebox.showinfo('Authenticate','Your Account not yet activated ')
    else:
        tkinter.messagebox.showinfo('Authenticate','Invalid User ')
        cursor.execute('select * from details where Username = %s', [username])
        data1 = cursor.fetchone()
        count = data1[7]
        if  count is None:
            c = 1
        else:
            c = int(count)
            c += 1
        cursor.execute('update details set count = %s where Username = %s', (c, username))
        db.commit()
        if c <= 3:
            tkinter.messagebox.showwarning('Password', 'Wrong Password')
        else:
            tkinter.messagebox.showwarning('Password', 'Your account has been locked')
            cursor.execute('update details set Status = %s where Username = %s', ('Pending', username))
            db.commit()
            c = 0
            cursor.execute('update details set count = %s where Username = %s', (c, username))
            db.commit()



def register():
    global register_frame, register_name, register_mail, register_address, register_gender
    global register_username, register_password
    register_frame = Frame(homepage, width=350, height=500)
    register_frame.place(x=900, y=150)
    register_name = StringVar()
    register_mail = StringVar()
    register_address = StringVar()
    register_gender = StringVar()
    register_username = StringVar()
    register_password = StringVar()
    Label(register_frame,
          text='Name',
          font=('Impact', 14)).place(x=30, y=30)
    Label(register_frame,
          text='Mail',
          font=('Impact', 14)).place(x=30, y=80)
    Label(register_frame,
          text='Address',
          font=('Impact', 14)).place(x=30, y=130)
    Label(register_frame,
          text='Gender',
          font=('Impact', 14)).place(x=30, y=180)
    Label(register_frame,
          text='username',
          font=('Impact', 14)).place(x=30, y=230)
    Label(register_frame,
          text='password',
          font=('Impact', 14)).place(x=30, y=280)
    Entry(register_frame,
          textvariable=register_name,
          font=('Impact',12),
          bg='lightblue').place(x=150, y=30)
    Entry(register_frame,
          textvariable=register_mail,
          font=('Impact', 12),
          bg='lightblue').place(x=150, y=80)
    Entry(register_frame,
          textvariable=register_address,
          font=('Impact', 12),
          bg='lightblue').place(x=150, y=130)
    Radiobutton(register_frame,
                text='Male',
                variable=register_gender,
                value='Male',
                font=('Impact', 12)).place(x=150, y=180)
    Radiobutton(register_frame,
                text='Female',
                variable=register_gender,
                value='Female',
                font=('Impact', 12)).place(x=240, y=180)
    Entry(register_frame,
          textvariable=register_username,
          font=('Impact', 12),
          bg='lightblue').place(x=150, y=230)
    Entry(register_frame,
          textvariable=register_password,
          font=('Impact', 12),
          bg='lightblue').place(x=150, y=280)
    Button(register_frame,
           text='Submit',
           command=store_data,
           font=('Impact',14),
           bg='blue',
           fg='white',
           width='8',
           height='1').place(x=220,y=330)

def store_data():
    name = register_name.get()
    mail = register_mail.get()
    address = register_address.get()
    gender = register_gender.get()
    username = register_username.get()
    password = register_password.get()
    cursor.execute('insert into details values(%s,%s,%s,%s,%s,%s,%s)', [name, mail, address, gender, username, password, 'Pending'])
    db.commit()
    tkinter.messagebox.showinfo('Authenticate''Registered Successfully')

def startpage():
    global homepage
    homepage = Tk()
    homepage.geometry('1400x600')
    homepage.title('Authentication')
    homepage.configure(bg='lightblue')
    Label(homepage,
          text='Welcome to login page',
          font=('Impact', 25),
          fg='lightgreen').place(x=400, y=20)
    Button(homepage,
           text='Admin',
           command=admin,
           font=('Impact', 20, 'bold'),
           bg='white',
           fg='lightgreen',
           width='12',
           height='1').place(x=100,y=70)
    Button(homepage,
           text='User',
           command=user,
           font=('Impact', 20, 'bold'),
           bg='white',
           fg='lightgreen',
           width='12',
           height='1').place(x=900, y=70)
    homepage.mainloop()

startpage()




