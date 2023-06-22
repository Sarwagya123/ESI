from tkinter import *
import tkinter.font as font
from tkinter import messagebox
from tkinter import filedialog
from openpyxl import load_workbook
import datetime
import pandas as pd
import time
import os
import pharmacy
import main_bill
import challan


def main(dest_path):

    def gen_bill(t):
        main_bill.main(dest_path)
        print("Generate Bill")

    def gen_challan(t):
        challan.main(dest_path)
        print("Generate Challan")

    def edit_pharmacy(t, dest_path):
        f=open(dest_path+"patient_details.txt", 'r')
        l=f.readlines()
        doa=l[5].strip()
        dod=l[6].strip()
         #Parse the dates from strings into datetime objects
        date1 = time.mktime(time.strptime(doa, "%d-%m-%Y"))
        date2 = time.mktime(time.strptime(dod, "%d-%m-%Y"))
        
        # No. of days the patient is staying
        nod = int((date2-date1) / 86400) + 1

        # storing the dates the patient was there in the hospital
        test_date = datetime.datetime.strptime(doa, "%d-%m-%Y")
        dates = pd.date_range(test_date, periods=nod)
        dates=map(str, dates)
        dates=[i[0:10] for i in dates]
        for i in range(0,len(dates)):
            year=""
            month=""
            day=""
            for j in range(0, len(dates[i])):
                if(j<=3):
                    year=year+dates[i][j]
                elif(j>4 and j<=6):
                    month=month+dates[i][j]
                elif(j>7):
                    day=day+dates[i][j]
            dates[i]=day+"-"+month+"-"+year

        pharmacy.main(dates, dest_path)
        f.close()

    def edit_lab(t):
        os.startfile(dest_path+"Lab.xlsx")
    
    #Edit Patient GUI
    window = Tk()

    lbl = Label(window, text="Edit Patient", fg='red', bg='turquoise', font=("Times New Roman", 30))
    lbl.place(x=55, y=20)

    # declaring the common font size for all the buttons
    myFont = font.Font(size=15)

    # Main Bill button
    btn = Button(window, text="Generate Main Bill", fg='black', command=lambda t="Generate Main Bill Button Clicked": gen_bill(t))
    btn['font'] = myFont
    btn.place(x=65, y=105)

    # Generate Challan button
    btn = Button(window, text="Generate Challan", fg='black', command=lambda t="Generate Challan Button Clicked": gen_challan(t))
    btn['font'] = myFont
    btn.place(x=70, y=195)

    # Edit Patient button
    btn = Button(window, text="Edit Pharmacy", fg='black', command=lambda t="Edit Pharmacy Button Clicked": edit_pharmacy(t, dest_path))
    btn['font'] = myFont
    btn.place(x=80, y=285)

    # See Patient button
    btn = Button(window, text="Edit Lab", fg='black', command=lambda t="Edit Lab Button Clicked": edit_lab(t))
    btn['font'] = myFont
    btn.place(x=105, y=375)

    window.title('Edit Patient')
    window.geometry("300x450")
    window.configure(bg='turquoise')
    window.mainloop()