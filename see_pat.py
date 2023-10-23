import shutil
from tkinter import *
import tkinter.font as font
from tkinter import messagebox
from tkinter import filedialog
from ttkwidgets.autocomplete import *
from openpyxl import load_workbook
import add_pat
import edit_pat
import re
import os

def main():

    def name_auto(t, T2, T5, l_pat_dict):
        name=T2.get().strip()
        if(name in l_pat_dict.keys()):
            T5.insert(INSERT, l_pat_dict[name])
        else:
            messagebox.showinfo("Edit Patient","No Patient Found")
            print("Empty Field!")
        print("Auto Name")

    #see patient details
    def see(t, T5 , T2, menu1, menu2, window1):
        name=T2.get().strip()
        indoor=T5.get("1.0", "end-1c").strip()
        f=open(r'res\\extras.txt', 'r')
        l=f.readlines()
        if(len(l)==0 or l[0]==""):
            messagebox.showinfo("See Patient","First Add a Patient")
            print("See Patient Error")
            f.close()
        
        else:
            parent_dir=l[0]
            folder_name=name+"-"+indoor
            year=menu1.get()
            month=menu2.get()
            if(year=="Select Year" or month=="Select Month" or name=="" or indoor==""):
                messagebox.showinfo("See Patient","Please fill up the details")
                print("No Patient Error")
                T2.delete(0, END)
                T5.delete('1.0', END)

            l_year=os.listdir(l[0])

            if(year in l_year):
                l1=os.listdir(parent_dir+year+"/")
                if(month in l1):
                    l2=os.listdir(parent_dir+year+"/"+month+"/")
                    parent_dir=parent_dir+year+"/"+month+"/"
                    if(folder_name in l2):
                        os.startfile(parent_dir+folder_name)
                        window1.destroy()
                    else:
                        messagebox.showinfo("See Patient","No Patient Found")
                        print("No Month Error")
                        T2.delete(0, END)
                        T5.delete('1.0', END)
                else:
                    messagebox.showinfo("See Patient","No Month Found")
                    print("No Month Error")
                    T2.delete(0, END)
                    T5.delete('1.0', END)
                    
            else:
                messagebox.showinfo("See Patient","No Year Found")
                print("No Year Error")
                T2.delete(0, END)
                T5.delete('1.0', END)

    def see_patients_see(t, menu1, menu2, window1):

        f=open(r'res\\extras.txt', 'r')
        l=f.readlines()
        l_pat_dict=dict()
        l_pat_name=[]
        if(len(l)==0 or l[0]==""):
            messagebox.showinfo("See Patient","First Add a Patient")
            print("See Patient Error")
        
        else:
            parent_dir=l[0]
            year=menu1.get()
            month=menu2.get()
            if(year=="Select Year" or month=="Select Month"):
                messagebox.showinfo("See Patient","Please fill up the details")
                print("No Patient Error")
                return
            else:
                l_year=os.listdir(l[0])
                if(year in l_year):
                    l1=os.listdir(parent_dir+year+"/")
                    if(month not in l1):
                        messagebox.showinfo("See Patient","No Month Found")
                        print("No Patient Error")
                        return
                    else:
                        window1.destroy()
                        l_pat=os.listdir(parent_dir+year+"/"+month+"/")
                        for pat in l_pat:
                            pat=pat.split("-")
                            l_pat_name.append(pat[0])
                            l_pat_dict[pat[0]]=pat[1]
        

        window2 = Tk()
        lbl = Label(window2, text="Name", fg='white', bg='blue', font=("Times New Roman", 20))
        lbl.place(x=20, y=20)

        T2 = AutocompleteCombobox(window2, width=30, completevalues=l_pat_name)
        T2.place(x=95,y=28)

        # T2 = Text(window2, bg='white', fg='black', height=1.4, width=30, padx=1, pady=1)
        # T2.place(x=95,y=28)

        lbl = Label(window2, text="Indoor Reg. No.", fg='white', bg='blue', font=("Times New Roman", 20))
        lbl.place(x=20, y=73)

        T5 = Text(window2, bg='white', fg='black', height=1.4, width=15, padx=1, pady=1)
        T5.place(x=200,y=80)

        # See button
        btn = Button(window2, text="Ok", fg='black', command=lambda t="See Patient Button Clicked": see(t, T5, T2, menu1, menu2, window2))
        btn['font'] = myFont
        btn.place(x=160, y=120)

        myFont2 = font.Font(size=5)

        btn1 = Button(window2, text="A", fg='black', command=lambda t="Auto Name Button Clicked": name_auto(t, T2, T5, l_pat_dict))
        btn1['font'] = myFont2
        btn1.place(x=310, y=25)

        window2.title('See Patient')
        window2.geometry("350x180")
        window2.configure(bg='blue')
        window2.mainloop()

    f=open(r'res\\extras.txt', 'r')
    l=f.readlines()
    if(len(l)==0 or l[0]==""):
        messagebox.showinfo("see Patient","First Add a Patient")
        print("see Patient Error")
        f.close()


    else:
        l_year=os.listdir(l[0])
        if(len(l_year)==0 or l_year[0]==""):
            messagebox.showinfo("see Patient","First Add a Patient")
            print("see Patient Error")
            f.close()
        else:

            window1 = Tk()

            # declaring the common font size for all the buttons
            myFont = font.Font(size=15)

            #Set the Menu initially
            menu1= StringVar(window1)
            menu1.set("Select Year")

            #Create a dropdown Menu
            drop1= OptionMenu(window1, menu1, *l_year)
            drop1.place(x=30,y=20)

            #Set the Menu initially
            menu2= StringVar(window1)
            menu2.set("Select Month")
            #Create a dropdown Menu
            drop2= OptionMenu(window1, menu2, *["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
            drop2.place(x=200,y=20)

            # See button
            btn = Button(window1, text="Ok", fg='black', command=lambda t="See Patient Button Clicked": see_patients_see(t, menu1, menu2, window1))
            btn['font'] = myFont
            btn.place(x=160, y=70)


            window1.title('see Patient')
            window1.geometry("350x120")
            window1.configure(bg='blue')
            window1.mainloop()
            print("see patients")