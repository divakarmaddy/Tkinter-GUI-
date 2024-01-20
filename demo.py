import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "divakar" and password == "rakavid":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

root = tk.Tk()

photo = PhotoImage(file='username.png')
photo = PhotoImage(file='lock.png')

root.title("Login Page")

# Customize the appearance
root.geometry("400x300")
root.configure(bg="black")

label = tk.Label(root,
                 text="Login Page",
                 font=("Impact", 20,"bold"),
                 bg="lightgray" ,
                 fg="black")
username_label = tk.Label(root,
                          text="Username",
                          font=("Impact", 12),
                          bg="lightgray" ,
                          fg="black",
                          image=photo)
password_label = tk.Label(root,
                          text="Password",
                          font=("Impact", 12),
                          bg="lightgray" ,
                          fg="black",
                          image=photo)
username_entry = tk.Entry(root,
                          font=("Impact", 12))
password_entry = tk.Entry(root,
                          show="*",
                          font=("Impact", 12))
login_button = tk.Button(root,
                         text="Login",
                         command=login,
                         font=("Impact", 12),
                         bg="green",
                         fg="white")

label.pack(pady=10)
username_label.pack(pady=5)
username_entry.pack(pady=5)
password_label.pack(pady=5)
password_entry.pack(pady=5)
login_button.pack(pady=10)

root.mainloop()
