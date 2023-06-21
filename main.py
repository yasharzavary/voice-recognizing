# created by: yashar zavary rezaie
"""
    voice recognition:
    system will recognize voice and answer specific answer to the User 
    it will check words in the sentence of the user and select primary words and get specific answer
    
"""
from tkinter import *

# my main root
mainRoot=Tk()
# size of the main root 
w=500
h=500
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



mainRoot.mainloop()

