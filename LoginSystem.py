from tkinter import *
from tkinter import messagebox
import os


def login():
    user = username.get()
    code = password.get()

    if user == "Andre" and code == "1234":
        root = Toplevel(screen)
        root.title("NAME?")
        root.geometry("1280x720+150+80")
        root.configure(bg="#d7dae2")
        root.resizable(False, False)

    elif user == "" and code == "":
        messagebox.showerror("Invalid", "Please enter Username and Password")
    elif user == "":
        messagebox.showerror("Invalid", "Username is required")
    elif code == "":
        messagebox.showerror("Invalid", "Password is required")
    elif user != "Andre" and code != "1234":
        messagebox.showerror("Invalid", "Username or Password is incorrect")
    elif user == "Andre":
        messagebox.showerror("Invalid", "Please enter a valid Username")
    elif code == "1234":
        messagebox.showerror("Invalid", "Please enter a valid assword")


def main_screen():

    global screen
    global username
    global password

    screen = Tk()
    screen.geometry("1280x720+150+80")
    screen.configure(bg="#d7dae2")

    #! icon
    image_icon = PhotoImage(file="icon.png")
    screen.iconphoto(False, image_icon)
    screen.title("Login System")

    lblTitle = Label(text="Login System", font=(
        "Arial", 50), bg="#d7dae2", fg="black")
    lblTitle.pack(pady=50)

    bordercolor = Frame(screen, bg="black", width=800, height=400)
    bordercolor.pack()

    mainframe = Frame(bordercolor, bg="#d7dae2", width=800, height=400)
    mainframe.pack(padx=20, pady=20)

    Label(mainframe, text="Username", font=(
        "Arial", 30, "bold"), bg="#d7dae2").place(x=100, y=50)
    Label(mainframe, text="Password", font=(
        "Arial", 30, "bold"), bg="#d7dae2").place(x=100, y=150)

    username = StringVar()
    password = StringVar()

    entry_username = Entry(mainframe, textvariable=username, width=12, bd=2,
                           font=("Arial", 30))
    entry_username.place(x=400, y=50)
    entry_password = Entry(mainframe, textvariable=password, width=12, bd=2,
                           font=("Arial", 30), show="*")
    entry_password.place(x=400, y=150)

    def reset():
        entry_username.delete(0, END)
        entry_password.delete(0, END)

    Button(mainframe, text="Login", height=2, width=23,
           bg="#ed3933", fg="white", bd=0, command=login).place(x=100, y=250)
    Button(mainframe, text="Reset", height=2, width=23,
           bg="#1089ff", fg="white", bd=0, command=reset).place(x=300, y=250)
    Button(mainframe, text="Exit", height=2, width=23,
           bg="#00bd56", fg="white", bd=0, command=screen.destroy).place(x=500, y=250)

    screen.mainloop()


main_screen()
