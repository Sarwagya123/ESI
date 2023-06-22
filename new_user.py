from tkinter import *
import tkinter.font as font
from tkinter import messagebox

def create(t, T1, T2, window):
    id = T1.get("1.0", "end-1c")
    id=id.strip()
    T1.delete(1.0, "end-1c")
    password = T2.get("1.0", "end-1c")
    password=password.strip()
    T2.delete(1.0, "end-1c")
    if(id=="" or password==""):
        messagebox.showinfo("user", "Please fill all the details")
        return
    print(id)
    print(password)

    f=open(r'res\\login.txt', 'r')
    l=f.readlines()
    flag=True

    #Checking if the user already exists
    for i in l:
        l2=i.split(',')
        if(l2[0]==id):
            messagebox.showinfo("user","User Already Exists")
            flag=False
            return
    
    if(flag):
        f.close()

    f=open(r'res\\login.txt', 'a')
    f.write(id+","+password+"\n")
    f.close()
    print("User Created Successfully")
    window.destroy()


def main():
    f=open(r'res\\login.txt', 'a')

    window = Tk()
    # declaring the common font size for all the buttons
    myFont = font.Font(family="Times New Roman",size=15)

    lbl1 = Label(window, text="New User Creation", fg='red', bg='turquoise', font=("Times New Roman", 30))
    lbl1.place(x=85, y=25)

    lbl2 = Label(window, text="Log-In ID", fg='black', bg='turquoise', font=("Times New Roman", 20))
    lbl2.place(x=30, y=100)

    T1 = Text(window, bg='white', fg='black', height=1.4, width=25, padx=1, pady=1)
    T1.place(x=170,y=108)

    lbl3 = Label(window, text="Password", fg='black', bg='turquoise', font=("Times New Roman", 20))
    lbl3.place(x=30, y=150)

    T2 = Text(window, bg='white', fg='black', height=1.4, width=25, padx=1, pady=1)
    T2.place(x=170,y=158)

    btn2 = Button(window, text="Create User", fg='black', command=lambda t="New User Button Clicked": create(t, T1, T2, window))
    btn2['font'] = font.Font(family="Times New Roman",size=14)
    btn2.place(x=165, y=220)

    window.title('New User')
    window.geometry("450x270")
    window.configure(bg='turquoise')
    window.mainloop()
