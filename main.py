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
import pyautogui
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
    pass 

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
    # my sign up root
    singUpRoot=Tk()
    
    # set geometry of main root and set resize False
    singUpRoot.geometry('%dx%d+%d+%d'%(700,500, 2500, 1000))
    singUpRoot.resizable(width=False, height=False)

    # set title and icon of the product
    singUpRoot.title('sign up to sadoos')
    singUpRoot.iconbitmap('icons\signUpRoot.ico')
    

    
    singUpRoot.mainloop()
    
# sign up button part
signUpbutton=Button(master=signUpFrame, text='sign up', bg='#f9f6e9')
signUpbutton.bind('<Enter>', lambda event: signUpbutton.config(bg='#c4f53a'))
signUpbutton.bind('<Leave>', lambda event: signUpbutton.config(bg='#f9f6e9'))
signUpbutton.bind('<Button>', singUp)
signUpbutton.pack(side='left')


mainRoot.mainloop()
