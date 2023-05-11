import csv
from datetime import date
def attendance():
    myfile=open("attendance.csv","a",newline='')
    stuwriter=csv.writer(myfile)
    data=[]
    field=["NAME","CLASS","SECTION","ROLL NO","DATE"]
    data.append(field)
    a=int(input("ENTER NO. OF STUDENTS: "))
    for i in range(a):
        name=input('ENTER YOUR NAME: ')
        sect=input("ENTER YOUR CLASS: ")
        sect2=input("ENTER YOUR SECTION: ")
        roll=input('ENTER YOUR ROLL NO: ')
        dates=date.today()
        rec=[name,sect,sect2,roll,dates]
        data.append(rec)
    stuwriter.writerows(data)
    myfile.close()
    print("ATTENDANCE TAKEN SUCCESSFULLY \n IT IS IN THE SAME LOCATION AS OF THIS PYTHON FILE")
    print()
