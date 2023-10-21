from tkinter import *
import tkinter.font as font
from tkinter import messagebox
import new_user
import admin
        

def show_pass_btn(T2, click_btn):
    if(click_btn.cget("file")=="res/hide_password_1.png"):
        T2.configure(show="*")
        click_btn.configure(file='res/show_password_1.png')
    else:
        T2.config(show="")
        click_btn.config(file='res/hide_password_1.png')
        
#function called on logging in
def login(t):
    id = T1.get("1.0", "end-1c")
    id=id.strip()
    T1.delete(1.0, "end-1c")
    password = T2.get()
    password=password.strip()
    T2.delete(0, END)
    if(id=="" or password==""):
        messagebox.showinfo("user","Please fill in the id and password")
        return
    print(id)
    print(password)
    f=open(r'res\\login.txt', 'r')
    l=f.readlines()
    flag=True
    for i in l:
        l2=i.split(',')
        print(l2)
        if(l2[0].strip()==id and l2[1].strip()==password):
            print("log in successful")
            flag=False
            f.close()
            window.destroy()
            admin.main(l2[0])
    
    if(flag):
        messagebox.showinfo("user","No such user exists")
        print("No user exist")
        f.close()
        
    
#Starting GUI
window = Tk()

# declaring the common font size for all the buttons
myFont = font.Font(family="Times New Roman",size=15)

lbl1 = Label(window, text="ESI - SHRC", fg='yellow', bg='blue', font=("Times New Roman", 30))
lbl1.place(x=130, y=30)

lbl2 = Label(window, text="Log-In ID", fg='white', bg='blue', font=("Times New Roman", 20))
lbl2.place(x=30, y=100)

T1 = Text(window, bg='white', fg='black', height=1.4, width=25, padx=1, pady=1)
T1.place(x=170,y=108)

lbl3 = Label(window, text="Password", fg='white', bg='blue', font=("Times New Roman", 20))
lbl3.place(x=30, y=150)

T2 = Entry(window, bg='white', show="*", fg='black', width=33)
T2.place(x=170,y=158)

click_btn= PhotoImage(file='res/show_password_1.png', height=18)
btn_pass= Button(window, command=lambda t="Show Pass Button Clicked": show_pass_btn(T2, click_btn) , image=click_btn, borderwidth=0)
btn_pass.place(x=380, y=158)

btn1 = Button(window, text="Log-In", fg='black', command=lambda t="LogIn Button Clicked": login(t))
btn1['font'] = myFont
btn1.place(x=190, y=200)

btn2 = Button(window, text="New User? Click Here", fg='black', command=lambda t="New User Button Clicked": new_user.main())
btn2['font'] = font.Font(family="Times New Roman",size=12)
btn2.place(x=150, y=250)


window.title('ESI')
window.geometry("450x300")
window.configure(bg='blue')
window.mainloop()