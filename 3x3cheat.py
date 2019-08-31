import tkinter
from tkinter import *
from tkinter import font
from tkinter import messagebox
import time
import random

listt = []
for i in range(1, 9):
    listt.append(i)
listt.append('')

clicks = 0
win = 0


def presenttime():
    global time1
    time1 = time.time()


def tick():
    global time1, win, time3
    if win == 1:
        print("Time Taken = ", time3)
    else:
        time2 = time.time()
        time3 = time.strftime('%H:%M:%S', time.gmtime(time2 - time1))
        clock.config(text=time3)
        clock.after(200, tick)


def showclicks():
    global clicks
    clicks += 1
    e1['text'] = 'Clicks : ' + str(clicks)


def cheater(a,e):
    if b2['text'] == a:
        b2['text'] = e
    elif b3['text'] == a:
        b3['text'] = e
    elif b4['text'] == a:
        b4['text'] = e
    elif b5['text'] == a:
        b5['text'] = e
    elif b6['text'] == a:
        b6['text'] = e
    elif b7['text'] == a:
        b7['text'] = e
    elif b8['text'] == a:
        b8['text'] = e
    elif b9['text'] == a:
        b9['text'] = e



def cheat_activated():
    if b1['text'] == 1 and b2['text'] == 2 and b3['text'] == 3 and b4['text'] == 4 and b5['text'] == 5 and b6[
        'text'] == 6 and b7['text'] == 7 and b8['text'] == 8 and b9['text'] == '':
        startbutton['text'] = 'Shuffle\nAgain'
        startbutton['width'] = 9
        b1['command'] = f1
        b2['command'] = f2
        b3['command'] = f3
        b4['command'] = f4
        b5['command'] = f5
        b6['command'] = f6
        b7['command'] = f7
        b8['command'] = f8
        b9['command'] = f9
        startbutton['command'] = randomize
        checkwin()
    else:
        a=1
        if b1['text'] == a:
            a=2
            if b2['text'] == a:
                a=3
                if b3['text'] == a:
                    a = 4
                    if b4['text'] == a:
                        a =5
                        if b5['text'] == a:
                            a =6
                            if b6['text'] == a:
                                a =7
                                if b7['text'] == a:
                                    a =8
                                    if b8['text'] == a:
                                        pass
                                    else:
                                        e = b8['text']
                                        cheater(a, e)
                                        b8['text'] = a
                                else:
                                    e = b7['text']
                                    cheater(a, e)
                                    b7['text'] = a
                            else:
                                e = b6['text']
                                cheater(a, e)
                                b6['text'] = a
                        else:
                            e = b5['text']
                            cheater(a, e)
                            b5['text'] = a
                    else:
                        e = b4['text']
                        cheater(a, e)
                        b4['text'] = a
                else:
                    e = b3['text']
                    cheater(a, e)
                    b3['text'] = a
            else:
                e = b2['text']
                cheater(a, e)
                b2['text'] = a
        else:
            e = b1['text']
            cheater(a,e)
            b1['text'] = a


        clock.after(1500, cheat_activated)




i = 0


def check_cheat(event):
    global i
    # print ("pressed", event.char)
    if event.char == 'g' and startbutton['text'] == 'Shuffle\nAgain':
        i = 1
    elif event.char == 'a' and i == 1:
        i = 2
    elif event.char == 'u' and i == 2:
        i = 3
    elif event.char == 'r' and i == 3:
        i = 4
    elif event.char == 'a' and i == 4:
        i = 5
    elif event.char == 'v' and i == 5:
        print("Gaurav's Cheat Activated")
        b1['command'] = b2['command'] = b3['command'] = b4['command'] = b5['command'] = b6['command'] = b7['command'] = \
        b8['command'] = b9['command'] = startbutton['command'] = NONE
        startbutton['text'] = 'Cheat\nActivated'
        startbutton['width'] = 9
        cheat_activated()
    else:
        i = 0


def checkwin():
    if b1['text'] == 1 and b2['text'] == 2 and b3['text'] == 3 and b4['text'] == 4 and b5['text'] == 5 and b6[
        'text'] == 6 and b7['text'] == 7 and b8['text'] == 8 and b9['text'] == '':
        global win, clicks
        print("You win\nClicks : ", clicks)
        win = 1
        b1['state'] = b2['state'] = b3['state'] = b4['state'] = b5['state'] = b6['state'] = b7['state'] = b8['state'] = \
            b9['state'] = tkinter.DISABLED


def randomize():
    global clicks, listt, win
    if startbutton['text'] == 'Start Game':
        presenttime()
        tick()
        clicks = 0
        e1['text'] = 'Clicks : ' + str(clicks)
        startbutton['text'] = 'Shuffle\nAgain'
        startbutton['width'] = 9
        b1['state'] = b2['state'] = b3['state'] = b4['state'] = b5['state'] = b6['state'] = b7['state'] = b8['state'] = \
        b9['state'] = tkinter.NORMAL
        random.shuffle(listt)
        #print(listt)
        # listt = [1, 2, 3, 4, 5, 6, 7, '', 8]
        b1['text'] = listt[0]
        b2['text'] = listt[1]
        b3['text'] = listt[2]
        b4['text'] = listt[3]
        b5['text'] = listt[4]
        b6['text'] = listt[5]
        b7['text'] = listt[6]
        b8['text'] = listt[7]
        b9['text'] = listt[8]

    elif startbutton['text'] == 'Shuffle\nAgain':
        restart = messagebox.askquestion("Restart", "Wanna Quit this Game  &  Start a New One?", icon='warning')
        if restart == 'yes':
            win = 0
            presenttime()
            tick()
            clicks = 0
            b1['state'] = b2['state'] = b3['state'] = b4['state'] = b5['state'] = b6['state'] = b7['state'] = b8[
                'state'] = b9['state'] = tkinter.NORMAL

            e1['text'] = 'Clicks : ' + str(clicks)
            random.shuffle(listt)
            #print(listt)
            # listt=[1, 2, 3, 4, 5, 6, 7, '', 8]
            b1['text'] = listt[0]
            b2['text'] = listt[1]
            b3['text'] = listt[2]
            b4['text'] = listt[3]
            b5['text'] = listt[4]
            b6['text'] = listt[5]
            b7['text'] = listt[6]
            b8['text'] = listt[7]
            b9['text'] = listt[8]
        else:
            pass


root = Tk()
root.title("Level Easy")
root.resizable(False, False)


def f1():
    showclicks()
    if b2['text'] == '':
        b1['text'], b2['text'] = b2['text'], b1['text']
    elif b4['text'] == '':
        b1['text'], b4['text'] = b4['text'], b1['text']


def f2():
    showclicks()
    if b1['text'] == '':
        b2['text'], b1['text'] = b1['text'], b2['text']
    elif b3['text'] == '':
        b2['text'], b3['text'] = b3['text'], b2['text']
    elif b5['text'] == '':
        b2['text'], b5['text'] = b5['text'], b2['text']


def f3():
    showclicks()
    if b2['text'] == '':
        b3['text'], b2['text'] = b2['text'], b3['text']
    elif b6['text'] == '':
        b3['text'], b6['text'] = b6['text'], b3['text']


def f4():
    showclicks()
    if b1['text'] == '':
        b4['text'], b1['text'] = b1['text'], b4['text']
    elif b5['text'] == '':
        b4['text'], b5['text'] = b5['text'], b4['text']
    elif b7['text'] == '':
        b4['text'], b7['text'] = b7['text'], b4['text']


def f5():
    showclicks()
    if b2['text'] == '':
        b5['text'], b2['text'] = b2['text'], b5['text']
    elif b4['text'] == '':
        b5['text'], b4['text'] = b4['text'], b5['text']
    elif b6['text'] == '':
        b5['text'], b6['text'] = b6['text'], b5['text']
    elif b8['text'] == '':
        b5['text'], b8['text'] = b8['text'], b5['text']


def f6():
    showclicks()
    if b3['text'] == '':
        b6['text'], b3['text'] = b3['text'], b6['text']
    elif b5['text'] == '':
        b6['text'], b5['text'] = b5['text'], b6['text']
    elif b9['text'] == '':
        b6['text'], b9['text'] = b9['text'], b6['text']


def f7():
    showclicks()
    if b8['text'] == '':
        b7['text'], b8['text'] = b8['text'], b7['text']
    elif b4['text'] == '':
        b7['text'], b4['text'] = b4['text'], b7['text']


def f8():
    showclicks()
    if b7['text'] == '':
        b8['text'], b7['text'] = b7['text'], b8['text']
    elif b5['text'] == '':
        b8['text'], b5['text'] = b5['text'], b8['text']
    elif b9['text'] == '':
        b8['text'], b9['text'] = b9['text'], b8['text']


def f9():
    showclicks()
    if b8['text'] == '':
        b9['text'], b8['text'] = b8['text'], b9['text']
    elif b6['text'] == '':
        b9['text'], b6['text'] = b6['text'], b9['text']
    checkwin()


clock = Label(root, font=('times', 20, 'bold'), bg='#b03a2e', height=2, width=7, bd=7, relief='g')
b1 = Button(root, text=listt[0], command=f1, height=1, width=3, bd=7, relief='g', state=tkinter.DISABLED)
b2 = Button(root, text=listt[1], command=f2, height=1, width=3, bd=7, relief='g', state=tkinter.DISABLED)
b3 = Button(root, text=listt[2], command=f3, height=1, width=3, bd=7, relief='g', state=tkinter.DISABLED)
b4 = Button(root, text=listt[3], command=f4, height=1, width=3, bd=7, relief='g', state=tkinter.DISABLED)
b5 = Button(root, text=listt[4], command=f5, height=1, width=3, bd=7, relief='g', state=tkinter.DISABLED)
b6 = Button(root, text=listt[5], command=f6, height=1, width=3, bd=7, relief='g', state=tkinter.DISABLED)
b7 = Button(root, text=listt[6], command=f7, height=1, width=3, bd=7, relief='g', state=tkinter.DISABLED)
b8 = Button(root, text=listt[7], command=f8, height=1, width=3, bd=7, relief='g', state=tkinter.DISABLED)
b9 = Button(root, text=listt[8], command=f9, height=1, width=3, bd=7, relief='g', state=tkinter.DISABLED)
startbutton = Button(root, text='Start Game', font=('Georgia', 15), command=randomize, height=2, bd=7, relief='g')
e1 = Label(root, text='Clicks :  0', font=('Georgia', 13), height=3, width=11, bd=7, relief='g', bg='#b03a2e')
b1['bg'] = b2['bg'] = b3['bg'] = b4['bg'] = b5['bg'] = b6['bg'] = b7['bg'] = b8['bg'] = b9['bg'] = startbutton[
    'bg'] = '#d2a26b'
b1['font'] = b2['font'] = b3['font'] = b4['font'] = b5['font'] = b6['font'] = b7['font'] = b8['font'] = b9['font'] = (
'Georgia', 40, font.BOLD)

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)
startbutton.grid(row=3, column=1)
e1.grid(row=3, column=2)
clock.grid(row=3, column=0)
root.bind("<Key>", check_cheat)

mainloop()

'''
working random lists
[4, 7, 8, '', 2, 5, 1, 3, 6]
[6, 7, 3, 2, '', 1, 5, 4, 8]
[7, 2, 5, 8, '', 6, 3, 1, 4]
[4, 3, 2, 7, '', 5, 8, 1, 6]
[6, 2, '', 4, 8, 5, 1, 3, 7]
[6, '', 7, 2, 1, 3, 4, 8, 5]
[4, 6, 7, 5, 3, '', 2, 8, 1]
[4, 8, 6, 7, 5, 2, '', 3, 1]
[3, 6, 1, 4, 8, 5, '', 7, 2]
['', 3, 7, 1, 6, 5, 2, 4, 8]

#d2a26b

'''
