import tkinter
from tkinter import *
from tkinter import messagebox
import random
from random import shuffle

answers = ["america","india","asia","japan","pakistan","africa","dragonfly","paris","france","google","tesla"]
questions = []

for i in answers:
    words = list(i)
    shuffle(words)
    questions.append(words)
    
num = random.randint(0, len(questions)-1)

def initial():
    global questions,num
    lb1.configure(text=questions[num])

def answercheck():
    global questions,num,answers
    userinput = e1.get()
    if userinput ==answers[num]:
        messagebox.showinfo('Sucess','Your ans was correct')
    else:
        messagebox.showinfo('Wrong','Your ans was incorrect')
        e1.delete(0,END)     

def resetswitch():
    global questions,num,answers
    num = random.randint(0,len(questions)-1)
    lb1.configure(text=questions[num])
    e1.delete(0, END)

window = Tk()
window.geometry("300x300")
window.configure(background ='#FF6666')
window.title("JumbleBot")
window.iconbitmap(r"Pythonmd\JumbleBot\icon.ico")

lb1 = Label(window, font="times 20",bg='#1B98F5',fg='#120E43')
lb1.pack(pady = 30,ipady=10,ipadx = 10)


answer = StringVar()
e1 = Entry(window , textvariable=answer)
e1.pack(ipady = 5,ipadx = 5)

button1 = Button(window,text= "Check",width= 20,bg='#22CB5C' ,command = answercheck)
button1.pack(pady=40)

button2 = Button(window,text= "Reset",width=20,bg='#EDBF69',command = resetswitch)
button2.pack()

initial()

window.mainloop()



