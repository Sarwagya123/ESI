import tkinter as tk
from tkinter import *
import tkinter.font as font
from tkinter import messagebox

verified = False

def verify(window, window1, T1, id, password):
    global verified
    code = T1.get()
    code=code.strip()
    T1.delete(0, END)
    if(not code=="12345678"):
        verified=False
        messagebox.showinfo("Incorrect Code","Kindly fill in the correct code")
        return
    else:
        messagebox.showinfo("Success!","Verified!")
        f=open(r'res\\login.txt', 'a')
        f.write(id+","+password+"\n")
        f.close()
        print("User Created Successfully")
        messagebox.showinfo("Success!","Account Created Successfully")
        window.destroy()
        verified=True
        window1.destroy()
        return

def show_pass_btn(T2, click_btn):
    if(click_btn.cget("file")=="res/hide_password_1.png"):
        T2.configure(show="*")
        click_btn.configure(file='res/show_password_1.png')
    else:
        T2.config(show="")
        click_btn.config(file='res/hide_password_1.png')

def create(t, T1, T2, window):
    id = T1.get("1.0", "end-1c")
    id=id.strip()
    T1.delete(1.0, "end-1c")
    password = T2.get()
    password=password.strip()
    T2.delete(0, END)
    if(id=="" or password==""):
        messagebox.showinfo("user", "Please fill all the details")
        return
    elif(id==password):
        messagebox.showinfo("user", "Username and Password cannot be same")
        return
    print(id)
    print(password)

    f=open(r'res\\login.txt', 'r')
    l=f.readlines()

    #Checking if the user already exists
    for i in l:
        l2=i.split(',')
        if(l2[0]==id):
            messagebox.showinfo("user","User Already Exists")
            return

    if(not verified):
        window1 = tk.Toplevel()
        
        # declaring the common font size for all the buttons
        myFont = font.Font(family="Times New Roman",size=15)

        lbl1 = Label(window1, text="Please enter the Verification Code", fg='yellow', bg='blue', font=("Times New Roman", 18))
        lbl1.place(x=15, y=15)

        T1 = Entry(window1, bg='white', fg='black', show="*")
        T1.place(x=105,y=65)

        click_btn= PhotoImage(file='res/show_password_1.png', height=18)
        btn_pass= Button(window1, command=lambda t="Show Pass Button Clicked": show_pass_btn(T1, click_btn) , image=click_btn, borderwidth=0)
        btn_pass.place(x=240, y=65)

        btn1 = Button(window1, text="Verify", fg='black', command=lambda t="Verify Button Clicked": verify(window, window1, T1, id, password))
        btn1['font'] = myFont
        btn1.place(x=140, y=100)

        window1.title('Verification')
        window1.geometry("350x150")
        window1.configure(bg='blue')
        window1.mainloop()

    return


def main():
    f=open(r'res\\login.txt', 'a')

    window = tk.Toplevel()
    # declaring the common font size for all the buttons
    myFont = font.Font(family="Times New Roman",size=15)

    lbl1 = Label(window, text="New User Creation", fg='yellow', bg='blue', font=("Times New Roman", 30))
    lbl1.place(x=85, y=25)

    lbl2 = Label(window, text="Log-In ID", fg='white', bg='blue', font=("Times New Roman", 20))
    lbl2.place(x=30, y=100)

    T1 = Text(window, bg='white', fg='black', height=1.4, width=25, padx=1, pady=1)
    T1.place(x=170,y=108)

    lbl3 = Label(window, text="Password", fg='white', bg='blue', font=("Times New Roman", 20))
    lbl3.place(x=30, y=150)

    T2 = Entry(window, bg='white', fg='black', show="*", width=33)
    T2.place(x=170,y=158)

    click_btn= PhotoImage(file='res/show_password_1.png', height=18)
    btn_pass= Button(window, command=lambda t="Show Pass Button Clicked": show_pass_btn(T2, click_btn) , image=click_btn, borderwidth=0)
    btn_pass.place(x=380, y=158)

    btn2 = Button(window, text="Create User", fg='black', command=lambda t="New User Button Clicked": create(t, T1, T2, window))
    btn2['font'] = font.Font(family="Times New Roman",size=14)
    btn2.place(x=165, y=220)

    window.title('New User')
    window.geometry("450x270")
    window.configure(bg='blue')
    window.mainloop()
