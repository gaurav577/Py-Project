import tkinter
from tkinter import *
from tkinter import font
from tkinter import messagebox
import time
import random

listt = []
for i in range(1, 25):
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


def cheater(a, e):
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
    elif b10['text'] == a:
        b10['text'] = e
    elif b11['text'] == a:
        b11['text'] = e
    elif b12['text'] == a:
        b12['text'] = e
    elif b13['text'] == a:
        b13['text'] = e
    elif b14['text'] == a:
        b14['text'] = e
    elif b15['text'] == a:
        b15['text'] = e
    elif b16['text'] == a:
        b16['text'] = e
    elif b17['text'] == a:
        b17['text'] = e
    elif b18['text'] == a:
        b18['text'] = e
    elif b19['text'] == a:
        b19['text'] = e
    elif b20['text'] == a:
        b20['text'] = e
    elif b21['text'] == a:
        b21['text'] = e
    elif b22['text'] == a:
        b22['text'] = e
    elif b23['text'] == a:
        b23['text'] = e
    elif b24['text'] == a:
        b24['text'] = e
    elif b25['text'] == a:
        b25['text'] = e


def cheat_activated():
    if b1['text'] == 1 and b2['text'] == 2 and b3['text'] == 3 and b4['text'] == 4 and b5['text'] == 5 \
            and b6['text'] == 6 and b7['text'] == 7 and b8['text'] == 8 and b9['text'] == 9 \
            and b10['text'] == 10 and b11['text'] == 11 and b12['text'] == 12 and b13['text'] == 13 \
            and b14['text'] == 14 and b15['text'] == 15 and b16['text'] == 16 and b17['text'] == 17 \
            and b18['text'] == 18 and b19['text'] == 19 and b20['text'] == 20 and b21['text'] == 21 \
            and b22['text'] == 22 and b23['text'] == 23 and b24['text'] == 24 and b25['text'] == '':
        startbutton['text'] = 'Shuffle\nAgain'
        startbutton['width'] = 20
        b1['command'] = f1
        b2['command'] = f2
        b3['command'] = f3
        b4['command'] = f4
        b5['command'] = f5
        b6['command'] = f6
        b7['command'] = f7
        b8['command'] = f8
        b9['command'] = f9
        b10['command'] = f10
        b11['command'] = f11
        b12['command'] = f12
        b13['command'] = f13
        b14['command'] = f14
        b15['command'] = f15
        b16['command'] = f16
        b17['command'] = f17
        b18['command'] = f18
        b19['command'] = f19
        b20['command'] = f20
        b21['command'] = f21
        b22['command'] = f22
        b23['command'] = f23
        b24['command'] = f24
        b25['command'] = f25

        startbutton['command'] = randomize
        checkwin()
    else:
        a = 1
        if b1['text'] == a:
            a = 2
            if b2['text'] == a:
                a = 3
                if b3['text'] == a:
                    a = 4
                    if b4['text'] == a:
                        a = 5
                        if b5['text'] == a:
                            a = 6
                            if b6['text'] == a:
                                a = 7
                                if b7['text'] == a:
                                    a = 8
                                    if b8['text'] == a:
                                        a = 9
                                        if b9['text'] == a:
                                            a = 10
                                            if b10['text'] == a:
                                                a = 11
                                                if b11['text'] == a:
                                                    a = 12
                                                    if b12['text'] == a:
                                                        a = 13
                                                        if b13['text'] == a:
                                                            a = 14
                                                            if b14['text'] == a:
                                                                a = 15
                                                                if b15['text'] == a:
                                                                    a = 16
                                                                    if b16['text'] == a:
                                                                        a = 17
                                                                        if b17['text'] == a:
                                                                            a = 18
                                                                            if b18['text'] == a:
                                                                                a = 19
                                                                                if b19['text'] == a:
                                                                                    a = 20
                                                                                    if b20['text'] == a:
                                                                                        a = 21
                                                                                        if b21['text'] == a:
                                                                                            a = 22
                                                                                            if b22['text'] == a:
                                                                                                a = 23
                                                                                                if b23['text'] == a:
                                                                                                    a = 24
                                                                                                    if b24['text'] == a:
                                                                                                        pass
                                                                                                    else:
                                                                                                        e = b24['text']
                                                                                                        cheater(a, e)
                                                                                                        b24['text'] = a
                                                                                                else:
                                                                                                    e = b23['text']
                                                                                                    cheater(a, e)
                                                                                                    b23['text'] = a
                                                                                            else:
                                                                                                e = b22['text']
                                                                                                cheater(a, e)
                                                                                                b22['text'] = a
                                                                                        else:
                                                                                            e = b21['text']
                                                                                            cheater(a, e)
                                                                                            b21['text'] = a
                                                                                    else:
                                                                                        e = b20['text']
                                                                                        cheater(a, e)
                                                                                        b20['text'] = a
                                                                                else:
                                                                                    e = b19['text']
                                                                                    cheater(a, e)
                                                                                    b19['text'] = a
                                                                            else:
                                                                                e = b18['text']
                                                                                cheater(a, e)
                                                                                b18['text'] = a
                                                                        else:
                                                                            e = b17['text']
                                                                            cheater(a, e)
                                                                            b17['text'] = a
                                                                    else:
                                                                        e = b16['text']
                                                                        cheater(a, e)
                                                                        b16['text'] = a
                                                                else:
                                                                    e = b15['text']
                                                                    cheater(a, e)
                                                                    b15['text'] = a
                                                            else:
                                                                e = b14['text']
                                                                cheater(a, e)
                                                                b14['text'] = a
                                                        else:
                                                            e = b13['text']
                                                            cheater(a, e)
                                                            b13['text'] = a
                                                    else:
                                                        e = b12['text']
                                                        cheater(a, e)
                                                        b12['text'] = a
                                                else:
                                                    e = b11['text']
                                                    cheater(a, e)
                                                    b11['text'] = a
                                            else:
                                                e = b10['text']
                                                cheater(a, e)
                                                b10['text'] = a
                                        else:
                                            e = b9['text']
                                            cheater(a, e)
                                            b9['text'] = a
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
            cheater(a, e)
            b1['text'] = a

        clock.after(500, cheat_activated)


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
            b8['command'] = b9['command'] = b10['command'] = b11['command'] = b12['command'] = b13['command'] = b14[
            'command'] = b15['command'] = b16['command'] = b17['command'] = b18['command'] = b19['command'] = b20[
            'command'] = b21['command'] = b22['command'] = b23['command'] = b24['command'] = b25['command'] = \
        startbutton['command'] = NONE
        startbutton['text'] = 'Cheat\nActivated'
        startbutton['width'] = 20
        cheat_activated()
    else:
        i = 0


def checkwin():
    if b1['text'] == 1 and b2['text'] == 2 and b3['text'] == 3 and b4['text'] == 4 and b5['text'] == 5 \
            and b6['text'] == 6 and b7['text'] == 7 and b8['text'] == 8 and b9['text'] == 9 \
            and b10['text'] == 10 and b11['text'] == 11 and b12['text'] == 12 and b13['text'] == 13 \
            and b14['text'] == 14 and b15['text'] == 15 and b16['text'] == 16 and b17['text'] == 17 \
            and b18['text'] == 18 and b19['text'] == 19 and b20['text'] == 20 and b21['text'] == 21 \
            and b22['text'] == 22 and b23['text'] == 23 and b24['text'] == 24 and b25['text'] == '':
        global win, clicks
        print("You win\nClicks : ", clicks)
        win = 1
        b1['state'] = b2['state'] = b3['state'] = b4['state'] = b5['state'] = b6['state'] = b7['state'] = b8['state'] = \
            b9['state'] = \
            b10['state'] = b11['state'] = b12['state'] = b13['state'] = b14['state'] = b15['state'] = b16['state'] = \
            b17['state'] = \
            b18['state'] = b19['state'] = b20['state'] = b21['state'] = b22['state'] = b23['state'] = b24['state'] = \
            b25['state'] = tkinter.DISABLED


def randomize():
    global clicks, listt, win
    if startbutton['text'] == 'Start Game':
        presenttime()
        tick()
        clicks = 0
        e1['text'] = 'Clicks : ' + str(clicks)
        startbutton['text'] = 'Shuffle\nAgain'
        startbutton['width'] = 20
        b1['state'] = b2['state'] = b3['state'] = b4['state'] = b5['state'] = b6['state'] = b7['state'] = b8['state'] = \
            b9['state'] = \
            b10['state'] = b11['state'] = b12['state'] = b13['state'] = b14['state'] = b15['state'] = b16['state'] = \
            b17['state'] = \
            b18['state'] = b19['state'] = b20['state'] = b21['state'] = b22['state'] = b23['state'] = b24['state'] = \
            b25['state'] = tkinter.NORMAL
        random.shuffle(listt)
        #print(listt)
        # listt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, '', 24]
        b1['text'] = listt[0]
        b2['text'] = listt[1]
        b3['text'] = listt[2]
        b4['text'] = listt[3]
        b5['text'] = listt[4]
        b6['text'] = listt[5]
        b7['text'] = listt[6]
        b8['text'] = listt[7]
        b9['text'] = listt[8]
        b10['text'] = listt[9]
        b11['text'] = listt[10]
        b12['text'] = listt[11]
        b13['text'] = listt[12]
        b14['text'] = listt[13]
        b15['text'] = listt[14]
        b16['text'] = listt[15]
        b17['text'] = listt[16]
        b18['text'] = listt[17]
        b19['text'] = listt[18]
        b20['text'] = listt[19]
        b21['text'] = listt[20]
        b22['text'] = listt[21]
        b23['text'] = listt[22]
        b24['text'] = listt[23]
        b25['text'] = listt[24]


    elif startbutton['text'] == 'Shuffle\nAgain':
        restart = messagebox.askquestion("Restart", "Wanna Quit this Game  &  Start a New One?", icon='warning')
        if restart == 'yes':
            win = 0
            presenttime()
            tick()
            clicks = 0
            b1['state'] = b2['state'] = b3['state'] = b4['state'] = b5['state'] = b6['state'] = b7['state'] = b8[
                'state'] = b9['state'] = \
                b10['state'] = b11['state'] = b12['state'] = b13['state'] = b14['state'] = b15['state'] = b16['state'] = \
                b17['state'] = \
                b18['state'] = b19['state'] = b20['state'] = b21['state'] = b22['state'] = b23['state'] = b24['state'] = \
                b25['state'] = tkinter.NORMAL

            e1['text'] = 'Clicks : ' + str(clicks)
            random.shuffle(listt)
            #print(listt)
            # listt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, '', 24]
            b1['text'] = listt[0]
            b2['text'] = listt[1]
            b3['text'] = listt[2]
            b4['text'] = listt[3]
            b5['text'] = listt[4]
            b6['text'] = listt[5]
            b7['text'] = listt[6]
            b8['text'] = listt[7]
            b9['text'] = listt[8]
            b10['text'] = listt[9]
            b11['text'] = listt[10]
            b12['text'] = listt[11]
            b13['text'] = listt[12]
            b14['text'] = listt[13]
            b15['text'] = listt[14]
            b16['text'] = listt[15]
            b17['text'] = listt[16]
            b18['text'] = listt[17]
            b19['text'] = listt[18]
            b20['text'] = listt[19]
            b21['text'] = listt[20]
            b22['text'] = listt[21]
            b23['text'] = listt[22]
            b24['text'] = listt[23]
            b25['text'] = listt[24]
        else:
            pass


root = Tk()
root.title("Level Difficult")
root.resizable(False, False)


def f1():
    showclicks()
    if b2['text'] == '':
        b1['text'], b2['text'] = b2['text'], b1['text']
    elif b6['text'] == '':
        b1['text'], b6['text'] = b6['text'], b1['text']


def f2():
    showclicks()
    if b1['text'] == '':
        b2['text'], b1['text'] = b1['text'], b2['text']
    elif b3['text'] == '':
        b2['text'], b3['text'] = b3['text'], b2['text']
    elif b7['text'] == '':
        b2['text'], b7['text'] = b7['text'], b2['text']


def f3():
    showclicks()
    if b2['text'] == '':
        b3['text'], b2['text'] = b2['text'], b3['text']
    elif b4['text'] == '':
        b3['text'], b4['text'] = b4['text'], b3['text']
    elif b8['text'] == '':
        b3['text'], b8['text'] = b8['text'], b3['text']


def f4():
    showclicks()
    if b3['text'] == '':
        b4['text'], b3['text'] = b3['text'], b4['text']
    elif b5['text'] == '':
        b4['text'], b5['text'] = b5['text'], b4['text']
    elif b9['text'] == '':
        b4['text'], b9['text'] = b9['text'], b4['text']


def f5():
    showclicks()
    if b4['text'] == '':
        b5['text'], b4['text'] = b4['text'], b5['text']
    elif b10['text'] == '':
        b5['text'], b10['text'] = b10['text'], b5['text']


def f6():
    showclicks()
    if b1['text'] == '':
        b6['text'], b1['text'] = b1['text'], b6['text']
    elif b7['text'] == '':
        b6['text'], b7['text'] = b7['text'], b6['text']
    elif b11['text'] == '':
        b6['text'], b11['text'] = b11['text'], b6['text']


def f7():
    showclicks()
    if b2['text'] == '':
        b7['text'], b2['text'] = b2['text'], b7['text']
    elif b6['text'] == '':
        b7['text'], b6['text'] = b6['text'], b7['text']
    elif b8['text'] == '':
        b7['text'], b8['text'] = b8['text'], b7['text']
    elif b12['text'] == '':
        b7['text'], b12['text'] = b12['text'], b7['text']


def f8():
    showclicks()
    if b7['text'] == '':
        b8['text'], b7['text'] = b7['text'], b8['text']
    elif b3['text'] == '':
        b8['text'], b3['text'] = b3['text'], b8['text']
    elif b9['text'] == '':
        b8['text'], b9['text'] = b9['text'], b8['text']
    elif b13['text'] == '':
        b8['text'], b13['text'] = b13['text'], b8['text']


def f9():
    showclicks()
    if b4['text'] == '':
        b9['text'], b4['text'] = b4['text'], b9['text']
    elif b10['text'] == '':
        b9['text'], b10['text'] = b10['text'], b9['text']
    elif b8['text'] == '':
        b9['text'], b8['text'] = b8['text'], b9['text']
    elif b14['text'] == '':
        b9['text'], b14['text'] = b14['text'], b9['text']


def f10():
    showclicks()
    if b9['text'] == '':
        b10['text'], b9['text'] = b9['text'], b10['text']
    elif b5['text'] == '':
        b10['text'], b5['text'] = b5['text'], b10['text']
    elif b15['text'] == '':
        b10['text'], b15['text'] = b15['text'], b10['text']


def f11():
    showclicks()
    if b12['text'] == '':
        b11['text'], b12['text'] = b12['text'], b11['text']
    elif b16['text'] == '':
        b11['text'], b16['text'] = b16['text'], b11['text']
    elif b6['text'] == '':
        b11['text'], b6['text'] = b6['text'], b11['text']


def f12():
    showclicks()
    if b7['text'] == '':
        b12['text'], b7['text'] = b7['text'], b12['text']
    elif b11['text'] == '':
        b12['text'], b11['text'] = b11['text'], b12['text']
    elif b13['text'] == '':
        b12['text'], b13['text'] = b13['text'], b12['text']
    elif b17['text'] == '':
        b12['text'], b17['text'] = b17['text'], b12['text']


def f13():
    showclicks()
    if b8['text'] == '':
        b13['text'], b8['text'] = b8['text'], b13['text']
    elif b14['text'] == '':
        b13['text'], b14['text'] = b14['text'], b13['text']
    elif b12['text'] == '':
        b13['text'], b12['text'] = b12['text'], b13['text']
    elif b18['text'] == '':
        b13['text'], b18['text'] = b18['text'], b13['text']


def f14():
    showclicks()
    if b13['text'] == '':
        b14['text'], b13['text'] = b13['text'], b14['text']
    elif b15['text'] == '':
        b14['text'], b15['text'] = b15['text'], b14['text']
    elif b19['text'] == '':
        b14['text'], b19['text'] = b19['text'], b14['text']
    elif b9['text'] == '':
        b14['text'], b9['text'] = b9['text'], b14['text']


def f15():
    showclicks()
    if b10['text'] == '':
        b15['text'], b10['text'] = b10['text'], b15['text']
    elif b14['text'] == '':
        b15['text'], b14['text'] = b14['text'], b15['text']
    elif b20['text'] == '':
        b15['text'], b20['text'] = b20['text'], b15['text']


def f16():
    showclicks()
    if b11['text'] == '':
        b16['text'], b11['text'] = b11['text'], b16['text']
    elif b17['text'] == '':
        b16['text'], b17['text'] = b17['text'], b16['text']
    elif b21['text'] == '':
        b16['text'], b21['text'] = b21['text'], b16['text']


def f17():
    showclicks()
    if b16['text'] == '':
        b17['text'], b16['text'] = b16['text'], b17['text']
    elif b22['text'] == '':
        b17['text'], b22['text'] = b22['text'], b17['text']
    elif b12['text'] == '':
        b17['text'], b12['text'] = b12['text'], b17['text']
    elif b18['text'] == '':
        b17['text'], b18['text'] = b18['text'], b17['text']


def f18():
    showclicks()
    if b19['text'] == '':
        b18['text'], b19['text'] = b19['text'], b18['text']
    elif b23['text'] == '':
        b18['text'], b23['text'] = b23['text'], b18['text']
    elif b13['text'] == '':
        b18['text'], b13['text'] = b13['text'], b18['text']
    elif b17['text'] == '':
        b18['text'], b17['text'] = b17['text'], b18['text']


def f19():
    showclicks()
    if b24['text'] == '':
        b19['text'], b24['text'] = b24['text'], b19['text']
    elif b14['text'] == '':
        b19['text'], b14['text'] = b14['text'], b19['text']
    elif b20['text'] == '':
        b19['text'], b20['text'] = b20['text'], b19['text']
    elif b18['text'] == '':
        b19['text'], b18['text'] = b18['text'], b19['text']


def f20():
    showclicks()
    if b25['text'] == '':
        b20['text'], b25['text'] = b25['text'], b20['text']
    elif b15['text'] == '':
        b20['text'], b15['text'] = b15['text'], b20['text']
    elif b19['text'] == '':
        b20['text'], b19['text'] = b19['text'], b20['text']


def f21():
    showclicks()
    if b16['text'] == '':
        b21['text'], b16['text'] = b16['text'], b21['text']
    elif b22['text'] == '':
        b21['text'], b22['text'] = b22['text'], b21['text']


def f22():
    showclicks()
    if b21['text'] == '':
        b22['text'], b21['text'] = b21['text'], b22['text']
    elif b23['text'] == '':
        b22['text'], b23['text'] = b23['text'], b22['text']
    elif b17['text'] == '':
        b22['text'], b17['text'] = b17['text'], b22['text']


def f23():
    showclicks()
    if b24['text'] == '':
        b23['text'], b24['text'] = b24['text'], b23['text']
    elif b22['text'] == '':
        b23['text'], b22['text'] = b22['text'], b23['text']
    elif b18['text'] == '':
        b23['text'], b18['text'] = b18['text'], b23['text']


def f24():
    showclicks()
    if b19['text'] == '':
        b24['text'], b19['text'] = b19['text'], b24['text']
    elif b23['text'] == '':
        b24['text'], b23['text'] = b23['text'], b24['text']
    elif b25['text'] == '':
        b24['text'], b25['text'] = b25['text'], b24['text']


def f25():
    showclicks()
    if b24['text'] == '':
        b25['text'], b24['text'] = b24['text'], b25['text']
    elif b20['text'] == '':
        b25['text'], b20['text'] = b20['text'], b25['text']
    checkwin()


# ===================================================================
# ===================================================================

clock = Label(root, font=('times', 20, 'bold'), bg='#b03a2e', height=2, width=11, bd=7, relief='g')
startbutton = Button(root, text='Start Game', font=('Georgia', 15), command=randomize, height=2, width=20, bd=7,
                     relief='g')
e1 = Label(root, text='Clicks :  0', font=('Georgia', 13), height=3, width=17, bd=7, relief='g', bg='#b03a2e')

b1 = Button(root, text=listt[0], command=f1, height=1, width=3, bd=7, relief='g', state=tkinter.DISABLED)
b2 = Button(root, text=listt[1], command=f2, height=1, width=3, bd=7, relief='g', state=tkinter.DISABLED)
b3 = Button(root, text=listt[2], command=f3, height=1, width=3, bd=7, relief='g', state=tkinter.DISABLED)
b4 = Button(root, text=listt[3], command=f4, height=1, width=3, bd=7, relief='g', state=tkinter.DISABLED)
b5 = Button(root, text=listt[4], command=f5, height=1, width=3, bd=7, relief='g', state=tkinter.DISABLED)
b6 = Button(root, text=listt[5], command=f6, height=1, width=3, bd=7, relief='g', state=tkinter.DISABLED)
b7 = Button(root, text=listt[6], command=f7, height=1, width=3, bd=7, relief='g', state=tkinter.DISABLED)
b8 = Button(root, text=listt[7], command=f8, height=1, width=3, bd=7, relief='g', state=tkinter.DISABLED)
b9 = Button(root, text=listt[8], command=f9, height=1, width=3, bd=7, relief='g', state=tkinter.DISABLED)
b10 = Button(root, text=listt[9], command=f10, height=1, width=3, bd=7, relief='g', state=tkinter.DISABLED)
b11 = Button(root, text=listt[10], command=f11, height=1, width=3, bd=7, relief='g', state=tkinter.DISABLED)
b12 = Button(root, text=listt[11], command=f12, height=1, width=3, bd=7, relief='g', state=tkinter.DISABLED)
b13 = Button(root, text=listt[12], command=f13, height=1, width=3, bd=7, relief='g', state=tkinter.DISABLED)
b14 = Button(root, text=listt[13], command=f14, height=1, width=3, bd=7, relief='g', state=tkinter.DISABLED)
b15 = Button(root, text=listt[14], command=f15, height=1, width=3, bd=7, relief='g', state=tkinter.DISABLED)
b16 = Button(root, text=listt[15], command=f16, height=1, width=3, bd=7, relief='g', state=tkinter.DISABLED)
b17 = Button(root, text=listt[16], command=f17, height=1, width=3, bd=7, relief='g', state=tkinter.DISABLED)
b18 = Button(root, text=listt[17], command=f18, height=1, width=3, bd=7, relief='g', state=tkinter.DISABLED)
b19 = Button(root, text=listt[18], command=f19, height=1, width=3, bd=7, relief='g', state=tkinter.DISABLED)
b20 = Button(root, text=listt[19], command=f20, height=1, width=3, bd=7, relief='g', state=tkinter.DISABLED)
b21 = Button(root, text=listt[20], command=f21, height=1, width=3, bd=7, relief='g', state=tkinter.DISABLED)
b22 = Button(root, text=listt[21], command=f22, height=1, width=3, bd=7, relief='g', state=tkinter.DISABLED)
b23 = Button(root, text=listt[22], command=f23, height=1, width=3, bd=7, relief='g', state=tkinter.DISABLED)
b24 = Button(root, text=listt[23], command=f24, height=1, width=3, bd=7, relief='g', state=tkinter.DISABLED)
b25 = Button(root, text=listt[24], command=f25, height=1, width=3, bd=7, relief='g', state=tkinter.DISABLED)

b1['bg'] = b2['bg'] = b3['bg'] = b4['bg'] = b5['bg'] = b6['bg'] = b7['bg'] = b8['bg'] = b9['bg'] = \
    b10['bg'] = b11['bg'] = b12['bg'] = b13['bg'] = b14['bg'] = b15['bg'] = b16['bg'] = b17['bg'] = b18['bg'] = b19[
    'bg'] \
    = b20['bg'] = b21['bg'] = b22['bg'] = b23['bg'] = b24['bg'] = b25['bg'] = startbutton['bg'] = '#d2a26b'
b1['font'] = b2['font'] = b3['font'] = b4['font'] = b5['font'] = b6['font'] = b7['font'] = b8['font'] = b9['font'] = \
    b10['font'] = b11['font'] = b12['font'] = b13['font'] = b14['font'] = b15['font'] = b16['font'] = b17['font'] \
    = b18['font'] = b19['font'] = b20['font'] = b21['font'] = b22['font'] = b23['font'] = b24['font'] = b25['font'] = (
    'Georgia', 40, font.BOLD)

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=0, column=3)
b5.grid(row=0, column=4)
b6.grid(row=1, column=0)
b7.grid(row=1, column=1)
b8.grid(row=1, column=2)
b9.grid(row=1, column=3)
b10.grid(row=1, column=4)
b11.grid(row=2, column=0)
b12.grid(row=2, column=1)
b13.grid(row=2, column=2)
b14.grid(row=2, column=3)
b15.grid(row=2, column=4)
b16.grid(row=3, column=0)
b17.grid(row=3, column=1)
b18.grid(row=3, column=2)
b19.grid(row=3, column=3)
b20.grid(row=3, column=4)
b21.grid(row=4, column=0)
b22.grid(row=4, column=1)
b23.grid(row=4, column=2)
b24.grid(row=4, column=3)
b25.grid(row=4, column=4)

startbutton.grid(row=5, column=1, columnspan=3)
e1.grid(row=5, column=3, columnspan=2, sticky=E)
clock.grid(row=5, column=0, columnspan=2, sticky=W)
root.bind("<Key>", check_cheat)

mainloop()
