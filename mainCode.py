import mysql.connector as con
username=input("ENTER MYSQL SERVER'S USERNAME:") password=input("ENTER MYSQL SERVER'S PASSWORD:")
database=input("ENTER NAME OF DATABASE:") connect=con.connect(host="localhost",user=username,passwd=password,database=database) cursor=connect.cursor()
def AdminMenu():

print("|
|")
print("| 1:Create table doctor_details	|")
print("| 2:Describe doctor_details	|")
print("| 3:Register doctor_details	|")
print("| 4:Display all doctor_details	|")
print("| 5:Create table patient_details	|")
print("| 6:Describe patient_details	|")
print("| 7:Register patient_details	|")
print("| 8:Display all patient_details	|")
print("| 9:Create table worker_details	|")
print("| 10:Describe worker_details	|")
print("| 11:Register worker_details	|")
print("| 12:Display all worker_details	|")
print("| 13:Search Doctor details	|")
print("| 14:Search Patient details	|")
print("| 15:Search Worker details	|")
print("| 16:Update Doctor details	|")
print("| 17:Update patient details	|")
print("| 18:Update Worker details	|")
 print("| 19:Create table bill	|")
print("| 20:Enter charges of patient for Bill_details	|")
print("| 21:Show records of bill	|")
print("| 22:Delete records	|")
print("| 23:Remove All Doctor	|")
print("| 24:Remove All Patient	|")
print("| 25:Remove All Workers	|")
print("| 26:Display details of a particular doctor	|")
print("| 27:Display details of a particular Patient	|")
print("| 28:Display details of a particular worker	|")
print("| 29:Exit	|")
print("|	|")
ef UserMenu():
print("|	|")
print("| 1:Display details of a particular Doctor	|")
print("| 2:Display details of a particular Patient	|")
print("| 3:Display details of a particular Worker	|")
print("| 4:Display all Doctor details	|")
print("| 5:Display all Patient details	|")
print("| 6:Display all Worker details	|")
print("| 7:Search Doctors details	|")
print("| 8:Search Patient details	|")
print("| 9:Search Worker details	|")
print("| 10:Exit	|")
print("|	|")

def Doctor_details(): #To Create Doctor's Table
cursor.execute("CREATE TABLE IF NOT EXISTS doctor_details(d_id int primary key,d_name varchar(30) NOT NULL,d_age int,d_gender varchar(10),d_department varchar(20) NOT NULL,d_post varchar(30) NOT NULL,d_phone varchar(11) unique key,d_date_of_joining date NOT NULL);")
print("::::::||||||::::::Doctor's TABLE Created Successfully:::::||||||:::::")
 
def Patient_details(): #To Create Patient's Table
cursor.execute("CREATE TABLE IF NOT EXISTS patient_details(p_id int primary key,p_name varchar(30) NOT NULL,p_age int,p_gender varchar(10),p_problems varchar(20) NOT NULL,p_phone varchar(11) NOT NULL,p_date_of_admit date NOT NULL);")
print("::::::||||||::::::Patient's TABLE Created Successfully:::::||||||:::::")


def Worker_details(): #To Create Worker's Table
cursor.execute("CREATE TABLE IF NOT EXISTS worker_details(w_id int primary key,w_name varchar(30) NOT NULL,w_age int,w_gender varchar(10),w_workname varchar(20) NOT NULL,w_phone varchar(11) NOT NULL,w_date_of_joining date NOT NULL);")
print("::::::||||||::::::Worker's TABLE Created Successfully:::::||||||:::::")


def Add_doctor(): #To Add New Doctor print("Enter New Doctor Information:") i=int(input("Enter ID of Doctor:")) n=input("Enter Doctor Name:") a=int(input("Enter Age:")) g=input("Enter Gender ( F or M):") d=input("Enter the Department:") p=input("Enter the post:") ph=input("Enter Phone Number:")
da=input("Enter date of joining(YYYY-MM-DD):")
cursor.execute("insert into doctor_details values({},'{}',{},'{}','{}','{}','{}','{}')".format(i,n,a,g,d,p,ph,da))
connect.commit() connect.close()
print(":::::|||||:::::Registered New Doctor:::::|||||:::::")


def Add_Patient(): #To Add New Patient print("Enter New Patient Information:") i=int(input("Enter ID of Patient:"))
 
n=input("Enter Patient Name:") a=int(input("Enter Age:")) g=input("Enter Gender ( F or M):") p=input("Enter Problems:") ph=input("Enter Phone Number:")
da=input("Enter the date on which patient was admitted to hospital(YYYY-MM-DD):")
cursor.execute("insert into patient_details values({},'{}',{},'{}','{}','{}','{}')".format(i,n,a,g,p,ph,da))
connect.commit() connect.close()
print(":::::|||||:::::Registered New Patient:::::|||||:::::") def Add_worker(): #To Add New Worker
print("Enter New Worker Information:") i=int(input("Enter ID of Worker: ")) n=input("Enter Worker Name:") a=int(input("Enter Age:")) g=input("Enter Gender ( F or M):") w=input("Enter type of work:") ph=input("Enter Phone Number:")
da=input("Enter date of joining(YYYY-MM-DD):")
cursor.execute("insert into worker_details values({},'{}',{},'{}','{}','{}','{}')".format(i,n,a,g,w,ph,da))
connect.commit() connect.close()
print(":::::|||||:::::Registered New Worker:::::|||||:::::")
def desc_doctor(): #To Describe Structure of Doctor Table print("Structure of doctor_details table") cursor.execute("desc doctor_details")
for i in cursor: print(i)
connect.close()
 
def desc_patient(): #To Describe Structure of Patient Table print("Structure of patient_details table") cursor.execute("desc patient_details")
for i in cursor: print(i)
connect.close()


def desc_worker(): #To Describe Structure of Worker Table print("Structure of worker_details table") cursor.execute("desc worker_details")
for i in cursor: print(i)
connect.close()


def DisplayAllDoctor(): #To Display All Doctors
print("In which order you want to display the doctor_details:") x=int(input("1:Ascending order , 2:Descending order , 3:As present in table :")) if x==1:
col=input("Enter column name with respect to which you want to order the records:") cursor.execute("select * from doctor_details order by {} asc".format(col))
for a in cursor: for j in a:
print(j,end=',') print()
connect.close() elif x==2:
col=input("Enter column name with respect to which you want to order the records:") cursor.execute("select * from doctor_details order by {} desc".format(col))
for a in cursor: for j in a:
 
print(j,end=',') print()
connect.close() else:
cursor.execute("select * from doctor_details") for a in cursor:
for j in a: print(j,end=',')
print() connect.close()

def DisplayAllPatient(): #To Display All Patient
print("In which order you want to display the patient_details:") x=int(input("1:Ascending order , 2:Descending order ,3:As present in table :")) if x==1:
col=input("Enter column name with respect to which you want to order the records:") cursor.execute("select * from patient_details order by {} asc".format(col))
for a in cursor: for j in a:
print(j,end=',') print()
connect.close() elif x==2:
col=input("Enter column name with respect to which you want to order the records:") cursor.execute("select * from patient_details order by {} desc".format(col))
for a in cursor: for j in a:
print(j,end=',') print()
connect.close()
 
else:
cursor.execute("select * from patient_details") for a in cursor:
for j in a: print(j,end=',')
print() connect.close()

def DisplayAllWorker(): #To Display All Workers
print("In which order you want to display the worker_details:") x=int(input("1:Ascending order , 2:Descending order , 3:As present in table:")) if x==1:
col=input("Enter column name with respect to which you want to order the records:") cursor.execute("select * from worker_details order by {} asc".format(col))
for a in cursor: for j in a:
print(j,end=',') print()
connect.close() elif x==2:
col=input("Enter column name with respect to which you want to order the records:") cursor.execute("select * from worker_details order by {} desc".format(col))
for a in cursor: for j in a:
print(j,end=',') print()
connect.close() else:
cursor.execute("select * from worker_details") for a in cursor:
 
for j in a: print(j,end=',')
print() connect.close()

def SearchDoctor(): #To Search Doctor
d=int(input("Enter the ID of Doctor to be searched:")) cursor.execute("select * from doctor_details where d_id={}".format(d)) x=cursor.fetchone()
if x==None:
print("No such Records of Doctor is found !!") else:
for i in x: print(i,end=",")
print() connect.close()

def SearchPatient(): #To Search Patient
d=int(input("Enter the ID of Patient to be searched:")) cursor.execute("select * from patient_details where p_id={}".format(d)) x=cursor.fetchone()
if x==None:
print("No such Patient found !!") else:
for i in x: print(i,end=",")
print() connect.close()
 
def SearchWorker(): #To Search Worker
d=int(input("Enter the ID of Worker to be searched:")) cursor.execute("select * from worker_details where w_id={}".format(d)) x=cursor.fetchone()
if x==None:
print("No such Worker found !!") else:
for i in x: print(i,end=",")
print() connect.close()

def update_doctor(): #To Update Doctor Details
d=int(input("Enter the Doctor's ID to be modified:"))
a=input("1:To change the age , 2:To change the Department , 3:To change the post , 4:To change the phone number , 5: To change All the details :")
if a=='1':
x=int(input("Enter the new age:"))
cursor.execute("update doctor_details set d_age={} where d_id={}".format(x,d)) print(":::::|||||:::::Details updated successfully:::::|||||::::::")
elif a=='2':
x=input("Enter the new Department:")
cursor.execute("update doctor_details set d_name='{}' where d_id={}".format(x,d)) print(":::::|||||:::::Details updated successfully:::::|||||::::::")
elif a=='3':
x=input("Enter the new Post:")
cursor.execute("update doctor_details set d_post='{}' where d_id={}".format(x,d)) print(":::::|||||:::::Details updated successfully:::::|||||::::::")
elif a=='4':
x=input("Enter the new phone Number:")
cursor.execute("update doctor_details set d_phone='{}' where d_id={}".format(x,d))
 
print(":::::|||||:::::Details updated successfully:::::|||||::::::") elif a=='5':
ag=int(input("Enter the age :")) p=input("Enter the new Department:") po=input("Enter the new post:") n=input("Enter the new phone number:")
cursor.execute("update doctor_details set d_age={},d_name='{}',d_post='{}',d_phone='{}' where d_id={}".format(ag,p,po,n,d))
print(":::::|||||:::::Details updated successfully:::::|||||::::::") else:
print("Invalid Option!!") return
connect.commit() connect.close()
print(“:::::|||||:::::Detail’s Updated Successfully::::|||||:::::”)


def update_worker(): #To Update Worker Details
d=int(input("Enter the Worker's ID to be modified:"))
a=input("1:To change the age , 2:To change the work name ,3:To change the phone number , 4: To change All the details :")
if a=='1':
x=int(input("Enter the new age:"))
cursor.execute("update worker_details set w_age={} where w_id={}".format(x,d)) elif a=='2':
x=input("Enter the new Work name:")
cursor.execute("update worker_details set w_name='{}' where w_id={}".format(x,d)) elif a=='3':
x=input("Enter the new Phone Number:")
cursor.execute("update worker_details set w_phone='{}' where w_id={}".format(x,d)) elif a=='4':
ag=int(input("Enter the age :"))
 
w=input("Enter the new Work name:") n=input("Enter the new phone number:")
cursor.execute("update worker_details set w_age={},w_workname='{}',w_phone='{}' where w_id={}".format(ag,w,n,d))
else:
print("Invalid Option!!") return
connect.commit() connect.close()
print(":::::|||||:::::Details updated successfully:::::|||||::::::")


def update_patient(): #To Update Patient Details
d=int(input("Enter the Patient's ID to be modified:"))
a=input("1:To change the age , 2:To change patient's problem , 3:To change the phone number , 4: To change All the details :")
if a=='1':
x=int(input("Enter the new age:"))
cursor.execute("update patient_details set p_age={} where p_id={}".format(x,d)) elif a=='2':
x=input("Enter the patient's problem:")
cursor.execute("update patient_details set p_name='{}'where p_id={}".format(x,d)) elif a=='3':
x=input("Enter the new phone Number:")
cursor.execute("update patient_details set p_phone='{}' where p_id={}".format(x,d)) elif a=='4':
ag=int(input("Enter the age :")) p=input("Enter the patient's Problem:") n=input("Enter the new phone number:")
cursor.execute("update patient_details set p_age={},p_problems='{}',p_phone='{}' where p_id={}".format(ag,p,n,d))
else:
 
print("Invalid Option!!") return
connect.commit() connect.close()
print(":::::|||||:::::Details updated successfully:::::|||||::::::")


def Bill_details(): #To Create Bill
cursor.execute("create table bill(p_id int primary key,p_name varchar(25),p_age int,drvisit varchar(40),medicines varchar(15),room int(15));")
print(":::::|||||:::::Table Created:::::|||||:::::")


def AddBill(): #To Add Bill
print("Enter Charges of patient in the bill") i=int(input("Enter ID of patient:")) n=input("Enter patient Name:") a=int(input("Enter patient age:")) d=int(input("Enter fee of Dr's visites:")) m=int(input("Enter the cost of medicines")) r=int(input("Enter Room charges:"))
cursor.execute("insert into bill values({},'{}',{},{},{},{})".format(i,n,a,d,m,r)) connect.commit()
connect.close()
print("Data inserted successfully") def ShowBill(): #To Show Bill
print("All Records of Bill") cursor.execute("Select * from bill") for i in cursor:
for j in i: print(j,end=",")
print() connect.close()
 
def delete_records(): #To Delete Records
a=int(input("1:Delete Doctor's Records , 2:Delete patient's Record , 3:Delete Worker's Recordd , 4:Delete Bill Record:"))
if a==1:
x=input("Enter the ID of doctor which you want to Remove:") cursor.execute("delete from doctor_details where d_id={}".format(x)) connect.commit()
connect.close()
print(":::::|||||::::: Record of Doctor removed successfully:::::|||||:::::") elif a==2:
x=input("Enter the ID of Patient which you want to Remove:") cursor.execute("delete from patient_details where p_id={}".format(x)) connect.commit()
connect.close()
print(":::::|||||:::::Record of Patient removed successfully:::::|||||:::::") elif a==3:
x=input("Enter the ID of worker which you want to Remove:") cursor.execute("delete from worker_details where w_id={}".format(x)) connect.commit()
connect.close()
print(":::::|||||:::::Record of Woker removed successfully:::::|||||:::::") elif a==4:
x=input("Enter the ID of patient whose bill you want to Remove:") cursor.execute("delete from bill where p_id={}".format(x)) connect.commit()
connect.close()
print(":::::|||||:::::Record removed successfully:::::|||||:::::") else:
print("Wrong choice.Enter choice correctly")
 
def RemoveAllDoctors(): #To Remove All Doctors cursor.execute("delete from doctor_details") connect.commit()
connect.close()
print("All Doctors details removed successfully")


def RemoveAllPatients(): #To Remove All Patients cursor.execute("delete from patient_details") connect.commit()
connect.close()
print("All Patients details removed successfully")


def RemoveAllWorkers(): #To Remove All Workers cursor.execute("delete from worker_details") connect.commit()
connect.close()
print("All Workers details removed successfully")


#Main Program Begins
print("\n\n\t\t|||****WELCOME TO HOSPITAL DATABASE MANAGEMENT SYSTEM****||||\n\n")
ch=int(input("Press 1: To login as ADMIN\n Press 2:To login as USER\n\n")) if ch==1:
a=input("Enter Admin Password:") if a=="Hospital@123":
print("\n\n\t| WELCOME ADMIN: Here is the Menu|\n\n") while True:
print("\n") AdminMenu() print("\n")
n=int(input("Enter Your Choice:"))
 
if n==1:
Doctor_details() elif n==2:
desc_doctor() elif n==3:
Add_doctor() elif n==4:
DisplayAllDoctor() elif n==5:
Patient_details() elif n==6:
desc_patient() elif n==7:
Add_Patient() elif n==8:
DisplayAllPatient() elif n==9:
Worker_details() elif n==10:
desc_worker() elif n==11:
Add_worker() elif n==12:
DisplayAllWorker() elif n==13 or n==26:
SearchDoctor() elif n==14 or n==27:
SearchPatient() elif n==15 or n==28:
SearchWorker()
 
elif n==16: update_doctor()
elif n==17: update_patient()
elif n==18: update_worker()
elif n==19: Bill_details()
elif n==20: AddBill()
elif n==21: ShowBill()
elif n==22: delete_records()
elif n==23: RemoveAllDoctors()
elif n==24: RemoveAllPatients()
elif n==25: RemoveAllWorkers()
elif n==29: break
else:
print("WRONG CHOICE")
else:
print("Invalid password !! LOGIN UNSUCCESSFUL") elif ch==2:
nm=input("Enter Username:")
print("\n\n\t\t| WELCOME ",nm,":HERE IS THE MENU |\n\n") while True:
 print("\n") UserMenu() print("\n")
n=int(input("Enter your choice:")) if n==1 or n==7:
SearchDoctor() elif n==2 or n==8: SearchPatient() elif n==3 or n==9: SearchWorker()
elif n==4: DisplayAllDoctor()
elif n==5: DisplayAllPatient()
elif n==6: DisplayAllWorker()
elif n==10: break
else:
print("WRONG CHOICE")
else:
print("Invalid Choice!!")

 
