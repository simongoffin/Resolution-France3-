#!/usr/local/bin/python
# -*- coding:utf-8 -*-
from Tkinter import *
from core import *

def calcul():
    arg1=ent1.get()
    arg2=ent2.get()
    arg3=ent3.get()
    arg4=ent4.get()
    arg5=ent5.get()
    arg6=ent6.get()
    arg7=ent7.get()
    tuple=(int(arg1),int(arg2),int(arg3),int(arg4),int(arg5),int(arg6))
    compte=int(arg7)
    v=run(tuple,compte)
    affichage1['text'] = v[0]
    affichage2['text'] = v[1]
    affichage3['text'] = v[2]
    affichage4['text'] = v[3]
    affichage5['text'] = v[4]
    

application = Tk()
application.title("Résolution")

frame1 = Frame(application, bg="white", width=300, height=150)
frame1.pack(side=TOP,fill=Y)

frame3 = Frame(application, bg="white", width=300, height=150)
frame3.pack(side=BOTTOM,fill=Y)

frame2 = Frame(application, bg="white",width=300, height=150)
frame2.pack(side=BOTTOM, fill=Y)



w=3

lab1 = Label(frame1, text="1").grid(row=0,column=0)
ent1 = Entry(frame1,width=w)
ent1.grid(row=0,column=1)
lab2 = Label(frame1, text="2" ).grid(row=0,column=2)
ent2 = Entry(frame1,width=w)
ent2.grid(row=0,column=3)
lab3 = Label(frame1, text="3").grid(row=0,column=4)
ent3 = Entry(frame1,width=w)
ent3.grid(row=0,column=5)
lab4 = Label(frame1, text="4").grid(row=0,column=6)
ent4 = Entry(frame1,width=w)
ent4.grid(row=0,column=7)
lab5 = Label(frame1, text="5" ).grid(row=0,column=8)
ent5 = Entry(frame1,width=w)
ent5.grid(row=0,column=9)
lab6 = Label(frame1, text="6").grid(row=0,column=10)
ent6 = Entry(frame1,width=w)
ent6.grid(row=0,column=11)
lab7 = Label(frame1, text="C").grid(row=1,column=0)
ent7 = Entry(frame1,width=w)
ent7.grid(row=1,column=1)


valeur = Button(frame2, text =' run', command=calcul)
valeur.pack()

affichage1 = Label(frame3, width=30)
affichage1.pack()
affichage2 = Label(frame3, width=30)
affichage2.pack()
affichage3 = Label(frame3, width=30)
affichage3.pack()
affichage4 = Label(frame3, width=30)
affichage4.pack()
affichage5 = Label(frame3, width=30)
affichage5.pack()

application.mainloop()