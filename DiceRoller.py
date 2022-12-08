#Blake Matteson 12.8.2022
#Purpose: Just a simple little gui Dice Roller with a textbox to write temporary notes in. 
#Plenty of stuff that does this and better online. 
#Wanted To Get Some Experience in some "lite" GUI work. 



import random
from tkinter import *

def roll1():
    # Roll the dice
    dice1 = random.randint(1, 6)
    label1["text"] = str(dice1)
def roll2():
    dice2 = random.randint(1, 20)
    label2["text"] = str(dice2)
def roll3():
    dice3 = random.randint(1,12)
    label3["text"] = str(dice3)

    
root = Tk()
root.title("Dice Roller")

label1 = Label(root, text="0", font=("Comic Sans", 112))
label1.grid(row=0, column=1, sticky=N+S+E+W)

label2 = Label(root, text="0", font=("Comic Sans", 112))
label2.grid(row=2, column=1, sticky=N+S+E+W)

label3 = Label(root, text="0", font=("Comic Sans", 112))
label3.grid(row=0, column=3, sticky=N+S+E+W)

button3 = Button(root, text="Roll D12", command=roll3)
button3.grid(row=1, column=3, columnspan=2, sticky=N+S+E+W)

button2 = Button(root, text="Roll D20", command=roll2)
button2.grid(row=3, column=0, columnspan=2, sticky=N+S+E+W)

button = Button(root, text="Roll D6", command=roll1)
button.grid(row=1, column=0, columnspan=2, sticky=N+S+E+W)

T = Text(root, height=5, width = 20,)
T.grid(row=1,column=2, sticky=N+S+E+W)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)


root.mainloop()
