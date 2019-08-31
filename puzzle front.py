import tkinter
from tkinter import *
from tkinter import font
import os
'''
import vlc

p = vlc.MediaPlayer("Sound.mp3")
p.play()
'''
from pygame import mixer
mixer.init()
p = mixer.music.load('Puzzlemusic.mp3')
mixer.music.play(-1)



createPlayerOn = alreadyPlayerOn = 0
currentPlayer = 'rrr'

playersList = ['Gaurav', 'Aman', 'Akash', 'Ishaan', 'Ravinder', 'GNIT', 'CDAC', 'Python', 'Coder']


def oneselect(evt):
    global f, welcomePlayerLabel, choosePlayerLabel, alreadyPlayerOn, playbutton
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    # print('You selected item %d: "%s"' % (index, value))
    f.place_forget()
    choosePlayerLabel.place_forget()
    welcomePlayerLabel['text'] = "Welcome  " + value
    welcomePlayerLabel.place(x=350, y=7)
    alreadyPlayerOn = 0
    playbutton['state'] = tkinter.NORMAL


def getcurrentPlayer():
    global createPlayerOn, currentPlayer,playbutton, welcomePlayerLabel, playersList, playersListbox
    currentPlayer = var.get()
    playersList.append(currentPlayer)
    playersListbox.insert(END, currentPlayer)
    createPlayerOn = 0
    playbutton['state'] = tkinter.NORMAL
    # print(playersList)
    newPlayerEntry.place_forget()
    newPlayerLabel.place_forget()
    doneButton.place_forget()
    welcomePlayerLabel['text'] = "Welcome  " + str(currentPlayer)
    welcomePlayerLabel.place(x=350, y=7)


def createPlayer():
    global createPlayerOn, newPlayerEntry, newPlayerLabel, playbutton, playersList, doneButton, var, welcomePlayerLabel, alreadyPlayerOn, f, choosePlayerLabel
    alreadyPlayerOn = 0
    playbutton['state'] = tkinter.DISABLED
    f.place_forget()
    choosePlayerLabel.place_forget()

    max_len = 15

    def on_write(*args):
        s = var.get()
        if len(s) > max_len:
            var.set(s[:max_len])

    var.trace_variable("w", on_write)

    if createPlayerOn == 0:
        welcomePlayerLabel.place_forget()
        createPlayerOn = 1
        newPlayerLabel.place(x=7, y=7)
        newPlayerEntry.place(x=320, y=9)
        doneButton.place(x=520, y=7)

    elif createPlayerOn == 1:
        newPlayerEntry.place_forget()
        newPlayerLabel.place_forget()
        doneButton.place_forget()

        newPlayerLabel.place(x=7, y=7)
        newPlayerEntry.place(x=320, y=9)
        doneButton.place(x=520, y=7)


def anonymousPlayer():
    global createPlayerOn, newPlayerEntry, newPlayerLabel,playbutton, doneButton, welcomePlayerLabel, playersList, f, choosePlayerLabel, alreadyPlayerOn
    welcomePlayerLabel.place_forget()
    newPlayerEntry.place_forget()
    newPlayerLabel.place_forget()
    doneButton.place_forget()
    f.place_forget()
    choosePlayerLabel.place_forget()

    createPlayerOn = 0
    alreadyPlayerOn = 0
    playbutton['state'] = tkinter.NORMAL


def alreadyPlayer():
    global createPlayerOn, newPlayerEntry, newPlayerLabel,playbutton, playersList, doneButton, welcomePlayerLabel, choosePlayerLabel, f, playersListbox, alreadyPlayerOn
    alreadyPlayerOn = 1
    playbutton['state'] = tkinter.DISABLED
    if createPlayerOn == 1:
        newPlayerEntry.place_forget()
        newPlayerLabel.place_forget()
        doneButton.place_forget()
        createPlayerOn = 0

    elif createPlayerOn == 0:
        welcomePlayerLabel.place_forget()

    choosePlayerLabel.place(x=685, y=210)
    f.place(x=720, y=272)


def gamechoice():
    #mixer.music.fadeout(1000)
    if str(var1.get()) == '1':
        os.system('python "3x3cheat.py"')
    elif str(var1.get()) == '2':
        os.system('python "4x4cheat.py"')
    elif str(var1.get()) == '3':
        os.system('python "5x5cheat.py"')


root = Tk()
root.title("Sustainable (Unshuffle v 2.1)")
root.minsize(1004, 429)
root.resizable(False, False)
logo = PhotoImage(file="a3.png")
bglabel = Label(root, image=logo).place(x=0, y=0)

# ======================================================================================================

chooselevel = Label(bglabel, text="CHOOSE LEVEL", bg='#e4833b', relief="solid", font=('Gabriola', 22, font.BOLD),
                    height=0, width=20)
chooselevel.place(x=685, y=210)

var1 = IntVar(None, 1)
r1 = Radiobutton(bglabel, text="  Easy   ", variable=var1, value=1, bg='#f77575',
                 font=('Franklin Gothic Book', 15, font.BOLD), relief="solid", height=0, width=10)
r1.place(x=750, y=272)

r2 = Radiobutton(bglabel, text="Medium", variable=var1, value=2, bg='#e13737',
                 font=('Franklin Gothic Book', 15, font.BOLD), relief="solid", height=0, width=10)
r2.place(x=750, y=307)

r3 = Radiobutton(bglabel, text="Difficult", variable=var1, value=3, bg='#bf1b1b',
                 font=('Franklin Gothic Book', 15, font.BOLD), relief="solid", height=0, width=10)
r3.place(x=750, y=342)

# ======================================================================================================


playas = Label(bglabel, text="PLAY AS", bg='#e4833b', relief="solid", font=('Gabriola', 22, font.BOLD),
               height=0, width=20)
playas.place(x=45, y=210)

var2 = IntVar(None, 1)
a1 = Radiobutton(bglabel, command=anonymousPlayer, text="   Anonymous    ", variable=var2, value=1, bg='#f77575',
                 font=('Franklin Gothic Book', 15, font.BOLD), relief="solid", height=0, width=15)
a1.place(x=80, y=272)

a2 = Radiobutton(bglabel, command=alreadyPlayer, text="Already a Player", variable=var2, value=2, bg='#e13737',
                 font=('Franklin Gothic Book', 15, font.BOLD), relief="solid", height=0, width=15)
a2.place(x=80, y=307)

a3 = Radiobutton(bglabel, command=createPlayer, text="   New Player     ", variable=var2, value=3, bg='#bf1b1b',
                 font=('Franklin Gothic Book', 15, font.BOLD), relief="solid", height=0, width=15)
a3.place(x=80, y=342)

# ======================================================================================================


playbutton = Button(bglabel, text="PLAY", font=('Forte', 28, font.BOLD), height=0, width=10, bg="#229954",
                    relief="solid", command=gamechoice)
playbutton.place(x=395, y=332)

newPlayerLabel = Label(bglabel, text="  Welcome New Player!! Enter Your Name : ", bg='#cbc571', relief="solid",
                       font=('Gabriola', 15, font.BOLD), height=0, width=55, anchor="w")

var = StringVar()
newPlayerEntry = Entry(bglabel, bg='#cbc571', textvariable=var, font=('Gabriola', 14, font.BOLD), fg='#15296a',
                       width=20, selectborderwidth=0, relief="flat")

doneButton = Button(root, text='Done', font=('Georgia', 15), bg='#27b5e3', command=getcurrentPlayer, height=0, width=5,
                    relief='solid')

welcomePlayerLabel = Label(bglabel, bg='#f16d6d', relief="solid", font=('Gabriola', 18, font.BOLD),
                           height=0, width=30)

choosePlayerLabel = Label(root, text="Choose Your Name", bg='#27b5e3', relief="solid",
                          font=('Gabriola', 22, font.BOLD), height=0, width=20)

f = Frame(root)
playersListbox = Listbox(f, width=20, height=7, bg='#27b5e3', relief="solid", bd=2, font=('Courier New Baltic', 12),
                         justify=CENTER)
playersListbox.pack(side=LEFT)
scrollbar = Scrollbar(f, command=playersListbox.yview)
scrollbar.pack(side=RIGHT, fill="y")
playersListbox.config(yscrollcommand=scrollbar.set)
for i in playersList:
    playersListbox.insert(END, str(i))
playersListbox.bind("<Double-1>", oneselect)

mainloop()

'''
#aeb6bf
#5d6d7e
#34495e
'''
