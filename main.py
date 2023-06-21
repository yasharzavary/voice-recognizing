# created by: yashar zavary rezaie
"""
    voice recognition:
    system will recognize voice and answer specific answer to the User 
    it will check words in the sentence of the user and select primary words and get specific answer
    
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
signInbutton=Button(master=mainRoot, text='sign in', bg='#55ccc9')
signInbutton.bind('<Enter>', lambda event: signInbutton.config(bg='#55f6c9'))
signInbutton.bind('<Leave>', lambda event: signInbutton.config(bg='#55ccc9'))
signInbutton.bind('<Button>', singIn)
signInbutton.pack()


mainRoot.mainloop()

