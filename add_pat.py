from tkinter import *
import tkinter.font as font
from tkinter import messagebox
import re
import os
import pat

def main(parent_dir):

    #making the Patient Directory
    def make_dir(t, parent_dir):
        month_dict={"01":"January",
              "02":"February",
              "03":"March",
              "04":"April",
              "05":"May",
              "06":"June",
              "07":"July",
              "08":"August",
              "09":"September",
              "10":"October",
              "11":"November",
              "12":"December"}
        doa=T7.get("1.0", "end-1c")
        doa=doa.strip()
        dod=T8.get("1.0", "end-1c")
        dod=dod.strip()
        directory = T2.get("1.0", "end-1c")
        directory=directory.strip()
        indoor=T5.get("1.0", "end-1c")
        indoor=indoor.strip()
        if(doa=="" or directory=="" or indoor==""):
            messagebox.showinfo("Add Patient","Empty Field")
            print("Empty Field!")

        elif(not(re.search("^[0-9]{2}-[0-9]{2}-[0-9]{4}$",doa) and re.search("^[0-9]{2}-[0-9]{2}-[0-9]{4}$",dod))):
            messagebox.showinfo("Add Patient","Add Date in DD-MM-YYYY Format")
            print("Date Format")

        else:
            year=doa[6:]
            month=month_dict[doa[3:5]]
            folder_name=directory+"-"+indoor
            l=os.listdir(parent_dir)
            f=True
            if(year in l):
                l1=os.listdir(parent_dir+year+"/")
                if(month in l1):
                    l2=os.listdir(parent_dir+year+"/"+month+"/")
                    parent_dir=parent_dir+year+"/"+month+"/"
                    if(directory+"-"+indoor in l2):
                        messagebox.showinfo("Add Patient","Duplicate Patient!")
                        print("Duplicate Patient")
                        T2.delete(1.0, "end-1c")
                        T5.delete(1.0, "end-1c")
                        f=False
                        # f.close()
                    else:
                        for i in l2:
                            l3=i.split("-")
                            if(indoor in l3):
                                messagebox.showinfo("Add Patient","Duplicate Indoor Reg No!")
                                print("Duplicate Indoor Reg No")
                                T5.delete(1.0, "end-1c")
                                f=False
                                break
                        
                else:
                    os.mkdir(parent_dir+year+"/"+month)
                    l2=os.listdir(parent_dir+year+"/"+month+"/")
                    if(directory+"-"+indoor in l2):
                        messagebox.showinfo("Add Patient","Duplicate Patient!")
                        print("Duplicate Patient")
                        T2.delete(1.0, "end-1c")
                        f=False
                        # f.close()
                    parent_dir=parent_dir+year+"/"+month
            else:
                os.mkdir(parent_dir+year)
                l1=os.listdir(parent_dir+year+"/")
                if(month in l1):
                    l2=os.listdir(parent_dir+year+"/"+month+"/")
                    if(directory+"-"+indoor in l2):
                        messagebox.showinfo("Add Patient","Duplicate Patient!")
                        print("Duplicate Patient")
                        T2.delete(1.0, "end-1c")
                        f=False
                        # f.close()
                    parent_dir=parent_dir+year+"/"+month+"/"

                else:
                    os.mkdir(parent_dir+year+"/"+month)
                    l2=os.listdir(parent_dir+year+"/"+month+"/")
                    if(directory+"-"+indoor in l2):
                        messagebox.showinfo("Add Patient","Duplicate Patient!")
                        print("Duplicate Patient")
                        T2.delete(1.0, "end-1c")
                        f=False
                        # f.close()
                    parent_dir=parent_dir+year+"/"+month+"/"

            if(f):
                age=T3.get("1.0", "end-1c")
                age=age.strip()
                relation=T4.get("1.0", "end-1c")
                relation=relation.strip()
                gender=T6.get("1.0", "end-1c")
                gender=gender.strip()
                insurance=T9.get("1.0", "end-1c")
                insurance=insurance.strip()
                if(age=="" or relation=="" or gender=="" or dod=="" or insurance==""):
                    messagebox.showinfo("Add Patient","Empty Field")
                    print("Empty Field!")
                
                elif(not(age.isnumeric())):
                    messagebox.showinfo("Add Patient","Age should be numeric")
                    T3.delete(1.0, "end-1c")
                    print("Non-numeric Age")
                
                elif(not(gender.lower() == "m" or gender.lower() == "f" or gender.lower() == "male" or gender.lower() == "female" or gender.lower() == "others")):
                    messagebox.showinfo("Add Patient","Please enter the correct gender")
                    T6.delete(1.0, "end-1c")
                    print("Correct the gender")
                
                
                #writing the patient details in a text file inside the directory
                else:
                    path = os.path.join(parent_dir, folder_name)
                    os.mkdir(path)
                    dest_path=path+"/"
                    f = open(dest_path+"patient_details.txt", "x")
                    f = open(dest_path+"patient_details.txt", "w")
                    f.write(directory+"\n")
                    f.write(age+"\n")
                    f.write(relation+"\n")
                    f.write(indoor+"\n")
                    f.write(gender+"\n")
                    f.write(doa+"\n")
                    f.write(dod+"\n")
                    f.write(insurance+"\n")
                    f.write(month+"\n")
                    f.write(year+"\n")
                    f.close()
                    window.destroy()
                    pat.main(dest_path, directory, doa, dod, insurance)


    #GUI for adding patient details
    window = Tk()

    # declaring the common font size for all the buttons
    myFont = font.Font(size=15)


    lbl = Label(window, text="Enter Patient Details", fg='yellow', bg='blue', font=("Times New Roman", 28))
    lbl.place(x=110, y=10)

    lbl = Label(window, text="Name", fg='white', bg='blue', font=("Times New Roman", 20))
    lbl.place(x=20, y=80)

    T2 = Text(window, bg='white', fg='black', height=1.4, width=30, padx=1, pady=1)
    T2.place(x=95,y=88)

    lbl = Label(window, text="Age", fg='white', bg='blue', font=("Times New Roman", 20))
    lbl.place(x=350, y=80)

    T3 = Text(window, bg='white', fg='black', height=1.4, width=10, padx=1, pady=1)
    T3.place(x=405,y=88)

    lbl = Label(window, text="Relation", fg='white', bg='blue', font=("Times New Roman", 20))
    lbl.place(x=20, y=130)

    T4 = Text(window, bg='white', fg='black', height=1.4, width=45, padx=1, pady=1)
    T4.place(x=125,y=138)

    lbl = Label(window, text="Indoor Reg. No.", fg='white', bg='blue', font=("Times New Roman", 20))
    lbl.place(x=20, y=183)

    T5 = Text(window, bg='white', fg='black', height=1.4, width=15, padx=1, pady=1)
    T5.place(x=200,y=190)

    lbl = Label(window, text="Gender", fg='white', bg='blue', font=("Times New Roman", 20))
    lbl.place(x=330, y=183)

    T6 = Text(window, bg='white', fg='black', height=1.4, width=7, padx=1, pady=1)
    T6.place(x=420,y=190)

    lbl = Label(window, text="DOA", fg='white', bg='blue', font=("Times New Roman", 20))
    lbl.place(x=20, y=233)

    T7 = Text(window, bg='white', fg='black', height=1.4, width=18, padx=1, pady=1)
    T7.place(x=87,y=240)

    lbl = Label(window, text="DOD", fg='white', bg='blue', font=("Times New Roman", 20))
    lbl.place(x=250, y=233)

    T8 = Text(window, bg='white', fg='black', height=1.4, width=18, padx=1, pady=1)
    T8.place(x=320,y=240)

    lbl = Label(window, text="Insurance No.", fg='white', bg='blue', font=("Times New Roman", 20))
    lbl.place(x=20, y=283)

    T9 = Text(window, bg='white', fg='black', height=1.4, width=25, padx=1, pady=1)
    T9.place(x=180,y=290)

    btn = Button(window, text="Add Patient", fg='black', command=lambda t="Add Patient Button Clicked": make_dir(t, parent_dir))
    btn['font'] = myFont
    btn.place(x=200, y=335)



    window.title('Add Patient')
    window.geometry("500x400")
    window.configure(bg='blue')
    window.mainloop()