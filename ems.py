from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import requests

root = Tk()
root.title("Employee Management System")
root.geometry("800x800+400+10")
root.configure(bg="lightsteelblue")
f = ("Times New Roman",30,"bold")
n = "navyblue"
l = "lightblue"
b = "skyblue"

def clsloc():
	labloc.configure(text="")

def clstemp():
	labtemp.configure(text="")

def f1():
	add.deiconify()
	root.withdraw()
	clsloc()
	clstemp()

def f2():
	entaid.delete(0,END)
	entaname.delete(0,END)
	entasal.delete(0,END)
	root.deiconify()
	add.withdraw()
	clsloc()
	clstemp()

def f3():
	view.deiconify()
	root.withdraw()
	scrdata.delete(1.0,END)
	clsloc()
	clstemp()
	con = None
	try:
		con = connect("employee.db")
		cursor = con.cursor()
		sql = "SELECT * FROM employee"
		cursor.execute(sql)
		data = cursor.fetchall()
		if not data:
			showinfo("No data","No employee data found.")
			return
		info = ""
		for d in data:
			info += f"Id: {d[0]} \tName: {d[1]}   \tSalary: {d[2]}\n"
 
		scrdata.insert(INSERT,info)
	except Exception as e:
		showerror("ISSUE!!",e)
	if con is not None:
		con.close()
		

def f4():
	root.deiconify()
	view.withdraw()
	clsloc()
	clstemp()

def f5():
	update.deiconify()
	root.withdraw()
	clsloc()
	clstemp()

def f6():
	entuid.delete(0,END)
	entuname.delete(0,END)
	entusal.delete(0,END)
	root.deiconify()
	update.withdraw()
	clsloc()
	clstemp()

def f7():
	delete.deiconify()
	root.withdraw()
	clsloc()
	clstemp()

def f8():
	entdid.delete(0,END)
	root.deiconify()
	delete.withdraw()
	clsloc()
	clstemp()

def validateid(id):
	if not id:
		return"Please Enter Employee id."
	try:
		id=int(id)
		if id <=0:
			return"Employee id must positive integer."
	except ValueError:
		return"It must be numeric values."


def validatename(name):
	if not name:
		return "Please enter employee name."
	elif name.isspace():
		return "Name should not be spaces"
	elif not name.isalpha():
		return "Invalid Name. It must contain only Alphabetical characters"
	elif len(name) < 2 or len(name) >50:
		return "Invalid! Name should be between 2 to 50 characters"
	return None


def validatesalary(salary):
	if not salary:
		return"Please enter salary."
	try:
		salary = float(salary)
		if salary<=0:
			return "Salary cannot be negative."
	except ValueError:
		return "Invalid Salary. It must be a numeric value."
	return None

def location():
	try:
		url = "https://ipinfo.io" 
		resquests = requests.get(url)
		if resquests.status_code == 200:
			data = resquests.json()
			loc = data.get('city')
			region = data.get('region')
			msg = loc+","+region
		labloc.configure(text=msg)
	except Exception as e:
		showerror("Error", f"Failed to fetch location: {e}")

def temp():
	try:
		api_key ="13a389e6a7777f4e06f7e81b9d4d8373"
		city = "Mumbai"
		url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
		response = requests.get(url)
		data = response.json()
		print(data)
		temperature = data['main']['temp']
		labtemp.configure(text=f"{temperature}°C")

	except Exception as e:
		showerror("ERROR",f"failed to fetch temperature:{e}")

def addemp():
	entaid.focus()
	con = None
	try:
		con = connect("employee.db")
		cursor = con.cursor()
		
		enteredid = entaid.get()
		cursor.execute("SELECT ID FROM employee WHERE id=?",(enteredid,))
		if cursor.fetchone():
			showerror("ERROR!!","Employee ID already exists.")
			entaid.delete(0,END)
			entaid.focus()
			return

		sql ="INSERT INTO employee VALUES(?,?,?)"

		id = entaid.get()
		result = validateid(id)
		if result:
			showerror("ERROR!!",result)
			entaid.delete(0,END)
			entaid.focus()
			return
		id = int(entaid.get())
		
		name = entaname.get()
		result = validatename(name)
		if result:
			showerror("ERROR!!",result)
			entaname.delete(0,END)
			entaname.focus()
			return

		salary = entasal.get()
		result = validatesalary(salary)
		if result:
			showerror("ERROR!!",result)
			entasal.delete(0,END)
			entasal.focus()
			return
		salary = float(salary)
		
		cursor.execute(sql,(id,name,salary))
		con.commit()
		showinfo("Successful","Employee details added successfully.")
		entaid.delete(0,END)
		entaname.delete(0,END)
		entasal.delete(0,END)
		entaid.focus()

	except Exception as e:
		con.rollback()
		showerror("ERROR!!",e)
	finally:
		if con is not None:
			con.close()			

def updateemp():
	entuid.focus()
	con = None
	try:
		con = connect("employee.db")
		cursor = con.cursor()
		id = entuid.get()
		result = validateid(id)
		if result:
			showerror("ERROR!!",result)
			entuid.delete(0,END)
			entuid.focus()
			return
		id = int(id)
		
		cursor.execute("SELECT ID FROM employee WHERE id=?",(id,))
		if not cursor.fetchone():
			showerror("ERROR!!",f"Employee ID: {id} cannot be found.")
			entuid.delete(0,END)
			entuid.focus()
			return
		sql = "UPDATE employee SET name=?,salary=? WHERE id=?"
		name = entuname.get()
		result = validatename(name)
		if result:
			showerror("ERROR!!",result)
			entuname.delete(0,END)
			entuname.focus()
			return

		salary = entusal.get()
		result = validatesalary(salary)
		if result:
			showerror("ERROR!!",result)
			entusal.delete(0,END)
			entusal.focus()
			return
		salary = float(salary)

		cursor.execute(sql,(name,salary,id))
		con.commit()
		showinfo("Successful","Employee detail updated successfully.")
		entuid.delete(0,END)
		entuname.delete(0,END)
		entusal.delete(0,END)
		entuid.focus()
		
	except Exception as e:
		con.rollback()
		showerror("ISSUE!!",e)
	finally:
		if con is not None:
			con.close()


def deleteemp():
	entdid.focus()
	con = None
	try:
		con = connect("employee.db")
		cursor = con.cursor()
		id = entdid.get()
		result = validateid(id)
		if result:
			showerror("ERROR!!",result)
			entdid.delete(0,END)
			entdid.focus()
			return
		id = int(id)
		
		cursor.execute("SELECT ID FROM employee WHERE id=?",(id,))
		if not cursor.fetchone():
			showerror("ERROR!!",f"Employee ID: {id} cannot be found.")
			entdid.delete(0,END)
			entdid.focus()
			return
		sql = "DELETE FROM employee WHERE id=?"
		cursor.execute(sql,(id,))
		con.commit()
		showinfo("Successfully","Employee Deleted successfully.")
		entdid.delete(0,END)
		entdid.focus()
	except Exception as e:
		showerror("ERROR!!",str(e))
	finally:
		if con is not None:
			con.close()

def chartemp():
    con = None
    try:
        con = connect("employee.db")
        cursor = con.cursor()
        cursor.execute("SELECT Name, Salary FROM employee ORDER BY Salary DESC LIMIT 5")
        data = cursor.fetchall()
        
        if data:
            names = [entry[0] for entry in data]
            salaries = [entry[1] for entry in data]
            
            plt.clf()
            fig, ax = plt.subplots()
            ax.bar(names, salaries, color='skyblue')
            ax.set_xlabel("Employee Names")
            ax.set_ylabel("Salaries")
            ax.set_title("Top 5 Employees by Salary")
            ax.grid(True)
            
            if 'chart_window' not in globals():
                global chart_window
                chart_window = Toplevel(root)
                chart_window.title("Employee Salaries Chart")
                chart_window.geometry("800x600+400+100")
                chart_window.configure(bg="lightsteelblue")
            
            for widget in chart_window.winfo_children():
                widget.destroy()

            canvas = FigureCanvasTkAgg(fig, master=chart_window)
            canvas.draw()
            canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)
            
            Button(chart_window, text="Close", font=f, bg=b, fg=n, command=chart_window.withdraw).pack(side=BOTTOM, pady=10)

            chart_window.deiconify()
            chart_window.lift()
        else:
            showinfo("No Data", "No employee data found.")
    except Exception as e:
        showerror("Error", f"Failed to generate chart: {e}")
    finally:
        if con is not None:
            con.close()


def exit():
	answer = askyesno("Exit Confirmation","Are you sure you want to exit?")
	if answer:
		root.destroy()


labtitle = Label(root,text="Employee Management System",bg="deepskyblue",font=f)
labtitle.place(x=130,y=20)

btnadd = Button(root,text="Add Employee",font=f,bg = b,fg=n,command=f1)
btnadd.place(x=250,y=100)
btnview = Button(root,text="View Employee",font=f,bg=b,fg=n,command=f3)
btnview.place(x=245,y=200)
btnupdate = Button(root,text="Update Employee",font=f,bg=b,fg=n,command=f5)
btnupdate.place(x=240,y=300) 
btndel = Button(root,text="Delete Employee",font=f,bg=b,fg=n,command=f7)
btndel.place(x=240,y=400)
btnchart = Button(root,text="Chart",font=f,bg=b,fg=n,command=chartemp)
btnchart.place(x=300,y=500)

btnloc = Button(root,text="Location",font=f,bg=b,fg=n,command=location)
btnloc.place(x=50,y=600)
labloc = Label(root,width=22,font=f,bg="White")
labloc.place(x=250,y=620)

btntemp = Button(root,text="Temperature",font=f,fg=n,bg=b,command=temp)
btntemp.place(x=150,y=700)
labtemp = Label(root,width=9,font=f,bg="white")
labtemp.place(x=430,y=720)

add = Toplevel(root)
add.title("Add Employee")
add.geometry("800x800+400+10")
add.configure(bg="lightsteelblue")

labtitle = Label(add,text="Add Employee",font=f,bg="deepskyblue")
labtitle.place(x=260,y=30)

labaid = Label(add,text="Employee Id :",font=f,bg=l,fg=n)
labaid.place(x=100,y=150)
entaid = Entry(add,font=f,width=15)
entaid.place(x=390,y=150)

labaname = Label(add,text="Name :",font=f,bg=l,fg=n)
labaname.place(x=100,y=250)
entaname = Entry(add,font=f,width=15)
entaname.place(x=390,y=250)

labasal = Label(add,text="Salary :",font=f,bg=l,fg=n)
labasal.place(x=100,y=350)
entasal = Entry(add,font=f,width=15)
entasal.place(x=390,y=350)

btnsave = Button(add,text="Save",font=f,bg=b,fg=n,command=addemp)
btnsave.place(x=300,y=450)
btnback = Button(add,text="Back",font=f,bg=b,fg=n,command=f2)
btnback.place(x=300,y=550)

view = Toplevel(root)
view.title("View Employee")
view.geometry("800x800+400+10")
view.configure(bg="lightsteelblue")

labview = Label(view,text="Employee info",bg="deepskyblue",fg=n,font=f)
labview.place(x=280,y=20)

scrdata = ScrolledText(view,width=40,height=14,font=("century",24,"bold"))
scrdata.place(x=10,y=80)
btnback = Button(view,text="Back",font=f,bg=b,fg=n,command=f4)
btnback.place(x=330,y=650)

update = Toplevel(root)
update.title("Update Employee")
update.geometry("800x800+400+10")
update.configure(bg="lightsteelblue")

labtitle = Label(update,text="Update Employee",font=f,bg="deepskyblue")
labtitle.place(x=260,y=30)

labuid = Label(update,text="Employee Id :",font=f,bg=l,fg=n)
labuid.place(x=100,y=150)
entuid = Entry(update,font=f,width=15)
entuid.place(x=390,y=150)

labuname = Label(update,text="Name :",font=f,bg=l,fg=n)
labuname.place(x=100,y=250)
entuname = Entry(update,font=f,width=15)
entuname.place(x=390,y=250)

labusal = Label(update,text="Salary :",font=f,bg=l,fg=n)
labusal.place(x=100,y=350)
entusal = Entry(update,font=f,width=15)
entusal.place(x=390,y=350)

btnupdate = Button(update,text="Update",font=f,bg=b,fg=n,command=updateemp)
btnupdate.place(x=290,y=450)
btnback = Button(update,text="Back",font=f,bg=b,fg=n,command=f6)
btnback.place(x=300,y=550)

delete = Toplevel(root)
delete.title("Delete Employee")
delete.configure(bg="lightsteelblue")
delete.geometry("800x800+400+10")

labtitle = Label(delete,text="Delete Employee",font=f,bg="deepskyblue")
labtitle.place(x=260,y=50)

labdid = Label(delete,text="Employee Id :",font=f,bg=l,fg=n)
labdid.place(x=100,y=150)
entdid = Entry(delete,font=f,width=15)
entdid.place(x=390,y=150)

btndelete = Button(delete,text="Delete",font=f,bg=b,fg=n,command=deleteemp)
btndelete.place(x=190,y=300)
btnback = Button(delete,text="Back",font=f,bg=b,fg=n,command=f8)
btnback.place(x=400,y=300)


root.protocol("WM_DELETE_WINDOW",exit)

root.mainloop()