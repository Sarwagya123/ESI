import shutil
from openpyxl import load_workbook


def main(dest_path, dod):
    src_path="res/Lab.xlsx"
    shutil.copy(src_path, dest_path+"Lab.xlsx")
    workbook = load_workbook(filename=dest_path+"Lab.xlsx")
    sheet = workbook.active
    sheet = workbook["Sheet 1"]
    f=open(dest_path+"patient_details.txt", 'r')
    l=f.readlines()
    sheet["D10"] = l[3]
    sheet["D9"]=l[0]+" ; "+l[4]+"/"+l[1]
    sheet["H7"] = dod
    workbook.save(filename=dest_path+"Lab.xlsx")