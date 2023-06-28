# created by: yashar zavary rezaie
"""
    developer = yashar zavary rezaie
    voice recognition:
    system will recognize voice and answer specific answer to the User 
    it will check words in the sentence of the user and select primary words and get specific answer
    we use tkinter in this project and database for save all data of the users
    get the voice and analize it with some python libraries like wave
"""
from tkinter import *
from tkinter import messagebox
import pyautogui
from re import search
from MySQLdb import Connect, Error
import speech_recognition as sr
import pyaudio

# my main root
mainRoot=Tk()
# size of the main root 
w=1000
h=1000
# sizing the window page
screenW=mainRoot.winfo_screenwidth()
screenh=mainRoot.winfo_screenheight()
x=(screenW/2) - (w/2)
y=(screenh/2) - (h/2)

# set geometry of main root and set resize False
mainRoot.geometry('%dx%d+%d+%d'%(w, h, x, y))
mainRoot.resizable(width=False, height=False)

# set title and icon of the product
mainRoot.title('sadoos')
mainRoot.iconbitmap('icons\mainRoot.ico')

# my welcome message
welcomeLabel=Label(master=mainRoot, 
                   text='Welcome to Sadoos\n', fg='black')
welcomeLabel.pack()

# my name block frame
nameFrame=Frame(master=mainRoot)
nameFrame.pack(side='top')

# my name label for fist block
nameLabel=Label(master=nameFrame, text='User name: ', fg='#5551c9')
nameLabel.pack(side='left')

# name Entry
nameEntry=Entry(master=nameFrame)
nameEntry.pack(side='right')

# password frame
passFrame=Frame(master=mainRoot)
passFrame.pack(side='top')

# password Label
passLabel=Label(master=passFrame, text='Password:   ', fg='#5551c9')
passLabel.pack(side='left')

# password entry block
passEntry=Entry(master=passFrame)
passEntry.pack(side='right')
 
# my control and sign in part (main program goes here)
def singIn(event):
    # my speak and answer
    def mainMenu():
        def speak(event):
            agent=sr.Recognizer()
            try:      
                with sr.Microphone() as source:
                    agent.pause_threshold=1
                    audio=agent.listen(source)
                    text=agent.recognize_google(audio, language='fa-IR')  
            except Exception as err:
                messagebox.showerror('Error', 'speech analize have problem, please try again in silent place')
                print(err)
            else:
                writeLabel.config(text=text)
                
                            
        mainMenuRoot=Tk()
        mainMenuRoot.title('workPlace')
        w=600
        h=600
        x=(screenW/2) - (w/2)
        y=(screenh/2) - (h/2)
        mainMenuRoot.geometry('%dx%d+%d+%d'%(w,h,x,y))
        mainMenuRoot.resizable(width=False, height=False)
        
        writeFrame=Frame(master=mainMenuRoot, width=600, height=50, bg='#C0C0C0')
        writeFrame.pack(side='bottom')          
        writeFrame.pack_propagate(0)
        
        writeLabel=Label(master=writeFrame,text="", bg='#C0C0C0')
        writeLabel.pack(side='left')
        
        collectButton=Button(master=writeFrame, text='speak')
        collectButton.bind('<Button>', speak)
        collectButton.pack(side='right')


        
        mainMenuRoot.mainloop()
    # get username and password to sign in
    inputUserName=nameEntry.get()
    inputPassword=passEntry.get()
    # control that name and password isn't empty
    if inputUserName=="" or inputPassword=="":
        messagebox.showerror('Error', 'blocks can\'t be empty')
    else:
        try:
            with Connect(password='Yasharzavary360', user="root", database='sadoos', host='127.0.0.11') as conn:
                # set the cursor
                databaseAgent=conn.cursor()
                # if username and password be true, change this variable
                itIsTrue=False
                databaseAgent.execute('select userName, userPassword from sadoosUser')
                # read each person data
                for person in databaseAgent:
                    # control the name and password
                    if person[0]==inputUserName and person[1]==inputPassword:
                        itIsTrue=True      
        # if we have server error
        except Error as err:
            messagebox.showerror('server error', 'we can\'t connect to server now')
            print(err)
        else:
            if itIsTrue:
                #  main menu of program
                mainMenu()
            else:
                messagebox.showerror('Error', 'password or username is incorrect')
        
# my sign in button with in and out changing color
signInbutton=Button(master=mainRoot, text='sign in', bg='#f9f6e9')
signInbutton.bind('<Enter>', lambda event: signInbutton.config(bg='#c4f53a'))
signInbutton.bind('<Leave>', lambda event: signInbutton.config(bg='#f9f6e9'))
signInbutton.bind('<Button>', singIn)
signInbutton.pack()

# exit button
exitButton=Button(master=mainRoot, text=' Exit ', bg='#f9f6e9')
exitButton.bind('<Enter>', lambda event: exitButton.config(bg='#c4f53a'))
exitButton.bind('<Leave>', lambda event: exitButton.config(bg='#f9f6e9'))
exitButton.bind('<Button>', lambda event: mainRoot.destroy())
exitButton.pack()


# copy right frame
copyrightFrame=Frame(master=mainRoot, bg='#6186fa', width=1000, height=40)
copyrightFrame.pack(side='bottom')
copyrightFrame.pack_propagate(0)

# my upfactor copy right label
copyrightLabel=Label(master=copyrightFrame, text='copyright@2023 upfactor', bg='#6186fa')
copyrightLabel.pack(side='right')

# sign up frame
signUpFrame=Frame(master=mainRoot, width=1000, height=60)
signUpFrame.pack(side='bottom')
signUpFrame.pack_propagate(0)

# label for sing up part
singUpLabel=Label(master=signUpFrame, text='you don\'t have a account?')
singUpLabel.pack(side='left')

# my sign up control and save part
def singUp(event):
    def control(event):
        # get data from blocks
        fullName=sNameEntry.get()
        userName=uNameEntry.get()
        password=passEntry.get()
        cellPhone=cellEntry.get()
        
        
        # control part
        if fullName == "" or userName=="" or password=="" or cellPhone=="":
            messagebox.showerror('Error', 'blocks can\'t be empty')
        elif search(r'\d', fullName):
            messagebox.showerror('Error', 'full name can\'t have number in')
        elif len(password) <8:
            messagebox.showerror('Error', 'password must be at least 8 characters')
        elif not search(r'\w', password):
            messagebox.showerror('Error', 'password must have A-Z symbols')
        elif not search(r'[!@#$%^&*]', password):
            messagebox.showerror('Error', 'password must have at least one @#!$%^&*')
        elif len(cellPhone) != 10 or search(r'[^0-9]', cellPhone):
            messagebox.showerror('Error', 'cell phone is invalid')
        else:
            try:
                # data base connection
                with Connect(host='127.0.0.11', password='Yasharzavary360', user="root", database='sadoos') as conn:
                    # cursor the database
                    databaseCursor=conn.cursor()
                    # select name and pass from database
                    databaseCursor.execute('select fullName,cellPhoneNumber,userName from sadoosUser')
                    # one variable for set that we found similar person or not
                    cantFound=True
                    # loop on the database and get data
                    for data in databaseCursor:
                        # if found the cellphone number
                        if cellPhone==data[1]:
                            messagebox.showerror('Error', 'this cellphone have account')
                            cantFound=False
                            break
                        # if found the user name 
                        elif userName==data[2]:
                            cantFound=False
                            messagebox.showerror('Error', 'this user name have a account')
                            break
                    # if we don't have that username, we add it to the database
                    if cantFound:
                        # select max number of primary key in database
                        databaseCursor.execute('select max(userCode) from sadoosUser')
                        # get the max ID
                        for code in databaseCursor:
                            maxId=code
                        # make person tuple for adding to the database
                        person=(maxId[0]+1, fullName, userName, str(cellPhone), str(password))
                        # adding part
                        databaseCursor.execute('''insert into sadoosUser(userCode, fullName, userName, cellPhoneNumber, userPassword)
                                                   values(%s,%s,%s,%s,%s)''', person)           
                        messagebox.showinfo('sign up', 'you sign up in sadoos!')              
                    conn.commit()
            # if one error happend we can except it
            except Error as err:
                messagebox.showerror('Error', 'we can\'t acces to server now')
                print(err)
        
    # my sign up root
    singUpRoot=Tk()
    
    # set geometry of main root and set resize False
    singUpRoot.geometry('%dx%d+%d+%d'%(700,500, 2500, 1000))
    singUpRoot.resizable(width=False, height=False)

    # set title and icon of the product
    singUpRoot.title('sign up to sadoos')
    singUpRoot.iconbitmap('icons\signUpRoot.ico')
    
    welcomeLabel=Label(master=singUpRoot, text='hi! please fill the blocks to sing up')
    welcomeLabel.pack(side='top')
    
    # full name block frame
    sNameFrame=Frame(master=singUpRoot)
    sNameFrame.pack(side='top')

    # full name label for fist block
    sNameLabel=Label(master=sNameFrame, text='full name: ', fg='#5551c9')
    sNameLabel.pack(side='left')

    # full name Entry
    sNameEntry=Entry(master=sNameFrame)
    sNameEntry.pack(side='right')
    
     # user name block frame
    uNameFrame=Frame(master=singUpRoot)
    uNameFrame.pack(side='top')

    # user name label for fist block
    uNameLabel=Label(master=uNameFrame, text='user name:', fg='#5551c9')
    uNameLabel.pack(side='left')

    # user name Entry
    uNameEntry=Entry(master=uNameFrame)
    uNameEntry.pack(side='right')
    
     # password block frame
    passFrame=Frame(master=singUpRoot)
    passFrame.pack(side='top')

    # password label for fist block
    passLabel=Label(master=passFrame, text='password: ', fg='#5551c9')
    passLabel.pack(side='left')

    # password Entry
    passEntry=Entry(master=passFrame)
    passEntry.pack(side='right')
    
    # cellPhone block frame
    cellFrame=Frame(master=singUpRoot)
    cellFrame.pack(side='top')

    # cellPhone label for fist block
    cellLabel=Label(master=cellFrame, text='cell phone number: +98', fg='#5551c9')
    cellLabel.pack(side='left')

    # cellPhone Entry
    cellEntry=Entry(master=cellFrame)
    cellEntry.pack(side='right')
    
    signUpButton=Button(master=singUpRoot, text='sign up', bg='#f9f6e9')
    signUpButton.bind('<Enter>', lambda event: signUpButton.config(bg='#c4f53a'))
    signUpButton.bind('<Leave>', lambda event: signUpButton.config(bg='#f9f6e9'))
    signUpButton.bind('<Button>', control)
    signUpButton.pack()
    
    singUpRoot.mainloop()
    
# sign up button part
signUpbutton=Button(master=signUpFrame, text='sign up', bg='#f9f6e9')
signUpbutton.bind('<Enter>', lambda event: signUpbutton.config(bg='#c4f53a'))
signUpbutton.bind('<Leave>', lambda event: signUpbutton.config(bg='#f9f6e9'))
signUpbutton.bind('<Button>', singUp)
signUpbutton.pack(side='left')


mainRoot.mainloop()
