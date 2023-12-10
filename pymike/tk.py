#!/usr/bin/python3
from tkinter import *


def funzioneDelBottone():
    testo_due = Label(text="un secondo testo", fg="red",
                      font=("Helvetica", 22)).pack()
finestra = Tk()
finestra.geometry("300x300+500+150")
finestra.title("la mia prima finestra TK")
testo = Label(finestra, text="il mio primo testo", fg="red", bg="yellow",
              font="Helvetica").pack(fill=BOTH, expand=1)
testo_due = Label(finestra, text="il mio secondo testo", fg="red", bg="blue",
                  font="Helvetica").pack(side=LEFT)
testo_tre = Label(finestra, text="il mio terzo testo", fg="red", bg="green",
                  font="Helvetica").pack(fill=X)
testo_quattro = Label(finestra, text="il mio quarto testo", fg="red",
                      bg="green", font="Helvetica").pack(fill=X)
bottone = Button(text="un bottone fasullo", command=funzioneDelBottone).pack()

finestra.mainloop()
