from tkinter import *
from tkinter.messagebox import *
import re
from tkinter.scrolledtext import *
from tkinter import simpledialog
from sqlite3 import *
from datetime import datetime
from tkcalendar import DateEntry


root = Tk()
root.title(" Reservation Management System")
root.geometry("900x770+50+50")
root.configure(bg="lightsteelblue")
f=("Times New Roman",30,"bold")
n = "navy"
l = "lightsteelblue"
labtitle = Label(root,text="Reservation Management System",font=f,bg="deepskyblue")
labtitle.place(x=150,y=20)

def f1():
	admin.deiconify()
	root.withdraw()
	
def f2():
	root.deiconify()
	admin.withdraw()

def login():
	entuser.focus()
	username = "admin"
	password = "admin123"
	if entuser.get() == username and entpassword.get() == password:
		showinfo("Login Success","You successfully logged in.")
		view.deiconify()
		admin.withdraw()
		showreservation()
		entuser.delete(0,END)
		entpassword.delete(0,END)
	else:
		showerror("ERROR","Invalid login.")
		entuser.delete(0,END)
		entpassword.delete(0,END)

def exit():
	answer = askyesno("Exit Confirmation","Are you sure you want to exit?")
	if answer:
		root.destroy()	

def showreservation():
	advdata.delete(1.0,END)
	con = None
	try:
		con = connect("reservations.db")
		cursor = con.cursor()
		sql = "SELECT * FROM reservations"
		cursor.execute(sql)
		data = cursor.fetchall()
		info = ""
		for d in data:
			info += f"Name: {d[0]} \tPhone: {int(d[1])} \tDestination: {d[2]} \nDate of travel: {d[3]} \tAirline: {d[4]}\n\n"
		
		advdata.insert("end",info)
	
	except Exception as e:
		showerror("ISSUE",e)
	finally:
		if con is not None:
			con.close()
def f4():
	admin.deiconify()
	view.withdraw()



def validatename(name):
	if not name:
		return "Please enter name."
	elif name.isspace():
		return "Name should not be spaces"
	elif not name.isalpha():
		return "Invalid Name. It must contain only Alphabetical characters"
	elif len(name) < 2 or len(name) >50:
		return "Invalid! Name should be between 2 to 50 characters"
	return None


def validatephone(phone):
	try:
		if not phone.isdigit():
			return "It must contain only numbers only."
			
		if 0 < len(phone)< 10 and len(phone)!=10:
			return"Phone number should be 10 digits."
	except ValueError:
		return"Invalid phone number. It must contain only digits."



def validatedestination(destination):
	if not destination:
		return "Please enter destination"
	elif not destination.replace(" ", "").isalpha():
		return "Destination cannot contain special characters or numbers."
	elif destination.isdigit():
		return "Destination cannot be numerical value."


def validatedate(date):
	date_pattern = re.compile(r'^\d{2}-\d{2}-\d{4}$')
	if not date_pattern.match(date):
		return "Invalid date format. Please use DD-MM-YYYY format."

def validatechoice(airline_choice):
	if airline == 0:
		showerror("ERROR","Please select an airline")
		return False
	return True

def submit():
	con = None
	try:
		con = connect("reservations.db")
		cursor = con.cursor()
		sql = "insert into reservations values(?,?,?,?,?)"
		
		name = entname.get()
		validation_result = validatename(name)
		if validation_result:
			showerror("ERROR",validation_result)
			entname.delete(0,END)
			entname.focus()
			return

		phone = entphone.get()
		validation_result = validatephone(phone)
		if validation_result:
			showerror("ERROR",validation_result)
			entphone.delete(0,END)
			entphone.focus()
			return
	
		destination = entdestination.get()
		validation_result = validatedestination(destination)
		if validation_result:
			showerror("ERROR",validation_result)
			entdestination.delete(0,END)
			entdestination.focus()
			return

		date = entdate.get()
		validation_result = validatedate(date)
		if validation_result:
			showerror("ERROR",validate_result)
			entdate.delete(0,END)
			entdate.focus()

		airline_choice = airline.get()
		validate_result = validatechoice(airline_choice)
		if validation_result:
			return
		else:
			airlinechoice = {1: "Indigo", 2: "Vistara", 3: "Akasa", 4: "Deccan", 5: "Spicejet"}[airline_choice]
		
		
		cursor.execute(sql, (name, phone, destination, date, airlinechoice))
		con.commit()
		showinfo("Successful","Reservation done successfully")
		entname.delete(0,END)
		entphone.delete(0,END)
		entdestination.delete(0,END)
		entdate.delete(0,END)
		airline.set(0)
		entname.focus()	

	except Exception as e:
		con.rollback()
		showerror("ISSUE",e)
	finally:
		if con is not None:
			con.close()


def delete():
	con = None
	try:
		con = connect("reservations.db")
		cursor = con.cursor()
		phone = simpledialog.askinteger("Input","Enter phone number to delete:")
		if phone:
			confirmation = askyesno("Confirm Deletion",f"Are you sure you want cancel the reservation?")
			if confirmation:
				sql = "delete from reservations where phone = '%s' " % phone
				cursor.execute(sql)
				con.commit()
				showinfo("Successful","Reservation cancelled successfully.")
				showreservation()
			else:
				showinfo("Cancelled","Deletion cancelled.")
		else:
			showwarning("No Input","Phone Number cannot be empty")
	except Exception as e:
		showerror("Issue",e)
	finally:
		if con is not None:
			con.close()


labname = Label(root,text="Name :",font=f,bg=l,fg=n)
labname.place(x=130,y=100)
entname = Entry(root,font=f,width=20)
entname.place(x=270,y=100)

labphone = Label(root,text="Phone No. :",font=f,bg=l,fg=n)
labphone.place(x=60,y=170)
entphone = Entry(root,font=f,width=20)
entphone.place(x=270,y=170)

labdestination = Label(root,text="Destination :",font=f,bg=l,fg=n)
labdestination.place(x=40,y=240)
entdestination = Entry(root,font=f,width=20)
entdestination.place(x=270,y=240)

labdate = Label(root,text="Date of Travel :",font=f,bg=l,fg=n)
labdate.place(x=40,y=310)
entdate = DateEntry(root, font=f, width=15, date_pattern="dd-mm-yyyy")
entdate.place(x=320,y=310)

labselect = Label(root,text="Select Airline:",font=f,bg=l,fg=n)
labselect.place(x=50,y=365)
airline = IntVar()
airline.set(0)

rbind = Radiobutton(root,text="Indigo",font=f,bg=l,fg=n,variable=airline,value=1)
rbind.place(x=300,y=390)
rbvis = Radiobutton(root,text="Vistara",font=f,bg=l,fg=n,variable=airline,value=2)
rbvis.place(x=300,y=450)
rbaka = Radiobutton(root,text="Akasa",font=f,bg=l,fg=n,variable=airline,value=3)
rbaka.place(x=300,y=500)
rbdec = Radiobutton(root,text="Deccan",font=f,bg=l,fg=n,variable=airline,value=4)
rbdec.place(x=300,y=550)
rbspi = Radiobutton(root,text="Spicejet",font=f,bg=l,fg=n,variable=airline,value=5)
rbspi.place(x=300,y=600)

btnsubmit = Button(root,text="Submit",font=f,bg="Skyblue",command=submit)
btnsubmit.place(x=200,y=670)

btnadmin = Button(root, text="Admin Login", font=f, bg="skyblue", command=f1)
btnadmin.place(x=450, y=670)



admin = Toplevel(root)
admin.title("Admin login")
admin.geometry("900x770+50+50")
admin.configure(bg="lightsteelblue")

labuser = Label(admin,text="Username :",font=f,bg=l)
labuser.place(x=200,y=200)
entuser = Entry(admin,font=f,width=15)
entuser.place(x=400,y=200)

labpassword = Label(admin,text="Password :",font=f,bg=l)
labpassword.place(x=200,y=300)
entpassword = Entry(admin,font=f,width=15,show="*")
entpassword.place(x=400,y=300)

btnlogin = Button(admin,text="Login",font=f,bg="skyblue",command=login)
btnlogin.place(x=340,y=400)
btnback = Button(admin,text="Back",font=f,bg="skyblue",command=f2)
btnback.place(x=340,y=500)

view = Toplevel(admin)
view.title("Reservations")
view.geometry("900x770+50+50")
view.configure(bg="lightsteelblue")
s=("Times New Roman",24,"bold")
f=("Times New Roman",30,"bold")

advdata = ScrolledText(view,width=52,height=13,font=s)
advdata.place(x=20,y=30)
advback = Button(view,text="Back",font=f,width=10,bg="skyblue",command=f4)
advback.place(x=200,y=650)
advdelete = Button(view,text="Delete",font=f,width=10,bg="skyblue",command=delete)
advdelete.place(x=500,y=650)

root.protocol("WM_DELETE_WINDOW",exit)
root.mainloop()
