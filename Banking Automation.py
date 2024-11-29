#!/usr/bin/env python
# coding: utf-8

# In[1]:


# # Database Design
# - Database product---->SQLite(easy to use,portable)
# 
# #### Tables
# - accounts
#     - acn_no int primary key auto increment
#     - acn_user text
#     - acn_pass text
#     - acn_type text
#     - acn_bal float
#     - acn_opendate text
#     - acn_email text
#     - acn_mob text
# - txns
#     - txn_acn_no int
#     - txn_amt float
#     - txn_type text
#     - txn_update_bal float
#     - txn_date text


# In[2]:


from tkinter import *
from tkinter.ttk import Combobox,Treeview,Style,Scrollbar 
from tkinter import messagebox
import time
import re
import sqlite3


# In[3]:


try:
    conobj=sqlite3.connect(database="banking.sqlite")
    curobj=conobj.cursor()
    curobj.execute("create table accounts(acn_no integer primary key autoincrement,acn_user text,acn_pass text,acn_type text,acn_bal float,acn_opendate text,acn_email text,acn_mob text)")
    curobj.execute("create table txns(txn_acn_no int,txn_amt float,txn_type text,txn_update_bal float,txn_date text)")
    print("tables created")
except:
    print("something went wrong,might be tables already exist")
conobj.close()

win=Tk()
win.state("zoomed")
win.configure(bg="powder blue")
win.resizable(width=False,height=False)

title=Label(win,text="Bank Automation",font=('arial',60,'bold','underline'),bg='powder blue')
title.pack()

t=time.localtime()
ft=time.strftime("%d %b %A,%Y",t)

time_lbl=Label(win,text=ft,font=('arial',15,'bold'),bg='powder blue',fg='purple')
time_lbl.place(relx=.85,rely=.1)

def home_screen():
    frm=Frame(win)
    frm.configure(bg='pink')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
    
    def open_click():
        frm.destroy()
        openaccount_screen()
    
    def recover_click():
        frm.destroy()
        recoverpass_screen()
    
    def login_click():
        acn=acn_entry.get()
        pwd=pass_entry.get()
        if len(acn)==0 or len(pwd)==0:
            messagebox.showerror("Login","Empty fields are not allowed")
            return
        elif not acn.isdigit():
            messagebox.showerror("Login","Incorrect ACN")
            return
        else:
            conobj=sqlite3.connect(database="banking.sqlite")
            curobj=conobj.cursor()
            curobj.execute("select * from accounts where acn_no=? and acn_pass=?",(acn,pwd))
            tup=curobj.fetchone()
            conobj.close()
            if tup==None:
                messagebox.showerror("Login","Invalid ACN/Pass !!")
            else:
                global uname,uacn
                uacn=tup[0]
                uname=tup[1]
                frm.destroy()
                welcome_screen()

    def clear():
        acn_entry.delete(0,"end")
        pass_entry.delete(0,"end")
        acn_entry.focus()
    
    acn_lbl=Label(frm,text='ACN No.',font=('arial',20,'bold'),bg='pink',fg='blue')
    acn_lbl.place(relx=.3,rely=.1)
    
    acn_entry=Entry(frm,font=('arial',20,'bold'),bd=7)
    acn_entry.place(relx=.4,rely=.1)
    acn_entry.focus()
    
    pass_lbl=Label(frm,text='Password',font=('arial',20,'bold'),bg='pink',fg='blue')
    pass_lbl.place(relx=.3,rely=.2)
    
    pass_entry=Entry(frm,font=('arial',20,'bold'),bd=7,show="*")
    pass_entry.place(relx=.4,rely=.2)
    
    btn_login=Button(frm,command=login_click,font=('arial',20,'bold'),bd=7,text="login",bg='powder blue')
    btn_login.place(relx=.4,rely=.3)
    
    btn_clear=Button(frm,command=clear,font=('arial',20,'bold'),bd=7,text="clear",bg='powder blue')
    btn_clear.place(relx=.5,rely=.3)
    
    btn_new=Button(frm,command=open_click,width=16,font=('arial',20,'bold'),bd=7,text="open account",bg='powder blue')
    btn_new.place(relx=.38,rely=.4)
    
    btn_recpass=Button(frm,command=recover_click,width=20,font=('arial',20,'bold'),bd=7,text="recover password",bg='powder blue')
    btn_recpass.place(relx=.36,rely=.5)
    
    
def openaccount_screen():
    frm=Frame(win)
    frm.configure(bg='pink')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
    
    name_lbl=Label(frm,text='Name',font=('arial',20,'bold'),bg='pink',fg='blue')
    name_lbl.place(relx=.3,rely=.1)
    
    name_entry=Entry(frm,font=('arial',20,'bold'),bd=7)
    name_entry.place(relx=.4,rely=.1)
    name_entry.focus()
    
    pass_lbl=Label(frm,text='Password',font=('arial',20,'bold'),bg='pink',fg='blue')
    pass_lbl.place(relx=.3,rely=.2)
    
    pass_entry=Entry(frm,font=('arial',20,'bold'),bd=7,show="*")
    pass_entry.place(relx=.4,rely=.2)
    
    email_lbl=Label(frm,text='Email',font=('arial',20,'bold'),bg='pink',fg='blue')
    email_lbl.place(relx=.3,rely=.3)
    
    email_entry=Entry(frm,font=('arial',20,'bold'),bd=7)
    email_entry.place(relx=.4,rely=.3)
    
    mob_lbl=Label(frm,text='Mob',font=('arial',20,'bold'),bg='pink',fg='blue')
    mob_lbl.place(relx=.3,rely=.4)
    
    mob_entry=Entry(frm,font=('arial',20,'bold'),bd=7)
    mob_entry.place(relx=.4,rely=.4)
    
    acntype_lbl=Label(frm,text='ACN Type',font=('arial',20,'bold'),bg='pink',fg='blue')
    acntype_lbl.place(relx=.3,rely=.5)
    
    acntype_cb=Combobox(frm,font=('arial',20,'bold'),values=['Saving','Current','Fixed Deposit'])
    acntype_cb.current(0)
    acntype_cb.place(relx=.4,rely=.5)
    
    def home_click():
        frm.destroy()
        home_screen()
        
    def open_click():
        name=name_entry.get()
        pwd=pass_entry.get()
        email=email_entry.get()
        mob=mob_entry.get()
        acntype=acntype_cb.get()
        bal=0
        opendate=time.ctime()
        
        if len(name)==0 or len(pwd)==0 or len(email)==0 or len(mob)==0:
            messagebox.showerror("Open Account","Empty fields are not allowed")
            return
        elif not re.fullmatch("[a-zA-Z0-9._]+@[a-zA-Z]+[.][a-zA-Z]+",email):
            messagebox.showerror("Open Account","email is not correct")
            return 
        elif not re.fullmatch("[6-9][0-9]{9}",mob):
            messagebox.showerror("Open Account","Mobile no. is not correct")
            return
        
        import sqlite3
        conobj=sqlite3.connect(database='banking.sqlite')
        curobj=conobj.cursor()
        curobj.execute("insert into accounts(acn_user,acn_pass,acn_type,acn_bal,acn_opendate,acn_email,acn_mob) values(?,?,?,?,?,?,?)",(name,pwd,acntype,bal,opendate,email,mob))
        conobj.commit()
        curobj.close()
        curobj=conobj.cursor()
        curobj.execute("select max(acn_no) from accounts")
        tup=curobj.fetchone()
        conobj.close()
        messagebox.showinfo("Open Account",f"Your Account is Opend with ACN:{tup[0]}")
        name_entry.delete(0,"end")
        pass_entry.delete(0,"end")
        email_entry.delete(0,"end")
        mob_entry.delete(0,"end")
        name_entry.focus()
        
    btn_back=Button(frm,command=home_click,font=('arial',20,'bold'),bd=7,text="back",bg='powder blue')
    btn_back.place(relx=0,rely=0)
    
    btn_open=Button(frm,command=open_click,font=('arial',20,'bold'),bd=7,text="open",bg='powder blue')
    btn_open.place(relx=.4,rely=.6)
    
    btn_clear=Button(frm,font=('arial',20,'bold'),bd=7,text="clear",bg='powder blue')
    btn_clear.place(relx=.5,rely=.6)
    
    
def recoverpass_screen():
    frm=Frame(win)
    frm.configure(bg='pink')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
    
    def home_click():
        frm.destroy()
        home_screen()

    def recoverpass_db():
        acn=acn_entry.get()
        email=email_entry.get()
        mob=mob_entry.get()

        conobj=sqlite3.connect(database="banking.sqlite")
        curobj=conobj.cursor()
        curobj.execute("select acn_pass from accounts where acn_no=? and acn_email=? and acn_mob=?",(acn,email,mob))
        tup=curobj.fetchone()
        conobj.close()
        if tup==None:
            messagebox.showerror("Recover Pass","Account does not exist !!")
        else:
            messagebox.showinfo("Recover Pass",f"Your Password={tup[0]}")
    
    btn_back=Button(frm,command=home_click,font=('arial',20,'bold'),bd=7,text="back",bg='powder blue')
    btn_back.place(relx=0,rely=0)
    
    acn_lbl=Label(frm,text='ACN No.',font=('arial',20,'bold'),bg='pink',fg='blue')
    acn_lbl.place(relx=.3,rely=.1)
    
    acn_entry=Entry(frm,font=('arial',20,'bold'),bd=7)
    acn_entry.place(relx=.4,rely=.1)
    acn_entry.focus()
    
    email_lbl=Label(frm,text='Email',font=('arial',20,'bold'),bg='pink',fg='blue')
    email_lbl.place(relx=.3,rely=.2)
    
    email_entry=Entry(frm,font=('arial',20,'bold'),bd=7)
    email_entry.place(relx=.4,rely=.2)
    
    mob_lbl=Label(frm,text='Mob',font=('arial',20,'bold'),bg='pink',fg='blue')
    mob_lbl.place(relx=.3,rely=.3)
    
    mob_entry=Entry(frm,font=('arial',20,'bold'),bd=7)
    mob_entry.place(relx=.4,rely=.3)
    
    btn_open=Button(frm,command=recoverpass_db,font=('arial',20,'bold'),bd=7,text="recover",bg='powder blue')
    btn_open.place(relx=.4,rely=.4)
    
    btn_clear=Button(frm,font=('arial',20,'bold'),bd=7,text="clear",bg='powder blue')
    btn_clear.place(relx=.52,rely=.4)
    
    
def welcome_screen():
    frm=Frame(win)
    frm.configure(bg='pink')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
    
    def logout_click():
        res=messagebox.askquestion("Logout","Do you want to exit from application?")
        if res=='yes':
            frm.destroy()
            home_screen()
     
    def update_screen():
        ifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
        ifrm.configure(bg='white')
        ifrm.place(relx=.2,rely=.1,relwidth=.7,relheight=.6)

        def update_db():
            name=name_entry.get()
            pwd=pass_entry.get()
            email=email_entry.get()
            mob=mob_entry.get()
            conobj=sqlite3.connect(database="banking.sqlite")
            curobj=conobj.cursor()
            curobj.execute("update accounts set acn_user=?,acn_pass=?,acn_email=?,acn_mob=? where acn_no=?",(name,pwd,email,mob,uacn))
            conobj.commit()
            conobj.close()
            messagebox.showinfo("Update Profile","Profile Updated")
            frm.destroy()
            global uname
            uname=name
            welcome_screen()
            
            
        
        conobj=sqlite3.connect(database="banking.sqlite")
        curobj=conobj.cursor()
        curobj.execute("select * from accounts where acn_no=?",(uacn,))
        tup=curobj.fetchone()
        conobj.close()
        
        title_lbl=Label(ifrm,text='This is Update Profile Screen',font=('arial',20,'bold'),bg='white',fg='purple')
        title_lbl.pack()
        
        name_lbl=Label(ifrm,text='Name',font=('arial',15,'bold'),bg='white',fg='blue')
        name_lbl.place(relx=.1,rely=.2)
        
        name_entry=Entry(ifrm,font=('arial',15,'bold'),border=7)
        name_entry.place(relx=.2,rely=.2)
        name_entry.insert(0,tup[1])
        
        pass_lbl=Label(ifrm,text='Pass',font=('arial',15,'bold'),bg='white',fg='blue')
        pass_lbl.place(relx=.1,rely=.35)
        
        pass_entry=Entry(ifrm,font=('arial',15,'bold'),border=7)
        pass_entry.place(relx=.2,rely=.35)
        pass_entry.insert(0,tup[2])
        
        email_lbl=Label(ifrm,text='Email',font=('arial',15,'bold'),bg='white',fg='blue')
        email_lbl.place(relx=.5,rely=.2)
        
        email_entry=Entry(ifrm,font=('arial',15,'bold'),border=7)
        email_entry.place(relx=.6,rely=.2)
        email_entry.insert(0,tup[6])
        
        mob_lbl=Label(ifrm,text='Mob',font=('arial',15,'bold'),bg='white',fg='blue')
        mob_lbl.place(relx=.5,rely=.35)
        
        mob_entry=Entry(ifrm,font=('arial',15,'bold'),border=7)
        mob_entry.place(relx=.6,rely=.35)
        mob_entry.insert(0,tup[7])
        
        btn=Button(ifrm,command=update_db,text="Update",font=('arial',20,'bold'),border=7,bg='powder blue')
        btn.place(relx=.7,rely=.7)
        
    def balance_screen():
        ifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
        ifrm.configure(bg='white')
        ifrm.place(relx=.2,rely=.1,relwidth=.7,relheight=.6)

        conobj=sqlite3.connect(database="banking.sqlite")
        curobj=conobj.cursor()
        curobj.execute("select acn_no,acn_bal,acn_opendate from accounts where acn_no=?",(uacn,))
        tup=curobj.fetchone()
        conobj.close()
        
        title_lbl=Label(ifrm,text='This is Check balance Screen',font=('arial',20,'bold'),bg='white',fg='purple')
        title_lbl.pack()
        
        acn_lbl=Label(ifrm,text=f'Account No \t{tup[0]}',font=('arial',15,'bold'),bg='white',fg='blue')
        acn_lbl.place(relx=.2,rely=.2)
        
        bal_lbl=Label(ifrm,text=f'Available Bal\t {tup[1]}',font=('arial',15,'bold'),bg='white',fg='blue')
        bal_lbl.place(relx=.2,rely=.3)

        opendate_lbl=Label(ifrm,text=f'ACN open date\t {tup[2]}',font=('arial',15,'bold'),bg='white',fg='blue')
        opendate_lbl.place(relx=.2,rely=.4)
    
        
        
        
    def deposit_screen():
        ifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
        ifrm.configure(bg='white')
        ifrm.place(relx=.2,rely=.1,relwidth=.7,relheight=.6)

        def deposit_db():
            amt=float(amt_entry.get())
            conobj=sqlite3.connect(database="banking.sqlite")
            curobj=conobj.cursor()
            curobj.execute("select acn_bal from accounts where acn_no=?",(uacn,))
            tup=curobj.fetchone()
            bal=tup[0]
            curobj.close()

            curobj=conobj.cursor()
            curobj.execute("update accounts set acn_bal=acn_bal+? where acn_no=?",(amt,uacn))
            curobj.execute("insert into txns values(?,?,?,?,?)",(uacn,amt,'Cr.',bal+amt,time.ctime()))
            conobj.commit()
            conobj.close()

            messagebox.showinfo("Deposit Amt",f"{amt} deposited ")
        
        title_lbl=Label(ifrm,text='This is Deposit Screen',font=('arial',20,'bold'),bg='white',fg='purple')
        title_lbl.pack()
        
        amt_lbl=Label(ifrm,text='Amount',font=('arial',20,'bold'),bg='white',fg='blue')
        amt_lbl.place(relx=.28,rely=.2)
        
        amt_entry=Entry(ifrm,font=('arial',20,'bold'),border=7)
        amt_entry.place(relx=.4,rely=.2)
        
        btn=Button(ifrm,command=deposit_db,text="Submit",font=('arial',20,'bold'),border=7,bg='powder blue')
        btn.place(relx=.4,rely=.35)
        
    def withdraw_screen():
        ifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
        ifrm.configure(bg='white')
        ifrm.place(relx=.2,rely=.1,relwidth=.7,relheight=.6)

        def withdraw_db():
            amt=float(amt_entry.get())
            conobj=sqlite3.connect(database="banking.sqlite")
            curobj=conobj.cursor()
            curobj.execute("select acn_bal from accounts where acn_no=?",(uacn,))
            tup=curobj.fetchone()
            bal=tup[0]
            curobj.close()
            if bal>=amt:
                curobj=conobj.cursor()
                curobj.execute("update accounts set acn_bal=acn_bal-? where acn_no=?",(amt,uacn))
                curobj.execute("insert into txns values(?,?,?,?,?)",(uacn,amt,'Db.',bal-amt,time.ctime()))
                conobj.commit()
                conobj.close()
    
                messagebox.showinfo("Withdraw Amt",f"{amt} withdrawn ")
            else:
                messagebox.showinfo("Withdraw Amt","Insufficient Bal")
            

        
        title_lbl=Label(ifrm,text='This is Withdraw Screen',font=('arial',20,'bold'),bg='white',fg='purple')
        title_lbl.pack()
        
        amt_lbl=Label(ifrm,text='Amount',font=('arial',20,'bold'),bg='white',fg='blue')
        amt_lbl.place(relx=.28,rely=.2)
        
        amt_entry=Entry(ifrm,font=('arial',20,'bold'),border=7)
        amt_entry.place(relx=.4,rely=.2)
        
        btn=Button(ifrm,command=withdraw_db,text="Submit",font=('arial',20,'bold'),border=7,bg='powder blue')
        btn.place(relx=.4,rely=.35)
        
    def transfer_screen():
        ifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
        ifrm.configure(bg='white')
        ifrm.place(relx=.2,rely=.1,relwidth=.7,relheight=.6)

        def transfer_db():
            amt=float(amt_entry.get())
            toacn=to_entry.get()
            
            conobj=sqlite3.connect(database="banking.sqlite")
            curobj=conobj.cursor()
            curobj.execute("select acn_bal from accounts where acn_no=?",(uacn,))
            tup=curobj.fetchone()
            bal_frm=tup[0]
            curobj.close()

            curobj=conobj.cursor()
            curobj.execute("select acn_bal from accounts where acn_no=?",(toacn,))
            tup=curobj.fetchone()
            bal_to=tup[0]
            curobj.close()
            
            curobj=conobj.cursor()
            curobj.execute("select acn_no from accounts where acn_no=?",(toacn,))
            tup=curobj.fetchone()
            curobj.close()
            if tup==None:
                messagebox.showerror("Transfer",f"To ACN {toacn} does not exist !")
                
            else:
                if bal_frm>=amt:
                    curobj=conobj.cursor()
                    curobj.execute("update accounts set acn_bal=acn_bal-? where acn_no=?",(amt,uacn))
                    curobj.execute("update accounts set acn_bal=acn_bal+? where acn_no=?",(amt,toacn))
                    
                    curobj.execute("insert into txns values(?,?,?,?,?)",(uacn,amt,'Db.',bal_frm-amt,time.ctime()))
                    curobj.execute("insert into txns values(?,?,?,?,?)",(toacn,amt,'Cr.',bal_to+amt,time.ctime()))
                   
                    conobj.commit()
                    conobj.close()
        
                    messagebox.showinfo("Transfer Amt",f"{amt} transfered to ACN {toacn} ")
                else:
                    messagebox.showwarning("Withdraw Amt","Insufficient Bal")
            
        title_lbl=Label(ifrm,text='This is Transfer Screen',font=('arial',20,'bold'),bg='white',fg='purple')
        title_lbl.pack()
        
        to_lbl=Label(ifrm,text='TO',font=('arial',20,'bold'),bg='white',fg='blue')
        to_lbl.place(relx=.28,rely=.2)
        
        to_entry=Entry(ifrm,font=('arial',20,'bold'),border=7)
        to_entry.place(relx=.4,rely=.2)
        
        amt_lbl=Label(ifrm,text='Amount',font=('arial',20,'bold'),bg='white',fg='blue')
        amt_lbl.place(relx=.28,rely=.35)
        
        amt_entry=Entry(ifrm,font=('arial',20,'bold'),border=7)
        amt_entry.place(relx=.4,rely=.35)
        
        btn=Button(ifrm,command=transfer_db,text="Submit",font=('arial',20,'bold'),border=7,bg='powder blue')
        btn.place(relx=.4,rely=.5)

    def txnhist_screen():
        ifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
        ifrm.configure(bg='white')
        ifrm.place(relx=.2,rely=.1,relwidth=.7,relheight=.6)

        title_lbl=Label(ifrm,text='This is Transaction History Screen',font=('arial',20,'bold'),bg='white',fg='purple')
        title_lbl.pack()

        tv=Treeview(ifrm)
        tv.place(x=0,y=0,relheight=1,relwidth=1)
        
        style = Style()
        style.configure("Treeview.Heading", font=('Arial',15,'bold'),foreground='black')
        sb=Scrollbar(ifrm,orient='vertical',command=tv.yview)
        sb.place(relx=.98,y=0,relheight=1)
        
        tv['columns']=('Txn date','Txn amount','Txn type','Updated bal')
        
        tv.column('Txn date',width=150,anchor='c')
        tv.column('Txn amount',width=100,anchor='c')
        tv.column('Txn type',width=100,anchor='c')
        tv.column('Updated bal',width=100,anchor='c')

        tv.heading('Txn date',text='Txn date')
        tv.heading('Txn amount',text='Txn amount')
        tv.heading('Txn type',text='Txn type')
        tv.heading('Updated bal',text='Updated bal')
        
        tv['show']='headings'

        con=sqlite3.connect(database="banking.sqlite")
        cur=con.cursor()
        cur.execute("select txn_date,txn_amt,txn_type,txn_update_bal from txns where txn_acn_no=?",(uacn,))
        for row in cur:
            tv.insert("","end",values=(row[0],row[1],row[2],row[3]),tags='ft')
            tv.tag_configure('ft',font=('',12))
        con.close()

    btn_logout=Button(frm,command=logout_click,font=('arial',20,'bold'),bd=7,text="logout",bg='powder blue')
    btn_logout.place(relx=.92,rely=0)
    
    wel_lbl=Label(frm,text=f'Welcome,{uname}',font=('arial',20,'bold'),bg='pink',fg='blue')
    wel_lbl.place(relx=0,rely=0)
    
    btn_profile=Button(frm,command=update_screen,width=12,font=('arial',20,'bold'),bd=7,text="update profile",bg='powder blue')
    btn_profile.place(relx=0,rely=.1)
    
    btn_bal=Button(frm,command=balance_screen,width=12,font=('arial',20,'bold'),bd=7,text="check balance",bg='powder blue')
    btn_bal.place(relx=0,rely=.2)
    
    btn_deposit=Button(frm,command=deposit_screen,width=12,font=('arial',20,'bold'),bd=7,text="deposit",bg='powder blue')
    btn_deposit.place(relx=0,rely=.3)
    
    btn_withdraw=Button(frm,command=withdraw_screen,width=12,font=('arial',20,'bold'),bd=7,text="withdraw",bg='powder blue')
    btn_withdraw.place(relx=0,rely=.4)
    
    btn_transfer=Button(frm,command=transfer_screen,width=12,font=('arial',20,'bold'),bd=7,text="transfer",bg='powder blue')
    btn_transfer.place(relx=0,rely=.5)

    btn_txnhist=Button(frm,command=txnhist_screen,width=12,font=('arial',20,'bold'),bd=7,text="tranx history",bg='powder blue')
    btn_txnhist.place(relx=0,rely=.6)
    
home_screen()
win.mainloop()


# In[ ]:




