from tkinter import *
from tkinter import ttk
import mysql.connector as sql

conn=sql.connect(host="localhost", user="root", passwd="jaisairam")

c1= conn.cursor()
c1.execute('create database if not exists food')

conn=sql.connect(host="localhost", user="root", passwd="jaisairam",database="food")
c1= conn.cursor()
c1.execute('create table if not exists myc(cust_name varchar(30),account_no varchar(50) primary key,v_address varchar(30),v_password varchar(30))')
c1.execute('create table if not exists sales(f_name varchar(30),address varchar(100))')


def ac_details():
    global details2

    details2=Tk()
    details2.geometry("900x200")
    
    details2.title("ACCOUNT DETAILS")

    tv1=ttk.Treeview(details2,columns=(1,2,3,4),show="headings",height="5")
    tv1.pack()
    tv1.heading(1,text="COSTUMER NAME")
    tv1.heading(2,text="ACCOUNT NO.")
    tv1.heading(3,text="COSTUMER ADDRESS")
    tv1.heading(4,text="COSTUMER PASSWORD")
    
    
    conn2=sql.connect(host="localhost", user="root", passwd="jaisairam", database="food")
    mycursor2=conn2.cursor()
    mycursor2.execute("select * from myc where cust_name='"+str(a)+"' and account_no='"+str(b)+"' and v_address='"+str(c)+"' and v_password='"+str(d)+"'")
    rows2=mycursor2.fetchall()
    for i in rows2:
        tv1.insert('','end',values=i)
    

def put():

    global a
    global b
    global c
    global d
    
    a=username_entry.get()
    b=account_entry.get()
    c=address_entry.get()
    d=password_entry.get()

    
    
    conn=sql.connect(host="localhost", user="root", passwd="jaisairam", database="food")
    mycursor=conn.cursor()

    global i
    
    mycursor.execute("select account_no from myc")
    g=mycursor.fetchall()
    for i in g:
        
        if (b in i):
            Label(account,text="PLEASE ENTER DIFFERENT ACCOUNT NUMBER",font=("arial",10,"bold"),bg="yellow").pack()
    
    mycursor.execute("insert into myc values('%s','%s','%s','%s')"%(a,b,c,d))
        
    mycursor.close()
    conn.commit()
    conn.close()
    Label(account,text="ACCOUNT CREATED",font=("arial",10,"bold"),bg="yellow").pack()
    Label(account,text="",bg="yellow").pack()
    Button(account,text="CLICK HERE TO SEE ACCOUNT DETAILS",font=("monotype corsiva",10,"bold"),command=ac_details,fg="yellow",bg="purple").pack()
    Button(account,text="CLICK HERE TO GO BACK TO MAIN WINDOW",font=("monotype corsiva",10,"bold"),command=account.destroy,fg="yellow",bg="purple").pack()
    username_entry.delete(0,END)
    account_entry.delete(0,END)
    address_entry.delete(0,END)
    password_entry.delete(0,END)
    
def create_account():
    global account
    account=Tk()
    account.geometry("400x400")
    account.configure(bg="yellow")
    account.title("CREATE YOUR ACCOUNT HERE")
    
    username=StringVar()
    account_no=StringVar()
    address=StringVar()
    password=StringVar()
    global username_entry
    global account_entry
    global address_entry
    global password_entry
    
    l1=Label(account,text="ENTER CUSTOMER NAME",font=("arial",10,"bold"),bg="yellow").pack()
    username_entry=Entry(account,textvariable=username)
    username_entry.pack()
    Label(account,text="",bg="yellow").pack()
    
    l2=Label(account,text="Enter Account no",font=("arial",10,"bold"),bg="yellow").pack()
    account_entry=Entry(account,textvariable=account_no)
    account_entry.pack()
    Label(account,text="",bg="yellow").pack()

    l3=Label(account,text="Enter Address",font=("arial",10,"bold"),bg="yellow").pack()
    address_entry=Entry(account,textvariable=address)
    address_entry.pack()
    Label(account,text="",bg="yellow").pack()

    l4=Label(account,text="Enter Password",font=("arial",10,"bold"),bg="yellow").pack()
    password_entry=Entry(account,textvariable=password,show='*')
    password_entry.pack()
    Label(account,text="",bg="yellow").pack()

    Button(account,text="SUBMIT",font=("monotype corsiva",10,"bold"),command=put,fg="yellow",bg="purple").pack()
    
    
def food_details():
    global details

    details=Tk()
    details.geometry("700x200")
    
    details.title("FOOD DETAILS")

    tv=ttk.Treeview(details,columns=(1,2),show="headings",height="5")
    tv.pack()
    tv.heading(1,text="FOOD NAME")
    tv.heading(2,text="COSTUMER ADDRESS")
    x=(u,j)
    conn1=sql.connect(host="localhost", user="root", passwd="jaisairam", database="food")
    mycursor1=conn1.cursor()
    mycursor1.execute("select * from sales where f_name = '"+str(u)+"' and address = '"+str(j)+"' ")
    rows=mycursor1.fetchall()
    for i in rows:
        tv.insert('','end',values=i)
   
def rate():
    Label(order,text="THANK YOU FOR RATING US,'"+str(rate1.get())+"'",bg="yellow").pack()
    

    


    
def food():

    global u
    global j
    u=food_name.get()
    j=food_address.get()


    conn=sql.connect(host="localhost", user="root", passwd="jaisairam", database="food")
    mycursor=conn.cursor()
    mycursor.execute("insert into sales values('%s','%s')"%(u,j))

    mycursor.close()
    conn.commit()
    conn.close()
    Label(order,text="",bg="yellow").pack()
    Label(order,text="FOOD ORDERED!!!!",bg="yellow",font=("monotype corsiva",20,"italic")).pack()
    Label(order,text="",bg="yellow").pack()
    Button(order,text="CLICK HERE TO SEE DETAILS OF YOUR FOOD",font=("monotype corsiva",10,"bold"),command=food_details,fg="yellow",bg="purple").pack()
    Label(order,text="",bg="yellow").pack()
    Button(order,text="CLICK HERE TO GO BACK TO MAIN SCREEN",font=("monotype corsiva",10,"bold"),command=order.destroy,fg="yellow",bg="purple").pack()
    Label(order,text="",bg="yellow").pack()

    global rate1
    Label(order,text="DON'T FORGET TO RATE OUR SERVICES",bg="yellow").pack()
    rate1=Scale(order, from_=1, to=5, orient=HORIZONTAL,bg="green")
    rate1.pack()
    Button(order,text="RATE US",command=rate,font=("monotype corsiva",10,"bold"),fg="yellow",bg="purple").pack()
    
    
    food_name.delete(0,END)
    food_address.delete(0,END)

def order_food():
    global order
    order=Tk()
    order.geometry("600x600")
    order.configure(bg="yellow")
    order.title("ORDER YOUR FOOD HERE")

    global food_name
    global food_address
    
    food_info=StringVar()
    cost=StringVar()
    add=StringVar()
    
    Label(order,text="ENTER FOOD NAME",bg="yellow").pack()
    food_name=Entry(order,textvariable=food_info)
    food_name.pack()
    Label(order,text="",bg="yellow").pack()

    
    
    Label(order,text="ENTER YOUR ADDRESS",bg="yellow").pack()
    food_address=Entry(order,textvariable=add)
    food_address.pack()
    Label(order,text="",bg="yellow").pack()

    Button(order,text="ORDER FOOD",font=("monotype corsiva",10,"bold"),command=food,fg="yellow",bg="purple").pack()
    login.destroy()


def check():
    
    passw=password_login.get()
    global acc
    acc=account_login.get()

    conn=sql.connect(host="localhost", user="root", passwd="jaisairam", database="food")
    mycursor=conn.cursor()
    global row
    mycursor.execute("select * from myc where account_no='"+str(acc)+"'")
    data=mycursor.fetchall()
    
    for row in data:
        

        if (passw in row and acc in row):
                
                
            Label(login,text="LOGIN SUCCESSFULL!!!",font=("arial",15),fg="black",bg="green").pack()
            Label(login,text="",bg="yellow").pack()
            Button(login,text="CLICK HERE TO ORDER FOOD",fg="yellow",bg="purple",command=order_food).pack()
            Button(login,text="CLICK HERE TO GO BACK TO MAIN WINDOW",font=("monotype corsiva",10,"bold"),command=login.destroy,fg="yellow",bg="purple").pack()
    

    
    account_login.delete(0,END)
    
    password_login.delete(0,END)


def login_window():
    global login
    login=Tk()
    login.geometry("300x300")
    login.configure(bg="MistyRose3")
    login.title("LOGIN HERE")

    

    '''global username_login'''
    global password_login
    global account_login
    
    username_verify=StringVar()
    password_verify=StringVar()
    account_verify=StringVar()

    

    Label(login,text="ENTER YOUR ACCOUNT NO.",font=("arial",10,"bold"),bg="MistyRose4").pack()
    account_login=Entry(login,textvariable=account_verify)
    account_login.pack()
    Label(login,text="",bg="MistyRose3").pack()

    Label(login,text="ENTER PASSWORD",font=("arial",10,"bold"),bg="MistyRose4").pack()
    password_login=Entry(login,textvariable=password_verify,show="*")
    password_login.pack()
    Label(login,text="",bg="MistyRose3").pack()

    Button(login,text="LOGIN",font=("monotype corsiva",10,"bold"),command=check,).pack()
    Label(login,text="",bg="MistyRose3").pack()
    Label(login,text="**IF NOTHING HAPPENS AFTER LOGGING IN",fg="MistyRose4",bg="MistyRose3").pack()
    Label(login,text=" THEN KINDLY, ENTER CORRECT DETAILS**",fg="MistyRose4",bg="MistyRose3").pack()
    Label(login,text="",bg="MistyRose3").pack()

    


def main():
    global window
    window=Tk()
    window.geometry("300x300")
    window.configure(bg="yellow")   
    window.title("ORDER YOUR FOOD HERE")

    
    Label(window,text="",bg="yellow").pack()
    c1=Button(window,text="CREATE ACCOUNT",fg="yellow",bg="purple",command=create_account).pack()
    Label(window,text="",bg="yellow").pack()
    
    c2=Button(window,text="LOG IN",fg="yellow",bg="purple",command=login_window).pack()
    Label(window,text="",bg="yellow").pack()
   
    c3=Button(window,text="EXIT",fg="yellow",bg="purple",command=window.destroy).pack()
    Label(window,text="                                                            ",font=("monotype corsiva",10,"italic","underline"),bg="yellow").pack()
    
    
    Label(window,text="*PLEASE SELECT ANY ONE OPTION*",font=("monotype corsiva",10,"italic","underline"),bg="yellow").pack()
    
    window.mainloop()
    
    
main()




