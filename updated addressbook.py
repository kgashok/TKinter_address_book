import pymysql
from tkinter import *
from tkinter import messagebox
#search



def search():
    try:
        con=pymysql.connect(user='root',password='',host='localhost',database='cb')
        cur=con.cursor()
        sql="select * from names where rollno=%s"%rollno.get()
        cur.execute(sql)
        result=cur.fetchone()
        name.set(result[1])
        age.set(result[2])
        department.set(result[3])
        college.set(result[4])
        address.set(result[5])
        city.set(result[6])
        state.set(result[7])
        country.set(result[8])
        phone_number.set(result[9])
        alternative_phone_number.set(result[10])
        email_ID.set(result[11])
        e1.configure(state='disabled')
        con.close()
    except:
        messagebox.showinfo('No Data','No such data available....')
        clear()
def clear():
    rollno.set('')
    name.set('')
    age.set('')
    department.set('')
    college.set('')
    address.set('')
    city.set('')
    state.set('')
    country.set('')
    phone_number.set('')
    alternative_phone_number.set('')
    email_ID.set('')
    e1.configure(state='normal')
def add():
    try:
        con=pymysql.connect(user='root',password='',host='localhost',database='cb')
        cur=con.cursor()
        sql="insert into names values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(rollno.get(),name.get(),age.get(),department.get(),college.get(),address.get(),city.get(),state.get(),country.get(),phone_number.get(),alternative_phone_number.get(),email_ID.get())
        cur.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo('Sucess','Record saved')
    except:
        messagebox.showinfo('Error','Error in data entry')
    finally:
        clear()
def update():
    try:
        con=pymysql.connect(user='root',password='',host='localhost',database='cb')
        cur=con.cursor()
        sql="update names set name='%s',age='%s',department='%s',college='%s',address='%s',city='%s',state='%s',country='%s',phone_number='%s',alternative_phone_number='%s',email_ID='%s' where rollno='%s'" %(name.get(),age.get(),department.get(),college.get(),address.get(),city.get(),state.get(),country.get(),phone_number.get(),alternative_phone_number.get(),email_ID.get(),rollno.get())
        cur.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo('Sucess','Record updated')
    except:
        messagebox.showinfo('Error','Error occurs')
    finally:
        clear()
def delete():
    try:
        con=pymysql.connect(user='root',password='',host='localhost',database='cb')
        cur=con.cursor()
        sql="delete from names where rollno='%s'" %(rollno.get())
        cur.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo('Sucess','Record deleted')
    except:
        messagebox.showinfo('Error','Error occurs')
    finally:
        clear()
w1=Tk()
w1.title('My app')
w1.geometry('500x400')
ptitle=Label(w1, text='''                 Program to add ,delete and modify the records from the studends table''')
ptitle.grid(row=0,column=0,columnspan=2)
rollno=IntVar()
name=StringVar()
age=StringVar()
department=StringVar()
college=StringVar()
address=StringVar()
city=StringVar()
state=StringVar()
country=StringVar()
phone_number=IntVar()
alternative_phone_number=IntVar()
email_ID=StringVar()
l1=Label(w1,text=' RollNo ')
e1=Entry(w1,textvariable=rollno)
l2=Label(w1,text=' Name ')
e2=Entry(w1,textvariable=name) 
l3=Label(w1,text=' Age ')
e3=Entry(w1,textvariable=age)
l4=Label(w1,text=' department ')
e4=Entry(w1,textvariable=department)
l5=Label(w1,text=' college ')
e5=Entry(w1,textvariable=college)
l6=Label(w1,text=' address ')
e6=Entry(w1,textvariable=address)
l7=Label(w1,text=' city ')
e7=Entry(w1,textvariable=city)
l8=Label(w1,text=' state ')
e8=Entry(w1,textvariable=state)
l9=Label(w1,text=' country ')
e9=Entry(w1,textvariable=country)
l10=Label(w1,text=' phone_number ')
e10=Entry(w1,textvariable=phone_number)
l11=Label(w1,text=' alternative_phone_number ')
e11=Entry(w1,textvariable=alternative_phone_number)
l12=Label(w1,text=' email_ID ')
e12=Entry(w1,textvariable=email_ID)
b1=Button(w1,text=' Search ',command=search)
b2=Button(w1,text=' Add ',command=add)
b3=Button(w1,text=' Update ',command=update)
b4=Button(w1,text=' Delete ',command=delete)
b5=Button(w1,text=' Clear ',command=clear)
l1.grid(row=1,column=0)
e1.grid(row=1,column=1)
b1.grid(row=1,column=2)

l2.grid(row=2,column=0)
e2.grid(row=2,column=1)
l3.grid(row=3,column=0)
e3.grid(row=3,column=1)
l4.grid(row=4,column=0)
e4.grid(row=4,column=1)
l5.grid(row=5,column=0)
e5.grid(row=5,column=1)
l6.grid(row=6,column=0)
e6.grid(row=6,column=1)
l7.grid(row=7,column=0)
e7.grid(row=7,column=1)
l8.grid(row=8,column=0)
e8.grid(row=8,column=1)
l9.grid(row=9,column=0)
e9.grid(row=9,column=1)
l10.grid(row=10,column=0)
e10.grid(row=10,column=1)
l11.grid(row=11,column=0)
e11.grid(row=11,column=1)
l12.grid(row=12,column=0)
e12.grid(row=12,column=1)
b2.grid(row=13,column=0)
b3.grid(row=13,column=1)
b4.grid(row=14,column=0)
b5.grid(row=14,column=1)
w1.mainloop()























