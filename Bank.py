from tkinter import *
import tkinter
import os 
from PIL import Image, ImageTk 
from tkinter import messagebox
import datetime as datetime
import string
import pyperclip
import random


bank_Window=Tk()
bank_Window.title('Banking App')
bank_Window.geometry('340x550')

bank_Window.configure(bg='black', pady=50)

"""
    below is the Password generating code
"""

choice = IntVar()

def passGen():

    global passEntry
    global pass_screen
    global generateDone_notif
    
    pass_screen=Toplevel(bank_Window)
    pass_screen.grab_set()
    
    
    pass_screen.config(bg="black", pady=10, padx=20)
    pass_screen.geometry('300x550')
    passLabel = Label(pass_screen, text="Generate Password", bg="black",
                      fg="white", font=('Baskerville Old Face', 16, 'bold'))
    passLabel.grid(sticky=N, pady=20, padx=30)

    radioBtn1 = Radiobutton(pass_screen, text='Strong Password', bg="black",
                            cursor="hand2", fg="white", value=1, variable=choice)
    radioBtn1.grid(row=2, sticky=W, padx=5)

    radioBtn2 = Radiobutton(pass_screen, text='Very Strong Password', bg="black",
                            cursor="hand2", fg="white", value=2, variable=choice)
    radioBtn2.grid(row=3, sticky=W, padx=5)

    passEntry = Entry(pass_screen, width=30, border=2, font=("Arial", 8))
    passEntry.grid(row=5, pady=10)
    
    generateDone_notif=Label(pass_screen, font=('Baskervill Old Face',10),bg='black', fg='green')
    generateDone_notif.grid(row=6,sticky=N, pady=10)
    
    
    
    generatorButton = Button(pass_screen, text="Generate", bg="black",
                             fg="white", cursor="hand2", command=generatePass, font=("Arial", 12))
    generatorButton.grid(row=8, sticky=W, padx=10, pady=5)

    copyButton = Button(pass_screen, text="Copy", command=copy, fg="white",bg="black", cursor="hand2",
                        font=("Arial", 12))
    copyButton.grid(row=8, sticky=E, padx=30, pady=5)

def forgetReg():
    pass_screen.place(x=300,y=3)
    register_screen.place_forget()

def generatePass():
    # password_length = 8 if choice.get() == 1 else 12

    lower_char = string.ascii_lowercase
    upper_char = string.ascii_uppercase
    num = string.digits
    char = string.punctuation

    passwordPool = lower_char + upper_char + num + char

    if choice.get() == 1:
        password_length = 8
        passEntry.delete(0, tkinter.END)
        password = random.sample(lower_char+num+upper_char, password_length)
        password = "".join(password)
        passEntry.insert(0, password)
        messagebox.showinfo(title="Congratulations!", 
             message=("YOU HAVE SUCCESSFULLY GENERATED YOUR PASSWORD!!\n\n Please copy and past it on the password field to complete your registration.\n"))
    
        generateDone_notif.config(fg="#35dd02", text="Copy and close to continue.")
  
        return password

    elif choice.get() == 2:
        password_length = 12
        passEntry.delete(0, tkinter.END)
        password = random.sample(passwordPool, password_length)
        password = "".join(password)
        passEntry.insert(0, password)
        messagebox.showinfo(title="Congratulations!", 
             message=("YOU HAVE SUCCESSFULLY GENERATED YOUR PASSWORD!!\n\n Please copy and past it on the password field to complete your registration.\n"))
    
        generateDone_notif.config(fg="#35dd02", text="Copy and close to continue.")
        return password
    
    else :
        generateDone_notif.config(fg="red", text="Select an option.")
        return
   
    pass_screen.grab_set()
   

def copy():
    if passEntry.get() =="":
        generateDone_notif.config(fg="red", text="You have not generated a password.")
        return
    else:
        randomPass=passEntry.get()
        pyperclip.copy(randomPass)
        pass_screen.destroy()

    
def finish_reg():
    name=temp_name.get()
    account_num=temp_account_num.get()
    idNumber=temp_idNumber.get()
    password=temp_password.get()

    all_accounts= os.listdir()
    if name=="" or account_num=="" or idNumber=="" or password=="":
        notif.config(fg="red", text="All fields required *")
        return
  
    
    for name_check in all_accounts:
          
        with open('Login Database.txt', 'r+') as file:
            file_data = file.read()
            details = file_data.split('\n')

            name_check = details[0]
            acc_num=details[1]


        if name ==name_check :
    
            notif.config(fg="red", text="Account already exists")
            
            return
        
        if account_num==acc_num:
            notif.config(fg="red", text="Account already exists")
            return
        else:
            new_file = open('Login Database.txt',"w")
            new_file.write(name+'\n')
            new_file.write(account_num+"\n")
            new_file.write(idNumber+'\n')
            new_file.write(password+'\n')

            new_file.write("0"+"\n")
            new_file.close()
            notif.config(fg="#35dd02", text="Account has been create")
            
            register_screen.destroy()
            login()
            return          


def register():

    global temp_name
    global temp_account_num
    global temp_idNumber
    global temp_password
    global notif
    global register_screen

    temp_name= StringVar()
    temp_account_num=StringVar()
    temp_idNumber=StringVar()
    temp_password=StringVar()

    register_screen= Toplevel(bank_Window)
    register_screen.grab_set()
    register_screen.title('Register')
    register_screen.configure(bg='black',padx=30, pady=10)
    register_screen.geometry('300x550')

    #Reg screen labels and Entries
    Button(register_screen,text="X",command=destroy_register_screen).grid(row=0,sticky=E)
    Label(register_screen, text="Register Account\n",bg='black',fg='white', font=("Baskervill Old Face",16, 'bold')).grid(row=0,sticky=N, padx=40,pady=5)
    Label(register_screen, image=reg_img, bg='black').grid(row=1,sticky=N,pady=10)

    Label(register_screen, text="Full Name: ", font=('Baskervill Old Face', 12), bg='black',fg='white').grid(row=3,sticky=W)
    Entry(register_screen, textvariable=temp_name).grid(row=3, column=0, sticky=E)
    Label(register_screen, text="Account No: ", font=('Baskervill Old Face', 12), bg='black',fg='white').grid(row=4,sticky=W)
    Entry(register_screen, textvariable=temp_account_num).grid(row=4, column=0, sticky=E)
    Label(register_screen, text="ID No: ", font=('Baskervill Old Face', 12), bg='black',fg='white').grid(row=5,sticky=W)
    Entry(register_screen, textvariable=temp_idNumber).grid(row=5, column=0,sticky=E)
    Label(register_screen, text="Password: ", font=('Baskervill Old Face', 12), bg='black',fg='white').grid(row=6,sticky=W)
    Entry(register_screen, textvariable=temp_password,show="*").grid(row=6,column=0,sticky=E)

    notif=Label(register_screen, font=('Baskervill Old Face', 12), bg='black',fg='white')
    notif.grid(row=7,sticky=N, pady=10)

    Button(register_screen, text="Sign up",bg='black',fg='white',cursor="hand2", command=finish_reg ,font=('Baskervill Old Face',12)).grid(row=9,sticky=N,pady=5)


    Button(register_screen, text='Generate Password',bg='black',fg='white', cursor="hand2", font=('Baskervill Old Face', 12),
       command=closeWindows).grid(row=8, sticky=N, pady=5)

def closeWindows():
    passGen() 
    forgetReg()


def destroy_register_screen():
    register_screen.destroy()
def destroy_deposit_screen():
    dashboard()
    deposit_screen.destroy()
   
def destroy_withdraw_screen():
    dashboard()
    withdraw_screen.destroy()

def destroy_beneficiary_screen():
    dashboard()
    beneficiary_screen.destroy()

def destroy_personal_details_screen():
    dashboard()
    personal_details_screen.destroy()

def destroy_account_dashboard():
    
    account_dashboard.destroy()

def destroy_statement_details_screen():
    dashboard()
    statement_details_screen.destroy()


def deposit():
     account_dashboard.destroy()
     global amount
     global deposit_notif
     global current_balance_label
     global deposit_screen
     amount= StringVar()
     
     file=open('Login Database.txt', "r")
     file_data = file.read()
     user_details=file_data.split('\n')
     details_balance=float(user_details[4])

     deposit_screen=Toplevel(bank_Window)
     deposit_screen.grab_set()
     deposit_screen.title('Deposit')
     deposit_screen.configure(bg='black',pady=40,padx=20)
     deposit_screen.geometry('300x550')

     Label(deposit_screen, image=deposit_img, borderwidth=0,bg='black').grid(row=0,sticky=W)
     Button(deposit_screen,text="X",command=destroy_deposit_screen).grid(row=0,sticky=E)

     Label(deposit_screen, text="Deposit",bg='black',fg='white', font=("Baskervill Old Face", 16, 'bold')).grid(row=0,sticky=N,pady=10) 
     Label(deposit_screen,text='\nPlease enter the amount you\nwould like to deposit below.\n',bg='black',fg='white', font=("Baskervill Old Face",12)).grid(row=1,sticky=N,pady=10)
     current_balance_label=Label(deposit_screen, text=f"Current Balance: R{details_balance:.2f}",bg='black',fg='white', font=('Baskervill Old Face', 12))
     current_balance_label.grid(row=3,sticky=W)
     Label(deposit_screen,text="\nAmount: R\n",bg='black',fg='white', font=('Baskervill Old Face',12)).grid(row=4,sticky=W)
     Entry(deposit_screen,textvariable=amount).grid(row=4,column=0,sticky=E)

    
     

     deposit_notif=Label(deposit_screen, font=('Baskervill Old Face',12),bg='black')
     deposit_notif.grid(row=5, sticky=N, pady=5)

     
     Button(deposit_screen,text='Proceed',cursor="hand2",bg='black',fg='white',font=('Baskervill Old Face', 12), command=finish_deposit).grid(row=6,sticky=W,pady=5)

def finish_deposit():
    if amount.get()=="":
        deposit_notif.config(text="Please enter amount", fg="red")
        return
    if float(amount.get())<=0:
        deposit_notif.config(text='Please enter valid amount', fg="red")
        return
    
    file=open('Login Database.txt', 'r+')
    file_data=file.read()
    details=file_data.split('\n')
    current_balance=details[4]
    updated_balance=current_balance
    updated_balance= float(updated_balance)+float(amount.get())
    file_data=file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    transaction_datetime = datetime.datetime.now()

    transaction_log("\nA deposit of: +R"+str(amount.get())+" has been made.\n\tDate: "+transaction_datetime.strftime("%y/%m/%d %H:%M:%S")+ f".\n\tUpdated balance: R{updated_balance:.2f}")

    current_balance_label.config(text=f"Current Balance: R{updated_balance:.2f}",fg="#35dd02",bg='black')
    deposit_notif.config(text="Balance Updated",fg='#35dd02',bg='black')
    messagebox.showinfo(title="Congratulations!", message=("YOUR TRANSACTION WAS SUCCESSFUL!!! \n\n"))
    
    amount.set("")


    "Transactions Log on a text file"

def transaction_log(transaction):
    with open('Transaction Log.txt', 'a' ) as file:
        file.write(transaction +"\n")

def withdraw():
     account_dashboard.destroy()
     global withdraw_amount
     global withdraw_notif
     global current_balance_label
     global withdraw_screen
     withdraw_amount= StringVar()
     file=open('Login Database.txt', "r")
     file_data = file.read()
     user_details=file_data.split('\n')
     details_balance=float(user_details[4])

     withdraw_screen=Toplevel(bank_Window)
     withdraw_screen.grab_set()
     withdraw_screen.title('Withdraw')
     withdraw_screen.configure(bg='black',pady=40,padx=20)
     withdraw_screen.geometry('300x550')

     Label(withdraw_screen, image=withdraw_img, borderwidth=0,bg='black').grid(row=0,sticky=W)
     Button(withdraw_screen,text="X",command=destroy_withdraw_screen).grid(row=0,sticky=E)

     Label(withdraw_screen, text="Withdraw",bg='black',fg='white', font=("Baskervill Old Face", 16, 'bold')).grid(row=0,sticky=N,pady=10) 
     Label(withdraw_screen,text='\nPlease enter the amount you\nwould like to withdraw below.\n',bg='black',fg='white', font=("Baskervill Old Face",12)).grid(row=1,sticky=N,pady=10)
     current_balance_label=Label(withdraw_screen, text=f"Current Balance: R{details_balance:.2f}",bg='black',fg='white', font=('Baskervill Old Face', 12))
     current_balance_label.grid(row=3,sticky=W)
     Label(withdraw_screen,text="\nAmount: R\n",bg='black',fg='white', font=('Baskervill Old Face',12)).grid(row=4,sticky=W)
     Entry(withdraw_screen,textvariable=withdraw_amount).grid(row=4,column=0,sticky=E)

     withdraw_notif=Label(withdraw_screen,bg='black' ,font=('Baskervill Old Face',12))
     withdraw_notif.grid(row=5, sticky=N, pady=5)

     Button(withdraw_screen,text='Proceed',cursor="hand2",bg='black',fg='white',font=('Baskervill Old Face', 12), command=finish_withdraw).grid(row=6,sticky=W,pady=5)

def finish_withdraw():
    if withdraw_amount.get()=="":
        withdraw_notif.config(text="Enter amount", fg="red")
        return
     
    if float(withdraw_amount.get())<=0:
        messagebox.showinfo(title="!!!!", message="Zero (0) and Negative numbers(-1) are not accepted. \nPlease enter a valid amount.")

        withdraw_notif.config(text='Please enter valid amount', fg="red")
        return
    
    file=open('Login Database.txt', 'r+')
    file_data=file.read()
    details=file_data.split('\n')
    current_balance=details[4]

    if float(withdraw_amount.get())>float(current_balance):

        withdraw_notif.config(text="Insufficient Funds!", fg="red")
        return

    updated_balance=current_balance
    updated_balance= float(updated_balance)-float(withdraw_amount.get())
    file_data=file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    transaction_datetime = datetime.datetime.now()
    transaction_log("\nA Withdrawal of: -R"+withdraw_amount.get()+" has been made on \n\t"+transaction_datetime.strftime("%y/%m/%d %H:%M:%S")+ f"\n\tUpdated balance: R{updated_balance:.2f}")

    messagebox.showinfo(title="Congratulations!", message=("YOUR TRANSACTION WAS SUCCESSFUL!!! \n\nPlease take your cash."))

    current_balance_label.config(text=f"Current Balance: R{updated_balance:.2f}",fg='#35dd02')
    withdraw_notif.config(text="Balance Updated",fg='#35dd02',)
    withdraw_amount.set("")

def beneficiary():
     account_dashboard.destroy()
     global beneficiary_amount
     global beneficiary_notif
     global current_balance_label
     global beneficiary_screen
     global beneficiary_account
     beneficiary_amount= StringVar()
     beneficiary_account=StringVar()
     file=open('Login Database.txt', "r")
     file_data = file.read()
     user_details=file_data.split('\n')
     details_balance=float(user_details[4])

     beneficiary_screen=Toplevel(bank_Window)
     beneficiary_screen.grab_set()
     beneficiary_screen.title('Withdraw')
     beneficiary_screen.configure(bg='black',pady=40,padx=20)
     beneficiary_screen.geometry('300x550')

     Label(beneficiary_screen, image=withdraw_img, borderwidth=0,bg='black').grid(row=0,sticky=W)
     Button(beneficiary_screen,text="X",command=destroy_beneficiary_screen).grid(row=0,sticky=E)

     Label(beneficiary_screen, text="Pay",bg='black',fg='white', font=("Baskervill Old Face", 16, 'bold')).grid(row=0,sticky=N,pady=10) 
     Label(beneficiary_screen,text='\nPlease enter the amount you\nwould like to withdraw below.\n',bg='black',fg='white', font=("Baskervill Old Face",12)).grid(row=1,sticky=N,pady=10)
     current_balance_label=Label(beneficiary_screen, text=f"Current Balance: R{details_balance:.2f}",bg='black',fg='white', font=('Baskervill Old Face', 12))
     current_balance_label.grid(row=3,sticky=W)

     Label(beneficiary_screen,text="\nAmount: R\n",bg='black',fg='white', font=('Baskervill Old Face',12)).grid(row=5,sticky=W)
     Entry(beneficiary_screen,textvariable=beneficiary_amount).grid(row=5,column=0,sticky=E)

     Label(beneficiary_screen,text="\nAccount No.\n",bg='black',fg='white', font=('Baskervill Old Face',12)).grid(row=4,sticky=W)
     Entry(beneficiary_screen,textvariable=beneficiary_account).grid(row=4,column=0,sticky=E)

     beneficiary_notif=Label(beneficiary_screen,bg='black' ,font=('Baskervill Old Face',12))
     beneficiary_notif.grid(row=6, sticky=N, pady=5)

     Button(beneficiary_screen,text='Pay',cursor="hand2",bg='black',fg='white',font=('Baskervill Old Face', 12), command=finish_payment).grid(row=8,sticky=W,pady=5)

def finish_payment():
    if  beneficiary_account.get()=="":
        beneficiary_notif.config(text="Enter beneficiary account", fg="red")
        return
     
    if beneficiary_amount.get()=="":
        beneficiary_notif.config(text="Enter amount", fg="red")
        return
     
    if float(beneficiary_amount.get())<=0:
        messagebox.showinfo(title="!!!!", message="Zero (0) and Negative numbers(-1) are not accepted. \nPlease enter a valid amount.")

        beneficiary_notif.config(text='Please enter valid amount', fg="red")
        return
    
    file=open('Login Database.txt', 'r+')
    file_data=file.read()
    details=file_data.split('\n')
    current_balance=details[4]

    if float(beneficiary_amount.get())>float(current_balance):

        beneficiary_notif.config(text="Insufficient Funds!", fg="red")
        return

    updated_balance=current_balance
    updated_balance= float(updated_balance)-float(beneficiary_amount.get())
    file_data=file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    transaction_datetime = datetime.datetime.now()
    transaction_log("\nA Payment of: -R"+beneficiary_amount.get()+" has been made on \n\tTo Account: "+beneficiary_account.get()+"\n\t"+'Date: '+transaction_datetime.strftime("%y/%m/%d %H:%M:%S")+ f"\n\tUpdated balance: R{updated_balance:.2f}")

    messagebox.showinfo(title="Congratulations!", message=("\nYOUR PAYMENT WAS SUCCESSFUL!!! \n\n"))

    current_balance_label.config(text=f"Current Balance: R{updated_balance:.2f}",fg='#35dd02')
    beneficiary_notif.config(text="Balance Updated",fg='#35dd02',)
    beneficiary_account.set("")
    beneficiary_amount.set("")


def personal_details():
    account_dashboard.destroy()
    file=open('Login Database.txt', 'r')
    file_data=file.read()
    user_details=file_data.split('\n')
    details_name=user_details[0]
    details_account_num=user_details[1]
    details_idNumber=user_details[2]
    details_balance=float(user_details[4])
    global personal_details_screen

    personal_details_screen=Toplevel(bank_Window)
    personal_details_screen.grab_set()
    personal_details_screen.title('Personal Details')
    personal_details_screen.configure(bg='black',pady=30, padx=10)
    personal_details_screen.geometry('300x550')

    Button(personal_details_screen,text="X", command=destroy_personal_details_screen).grid(row=0,sticky=E)

    Label(personal_details_screen,bg='black', image=details_img, borderwidth=0).grid(row=0,sticky=W,pady=15)
    Label(personal_details_screen,bg='black', image=details_img_bottom, borderwidth=0).grid(row=6,sticky=N,pady=65, padx=10)

    Label(personal_details_screen, text="\nPersonal Details\n",bg='black',fg='white', font=("Baskervill Old Face",16, 'bold')).grid(row=0,sticky=N, padx=50,pady=10)

    Label(personal_details_screen, text="\n Account Holder: "+details_name,bg='black',fg='white', font=("Baskervill Old Face",12)).grid(row=1,sticky=W)
    Label(personal_details_screen, text=" Account Number: "+details_account_num,bg='black',fg='white', font=("Baskervill Old Face",12)).grid(row=2,sticky=W)
    Label(personal_details_screen, text=" ID Number: "+details_idNumber,bg='black',fg='white', font=("Baskervill Old Face",12)).grid(row=3,sticky=W)
    Label(personal_details_screen, text=f" Balance: R{details_balance:.2f}",bg='black',fg='white', font=("Baskervill Old Face",12)).grid(row=4,sticky=W)

def statement_details():
    account_dashboard.destroy()
    file = open('Login Database.txt', 'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    details_name = user_details[0]
    details_account_num = user_details[1]
    details_idNumber = user_details[2]
    details_balance = float(user_details[4])
    global statement_details_screen

    transaction_file = open('Transaction Log.txt', 'r+')
    transaction_details = transaction_file.read()

    statement_details_screen = Toplevel(bank_Window)
    statement_details_screen.grab_set()
    statement_details_screen.title('Bank Statement')
    statement_details_screen.configure(bg='black', pady=10)
    statement_details_screen.geometry('320x550')

    frame = Frame(statement_details_screen, bg='black')
    frame.pack(fill=BOTH, expand=True)

    scrollbar = Scrollbar(frame, orient='vertical')
    scrollbar.pack(side=RIGHT, fill=Y)

    canvas = Canvas(frame, bg='black', yscrollcommand=scrollbar.set)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar.config(command=canvas.yview)

    canvas_frame = Frame(canvas, bg='black')
    canvas.create_window((0, 0), window=canvas_frame, anchor='nw')

    canvas_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

    Label(canvas_frame, bg='black', image=details_img, borderwidth=0).grid(row=0, sticky=W, pady=15)
    Label(canvas_frame, bg='black', image=details_img_bottom, borderwidth=0).grid(row=7, sticky=N, pady=20, padx=10)
    Button(canvas_frame, text="X", command=destroy_statement_details_screen).grid(row=0, sticky=E)

    Label(canvas_frame, text="\nBank statement\n", bg='black', fg='white', font=("Baskervill Old Face", 16, 'bold')).grid(row=0, sticky=N, pady=10)

    Label(canvas_frame, text="Account Holder: " + details_name, bg='black', fg='white', font=("Baskervill Old Face", 12, 'bold')).grid(row=1, sticky=W)
    Label(canvas_frame, text="Account Number: " + details_account_num, bg='black', fg='white', font=("Baskervill Old Face", 12, 'bold')).grid(row=2, sticky=W)
    Label(canvas_frame, text="ID Number: " + details_idNumber + "\n", bg='black', fg='white', font=("Baskervill Old Face", 12, 'bold')).grid(row=3, sticky=W)

    Label(canvas_frame, text=transaction_details, bg='black', fg='white', font=("Baskervill Old Face", 12)).grid(row=4, sticky=W)
    Label(canvas_frame, text=f"Current balance: R{details_balance:.2f}", bg='black', fg='white', font=("Baskervill Old Face", 12)).grid(row=5, sticky=W)



def dashboard():
    # global login_name
    global login_account
    global account_dashboard
    all_accounts=os.listdir()
    account_No=temp_login_account.get()
    login_password=temp_login_password.get()


    if account_No=="" and login_password=="":
        login_notif.config(fg="red", text="Enter credentials")
        return
               
    if account_No=="":
          login_notif.config(fg="red", text="Enter account number")  
          return    
          
    if login_password=="":
          login_notif.config(fg="red", text="Enter password")    
          return
          
    while 'Login Database.txt' in all_accounts:
            file=open('Login Database.txt',"r")
            file_data = file.read()
            file_data= file_data.split('\n')
            password= file_data[3]
            login_account=file_data[1]
            name=file_data[0]
            
            if login_password != password:
                login_notif.config(fg="red", text="Incorrect password")
                return
                
            if login_password==password and account_No==login_account:
                login_screen.destroy()
                account_dashboard=Toplevel(bank_Window)
                account_dashboard.title('Home')
                account_dashboard.configure(bg='black',pady=30, padx=30)
                account_dashboard.geometry('300x550')
                account_dashboard.grab_set()

                Button(account_dashboard,text="X",command=destroy_account_dashboard).grid(row=0,sticky=E)
                Label(account_dashboard, text="Account Dashboard",bg='black',fg='white', font=("Baskervill Old Face",12)).grid(row=0,sticky=N,pady=10)
                Label(account_dashboard, text="Welcome " +name,bg='black',fg='white', font=("Baskervill Old Face",12, 'bold')).grid(row=1,sticky=N,pady=5)
                Label (account_dashboard, image=login_img, borderwidth=0,bg='black').grid(row=2,sticky=N,pady=10)

                Button(account_dashboard,bg='black',fg='white', text="Personal Details",font=("Baskervill Old Face",12),width=15,command=personal_details).grid(row=3,sticky=N,padx=5,pady=2)
                Button(account_dashboard,bg='black',fg='white', text="Deposit",font=("Baskervill Old Face",12),width=15,command=deposit).grid(row=4,sticky=N,padx=10,pady=2)
                Button(account_dashboard,bg='black',fg='white', text="Withdraw",font=("Baskervill Old Face",12),width=15,command=withdraw).grid(row=5,sticky=N,padx=10,pady=2)
                Button(account_dashboard,bg='black',fg='white', text="Pay Beneficiary",font=("Baskervill Old Face",12),width=15,command=beneficiary).grid(row=6,sticky=N,padx=10,pady=2)
                Button(account_dashboard,bg='black',fg='white', text="Statement",font=("Baskervill Old Face",12),width=15,command=statement_details).grid(row=7,sticky=N,padx=10,pady=2)
                # Label(account_dashboard).grid(row=5,sticky=N,pady=10)

                return
            else: 
                login_notif.config(fg="red", text="Account number does not exist")    
                return
    login_notif.config(fg="red", text="Lets find out")



def login():
    
    global temp_login_account
    global temp_login_password
    global login_notif
    global login_screen
    temp_login_account=StringVar()
    temp_login_password=StringVar()

#for login screen

    login_screen = Toplevel(bank_Window)
    login_screen.title('Login')
    login_screen.grab_set()
    login_screen.configure(bg='black',pady=40, padx=30)
    login_screen.geometry('300x550')

    Label(login_screen, text=" UBA ", font=('Bell MT', 30,'bold'), bg='black',fg='red').grid(row=0,sticky=N)
    # Label (login_screen, image=login_img_info, borderwidth=0,bg='black').grid(row=0,sticky=N)

    Label(login_screen, text="Login to your acocount", bg='black',fg='white',
          font=('Baskervill Old Face',12, 'bold')).grid(row=1,sticky=N,pady=40,padx=20)

    Label(login_screen, text="Account No:",bg='black',fg='white', font=('Baskervill Old Face', 12)).grid(row=2,sticky=W)
    Entry(login_screen, textvariable=temp_login_account).grid(row=2, column=0, sticky=E)

    Label(login_screen, text="Password:",bg='black',fg='white', font=('Baskervill Old Face',12)).grid(row=3,pady=10,sticky=W)
    Entry(login_screen, textvariable=temp_login_password,show="*").grid(row=3, column=0,pady=10,sticky=E)
    Button(login_screen, text="Forgot password",bg='black',border=0,fg='gray',cursor="hand2",command=forgot_password,font=('Baskervill Old Face',12)).grid(row=4, column=0,sticky=E)
    login_notif=Label(login_screen,bg='black',fg='white', font=('Baskervill Old Face',12))
    login_notif.grid(row=5,sticky=N)
    Button(login_screen,text="Login",bg='black',fg='white', command=dashboard,cursor="hand2", width=15,font=("Baskervill Old Face", 12)).grid(row=6,sticky=W,padx=50,pady=10)

def forgot_password():
    login_screen.destroy()
    global temp_username
    global temp_new_password
    global pass_notif
    global forgot_password_screen
    temp_username=StringVar()
    temp_new_password=StringVar()

    forgot_password_screen=Toplevel(bank_Window)
    forgot_password_screen.title('Reset Password')
    forgot_password_screen.configure(bg='black',pady=20, padx=30)
    forgot_password_screen.grab_set()
    forgot_password_screen.geometry('300x550')

    Label(forgot_password_screen, text="Reset your password", bg='black',fg='white',
          font=('Baskervill Old Face',16, 'bold')).grid(row=1,sticky=N,pady=40,padx=20)
    Label(forgot_password_screen, text="Account No:",bg='black',fg='white', font=('Baskervill Old Face', 12)).grid(row=2,sticky=W)
    Entry(forgot_password_screen, textvariable=temp_username).grid(row=2, column=0, sticky=E)

    Label(forgot_password_screen, text="New Password:",bg='black',fg='white', font=('Baskervill Old Face',12)).grid(row=3,pady=10,sticky=W)
    Entry(forgot_password_screen, textvariable=temp_new_password,show="*").grid(row=3, column=0,pady=10,sticky=E)
    
    pass_notif=Label(forgot_password_screen,bg='black',fg='white', font=('Baskervill Old Face',12))
    pass_notif.grid(row=5,sticky=N)
    generatorButton = Button(forgot_password_screen, text="Generate", bg="black",
                             fg="white", cursor="hand2", command=passGen, font=("Arial", 12))
    generatorButton.grid(row=6, sticky=W, padx=10, pady=5)

    Button(forgot_password_screen,text="Reset", command=reset_session,cursor="hand2", width=10,fg='white' ,bg="black",font=("Baskervill Old Face", 12)).grid(row=6,sticky=E,padx=10,pady=10)


def reset_session():
    global username

    username = temp_username.get()
    new_password = temp_new_password.get()

    if username == "":
        pass_notif.config(fg='red', text="Enter valid account number")
        return

    if new_password == "":
        pass_notif.config(fg='red', text="Enter new password")
        return

    with open('Login Database.txt', 'r+') as file:
        file_data = file.read()
        details = file_data.split('\n')

        my_account = details[1]

        if username == my_account:
            # current_password = details[3]
            updated_password = new_password
            my_account = details[1]
            file_data = file_data.replace(details[3], updated_password)

            file.seek(0)
            file.truncate(0)
            file.write(file_data)

            pass_notif.config(fg='green', text="Password successfully changed")
            forgot_password_screen.destroy()
            login()
            messagebox.showinfo(title="Password Reset", message=("\nYOUR PASSWORD WAS SUCCESSFULLY RESET!!! \n\n"))
        else:
            pass_notif.config(fg='red', text="Account number does not exist")

    

#image
img= Image.open('Media/United_Bank.png')
img = img.resize((200,150))
img= ImageTk.PhotoImage(img)


login_img= Image.open('Media/mastercard-.png')
login_img = login_img.resize((220,120))
login_img= ImageTk.PhotoImage(login_img)


login_img_info= Image.open('Media/unitedbank2x_.png')
login_img_info = login_img_info.resize((150,150))
login_img_info= ImageTk.PhotoImage(login_img_info)


reg_img= Image.open('Media/carte-de-debit-removebg-.png')
reg_img = reg_img.resize((250,150))
reg_img= ImageTk.PhotoImage(reg_img)

details_img= Image.open('Media/UBA-Daily.png')
details_img = details_img.resize((70,50))
details_img= ImageTk.PhotoImage(details_img)

deposit_img= Image.open('Media/United_Bank.png')
deposit_img = deposit_img.resize((80,60))
deposit_img= ImageTk.PhotoImage(deposit_img)

withdraw_img= Image.open('Media/United_Bank.png')
withdraw_img = withdraw_img.resize((70,50))
withdraw_img= ImageTk.PhotoImage(withdraw_img)


details_img_bottom= Image.open('Media/pngtree-bank-icon.png')
details_img_bottom = details_img_bottom.resize((70,50))
details_img_bottom= ImageTk.PhotoImage(details_img_bottom)

# Label(master, text="UNITED BANK FOR AFRICA", font=('Arial Black', 15,'bold'),bg='maroon',fg='white').grid(row=0,sticky=N)
Label(bank_Window, text="Enterprise, Execution and Excellence",bg='black',fg='white', font=('Bell MT', 13, 'italic','bold')).grid(row=7,sticky=W,pady=75, padx=40)
Label (bank_Window, image=img, borderwidth=0,bg='black', width=250, ).grid(row=0,sticky=N,pady=10, padx=50)
Label(text="", bg='black').grid(row=3)
Label(text="", bg='black').grid(row=4,pady=10)

Button(bank_Window, text="Sign up",cursor="hand2",bg='#111111',fg='white', font=('Baskervill Old Face', 12),width=10,command=register).grid(row=5,sticky=N,pady=10)
Button(bank_Window, text="Login", bg='#111111',fg='white',font=('Baskervill Old Face', 12),cursor="hand2" ,width=10,command=login).grid(row=6,sticky=N, pady=10)
   
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------



bank_Window.mainloop()

