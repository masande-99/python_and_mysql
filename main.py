from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql
import os


def update():
    username_info = update_username.get()
    password_info = update_password.get()
    full_name_info = update_full_name.get()

    if(username_info == "" or password_info == "" or full_name_info == ""):
        messagebox.showinfo("Update status", "All fields are required")
    else:
        con = mysql.connect(host="localhost", user="lifechoices", password="@Lifechoices1234", database="lifechoicesonline")
        cursor = con.cursor()
        cursor.execute("update users set fullname='" + full_name_info + "',username='" + username_info + "', password='" + password_info + "'")
        con.commit()

        update_username.delete(0, END)
        update_password.delete(0, END)
        update_full_name.delete(0, END)


def update_users():
    global screen8
    screen8 = Toplevel(screen)
    screen8.title("Register")
    screen8.geometry("300x300")
    screen8.config(bg="red")

    global update_password
    global update_username
    global update_mobile_number
    global update_full_name

    global update_username_entry
    global update_password_entry
    global update_mobile_number_entry
    global update_full_name_entry

    update_username = StringVar()
    update_password = StringVar()
    update_mobile_number = IntVar()
    update_full_name = StringVar()

    Label(screen8, bg="blue", text="Please enter details below").pack()
    Label(screen8, text="").pack()
    Label(screen8, bg="red", text="Full name").pack()
    update_full_name_entry = Entry(screen8, textvariable=update_full_name)
    update_full_name_entry.pack()
    Label(screen8, bg="red", text="Username").pack()
    update_username_entry = Entry(screen8, textvariable=update_username)
    update_username_entry.pack()
    Label(screen8, bg="red", text="Password").pack()
    update_password_entry = Entry(screen8, textvariable=update_password)
    update_password_entry.pack()
    Label(screen8, text="").pack()
    Button(screen8, bg="orange", text="Register", width="10", height="1", command=update).pack()


def user_not_found():
    messagebox.showinfo("Insert status", "All fields are required")


def register_user():

    username_info = username.get()
    password_info = password.get()
    full_name_info = full_name.get()

    if(username_info == "" or password_info == "" or full_name_info == ""):
        messagebox.showinfo("Insert status", "All fields are required")
    else:
        con = mysql.connect(host="localhost", user="lifechoices", password="@Lifechoices1234", database="lifechoicesonline")
        cursor = con.cursor()
        sql = "INSERT INTO users(fullname, username, password) VALUES (%s, %s, %s)"
        val = (full_name_info, username_info, password_info)
        cursor.execute(sql, val)
        con.commit()

        print(cursor.rowcount, "record inserted")

        messagebox.showinfo("Insert Status", "Inserted Successfully")

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    full_name_entry.delete(0, END)


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x300")
    screen1.config(bg="red")

    global password
    global username
    global mobile_number
    global full_name

    global username_entry
    global password_entry
    global mobile_number_entry
    global full_name_entry

    username = StringVar()
    password = StringVar()
    mobile_number = IntVar()
    full_name = StringVar()

    Label(screen1, bg="blue", text="Please enter details below").pack()
    Label(screen1, text="").pack()
    Label(screen1, bg="red", text="Full name").pack()
    full_name_entry = Entry(screen1, textvariable=full_name)
    full_name_entry.pack()
    Label(screen1, bg="red", text="Username").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, bg="red", text="Password").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, bg="orange", text="Register", width="10", height="1", command=register_user).pack()


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()

    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    if(username1 == "" or password1 == ""):
        messagebox.showinfo("Insert status", "All fields are required")
    else:
        mydb = mysql.connect(host="localhost", user="lifechoices", password="@Lifechoices1234", database="lifechoicesonline")
        mycursor = mydb.cursor()
        sql = "select * from users where username = %s and password = %s"
        mycursor.execute(sql, [(username1), (password1)])
        results = mycursor.fetchall

        if results:
            messagebox.showinfo("Login status", "Logged successfully")
        else:
            fail()


def admin_login_verify():
    admin_username_info = username_verify.get()
    admin_password_info = password_verify.get()

    if(admin_username == "" or admin_password == ""):
        messagebox.showinfo("Insert status", "All fields are required")
    else:
        mydb = mysql.connect(host="localhost", user="lifechoices", password="@Lifechoices1234", database="lifechoicesonline")
        mycursor = mydb.cursor()
        sql = "select * from admins where username = %s and password = %s"
        mycursor.execute(sql, [(admin_username_info), (admin_password_info)])
        results = mycursor.fetchall

        if results:
            messagebox.showinfo("Login status", "Logged successfully")
        else:
            fail()


def fail():
    messagebox.showerror("Unsuccesful")


def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    screen2.config(bg="red")

    global username_verify
    global password_verify
    global username_entry1
    global password_entry1

    username_verify = StringVar()
    password_verify = StringVar()

    Label(screen2, bg="blue", text="PLEASE ENTER DETAILS BELOW").pack()
    Label(screen2, text="").pack()
    Label(screen2, bg="red", text="Username").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, bg="red", text="Password").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, bg="green", text="Login", width="10", height="1", command=login_verify).pack()


def login_admin():
    global screen6
    screen6 = Toplevel(screen)
    screen6.title("Login")
    screen6.geometry("300x250")
    screen6.config(bg="red")

    global username_verify
    global password_verify
    global username_entry1
    global password_entry1

    username_verify = StringVar()
    password_verify = StringVar()

    Label(screen6, bg="blue", text="PLEASE ENTER DETAILS BELOW").pack()
    Label(screen6, text="").pack()
    Label(screen6, bg="red", text="Username").pack()
    username_entry1 = Entry(screen6, textvariable=username_verify)
    username_entry1.pack()
    Label(screen6, text="").pack()
    Label(screen6, bg="red", text="Password").pack()
    password_entry1 = Entry(screen6, textvariable=password_verify)
    password_entry1.pack()
    Label(screen6, text="").pack()
    Button(screen6, bg="green", text="Login", width="10", height="1", command=admin_login_verify).pack()


def register_user_as_admin():

    admin_username_info = admin_username.get()
    admin_password_info = admin_password.get()
    admin_full_name_info = admin_full_name.get()

    if(admin_username_info == "" or admin_password_info == "" or admin_full_name_info == ""):
        messagebox.showinfo("Insert status", "All fields are required")
    else:
        con = mysql.connect(host="localhost", user="lifechoices", password="@Lifechoices1234", database="lifechoicesonline")
        cursor = con.cursor()
        sql = "INSERT INTO users(fullname, username, password) VALUES (%s, %s, %s)"
        val = (admin_full_name_info, admin_username_info, admin_password_info)
        cursor.execute(sql, val)
        con.commit()
        messagebox.showinfo("Insert Status", "Inserted Successfully")

        print(cursor.rowcount, "record inserted")

    admin_username_entry.delete(0, END)
    admin_password_entry.delete(0, END)
    admin_full_name_entry.delete(0, END)


def register_adminsql():
    admin_username_info = admin_username.get()
    admin_password_info = admin_password.get()
    admin_full_name_info = admin_full_name.get()

    if(admin_username_info == "" or admin_password_info == "" or admin_full_name_info == ""):
        messagebox.showinfo("Insert status", "All fields are required")
    else:
        con = mysql.connect(host="localhost", user="lifechoices", password="@Lifechoices1234", database="lifechoicesonline")
        cursor = con.cursor()
        sql = "INSERT INTO admins(fullname, username, password) VALUES (%s, %s, %s)"
        val = (admin_full_name_info, admin_username_info, admin_password_info)
        cursor.execute(sql, val)
        con.commit()

        messagebox.showinfo("Insert Status", "Inserted Successfully")

    admin_username_entry.delete(0, END)
    admin_password_entry.delete(0, END)
    admin_full_name_entry.delete(0, END)


def register_admin():
    global screen7
    screen7 = Toplevel(screen)
    screen7.title("Register")
    screen7.geometry("300x350")
    screen7.config(bg="red")

    global admin_password
    global admin_username
    global admin_full_name

    global admin_username_entry
    global admin_password_entry
    global admin_full_name_entry

    admin_username = StringVar()
    admin_password = StringVar()
    admin_full_name = StringVar()

    Label(screen7, bg="blue", text="Please enter details below").pack()
    Label(screen7, text="").pack()
    Label(screen7, bg="red", text="Full name").pack()
    admin_full_name_entry = Entry(screen7, textvariable=admin_full_name)
    admin_full_name_entry.pack()
    Label(screen7, bg="red", text="Username").pack()
    admin_username_entry = Entry(screen7, textvariable=admin_username)
    admin_username_entry.pack()
    Label(screen7, bg="red", text="Password").pack()
    admin_password_entry = Entry(screen7, textvariable=admin_password)
    admin_password_entry.pack()
    Label(screen7, text="").pack()
    Button(screen7, bg="orange", text="Register admin", width="10", height="1", command=register_adminsql).pack()
    Label(screen7, text="").pack()
    Button(screen7, bg="green", text="update", width="10", height="1", command=update_users).pack()
    Label(screen7, text="").pack()
    Button(screen7, bg="yellow", text="register user", width="10", height="1", command=register_user_as_admin).pack()


def admin_main():

    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Admin")
    screen4.geometry("300x250")
    Label(screen4, text="WELCOME ADMIN", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(screen4, text="").pack()
    Button(screen4, bg="green", text="Login", height="2", width="30", command=login_admin).pack()
    Label(screen4, text="").pack()
    Button(screen4, bg="orange", text="Register", height="2", width="30", command=register_admin).pack()
    Label(screen4, text="").pack()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x300")
    screen.title("User")
    screen.config(bg="red")

    Label(text="WELCOME TO LIFECHOICES", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(bg="yellow", text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(bg="orange", text="Register", height="2", width="30", command=register).pack()
    Label(text="").pack()
    Button(bg="green", text="Admin", height="2", width="30", command=admin_main).pack()

    screen.mainloop()
main_screen()
