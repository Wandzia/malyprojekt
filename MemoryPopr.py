"""
Program - gra Memory.
Przygotowany w ramach zajęć laboratoryjnych z inżynierii oprogramowania.
Autorzy: Michalina Bielewicz, Natalia Bulak, Wanda Roda.

Rozpoczęcie: 4 października 2018. Ostatnia modyfikacja: 30 pażdziernika 2018.

This program is free software: you can redistribute it and modify
it under the terms of the GNU General Public License.
"""


from tkinter import *

import time

import random

# okno startowe
start = Tk()
start.title("Memory")
top = Frame(start)
bottom = Frame(start)
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=True)

mem = Label(start, text="Memory", background="LightYellow", font=("Times New Roman", 30), height=5, width=15)
mem.pack()
startb = Button(start, text="Zagraj", background="LemonChiffon", font=("Times New Roman", 20), command=lambda: startok())
startb.pack(in_=bottom, side=LEFT)
zakoncz = Button(start, text="Zakończ", background="LemonChiffon", font=("Times New Roman", 20), command=lambda: close_window_start(start))
zakoncz.pack(in_=bottom, side=RIGHT)
instrukcja = Button(start, text="Instrukcja", background="LemonChiffon", font=("Times New Roman", 20), command=lambda: instr())
instrukcja.pack(in_=bottom)


# przycisk intrukcja
def instr():
    Ins = Tk()
    Ins.title("Memory")
    Inst = Label(Ins, text="Memory to gra pamięciowa, której zadaniem jest ćwiczenie pamięci i koncentracji u osób w każdym wieku. \n Celem gry jest wyszukiwanie par napisów. \n Klikając przyciski, odkrywaj napisy i zapamiętuj ich położenie aby znaleźć wszystkie pary.", background="white")

    Inst.pack()


# zamknięcie okien
def close_window_start(start):
    start.destroy()


# funkcja przycisku zagraj- okno memory
def startok():
    start.destroy()
    master = Tk()
    master.title("Memory")
    button_switch = True
    lista = [0]
    przyciski_do_wyczyszczenia = []

    # zamknięcie okien
    def close_window(wygrana, master):
        master.destroy()
        wygrana.destroy()

    # funkcja przycisków
    def click(przyciski, txt, lista, id):
        lista.append(id)  # lista kolejno klikniętych przycisków

        for i in range(1, len(przyciski)+1):
            if lista[len(lista)-2] == i:
                poprzedni = przyciski[i-1]  # zapamiętanie uprzednio klikniętego przycisku

        for i in range(1, len(przyciski)+1):
            if lista[len(lista)-1] == i:
                aktualny = przyciski[i-1]  # zapamiętanie aktualnie klikniętego przycisku

        aktualny["text"] = txt  # wyświetlenie tekstu

        if lista[len(lista)-2] != 0 and poprzedni["text"] != " " and poprzedni["state"] != DISABLED:
            if aktualny["text"] == poprzedni["text"] and aktualny != poprzedni:  # odkrycie tych samych przycisków -> zamrożenie
                aktualny["state"] = DISABLED
                aktualny["background"] = "lightgray"
                poprzedni["state"] = DISABLED
                poprzedni["background"] = "lightgray"

            elif aktualny["text"] != poprzedni["text"]:  # odkrycie dwóch różnych przycisków -> zakrycie
                przyciski_do_wyczyszczenia.append(aktualny)
                przyciski_do_wyczyszczenia.append(poprzedni)

        if all(x["state"] == DISABLED for x in przyciski):  # koniec gry
            wygrana = Tk()
            wygrana.title("Memory")
            wygrana.config(bg='LightYellow')
            label = Label(wygrana, text="Brawo!", background="LightYellow", font=("Times New Roman", 30), height=5, width=10)
            label.pack()
            button = Button(wygrana, text="Zakończ", background="LemonChiffon", font=("Times New Roman", 20), command=lambda: close_window(wygrana, master))
            button.pack(fill=X)

    # losowanie pozycji
    pozycja=[[0,0], [0,1], [0,2], [0,3], [1,0], [1,1], [1,2], [1,3], [2,0], [2,1], [2,2], [2,3], [3,0], [3,1], [3,2], [3,3]]
    pomocny= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    pomocny = random.sample(pomocny, k=len(pomocny))

    przyciski=[]

    # stworzenie przycisków
    b1 = Button(master, text=" ", command=lambda: click(przyciski, "Goodbye", lista, 1), background="skyblue", width=11, height=5, state=NORMAL)
    b1.grid(row=pozycja[pomocny[0]][0], column=pozycja[pomocny[0]][1])
    b2 = Button(master, text=" ", command=lambda: click(przyciski, "Goodbye", lista, 2), background="skyblue", width=11, height=5, state=NORMAL)
    b2.grid(row=pozycja[pomocny[1]][0], column=pozycja[pomocny[1]][1])
    b3 = Button(master, text=" ", command=lambda: click(przyciski, "Hello", lista, 3), background="skyblue", width=11, height=5, state=NORMAL)
    b3.grid(row=pozycja[pomocny[2]][0], column=pozycja[pomocny[2]][1])
    b4 = Button(master, text=" ", command=lambda: click(przyciski, "Hello", lista, 4), background="skyblue", width=11, height=5, state=NORMAL)
    b4.grid(row=pozycja[pomocny[3]][0], column=pozycja[pomocny[3]][1])
    b5 = Button(master, text=" ", command=lambda: click(przyciski, "Bye", lista, 5), background="skyblue", width=11, height=5, state=NORMAL)
    b5.grid(row=pozycja[pomocny[4]][0], column=pozycja[pomocny[4]][1])
    b6 = Button(master, text=" ", command=lambda: click(przyciski, "Bye", lista, 6), background="skyblue", width=11, height=5, state=NORMAL)
    b6.grid(row=pozycja[pomocny[5]][0], column=pozycja[pomocny[5]][1])
    b7 = Button(master, text=" ", command=lambda: click(przyciski, "Hi", lista, 7), background="skyblue", width=11, height=5, state=NORMAL)
    b7.grid(row=pozycja[pomocny[6]][0], column=pozycja[pomocny[6]][1])
    b8 = Button(master, text=" ", command=lambda: click(przyciski, "Hi", lista, 8), background="skyblue", width=11, height=5, state=NORMAL)
    b8.grid(row=pozycja[pomocny[7]][0], column=pozycja[pomocny[7]][1])
    b9 = Button(master, text=" ", command=lambda: click(przyciski, "Thank you", lista, 9), background="skyblue", width=11, height=5, state=NORMAL)
    b9.grid(row=pozycja[pomocny[8]][0], column=pozycja[pomocny[8]][1])
    b10 = Button(master, text=" ", command=lambda: click(przyciski, "Thank you", lista, 10), background="skyblue", width=11, height=5, state=NORMAL)
    b10.grid(row=pozycja[pomocny[9]][0], column=pozycja[pomocny[9]][1])
    b11 = Button(master, text=" ", command=lambda: click(przyciski, "I am Kuba", lista, 11), background="skyblue", width=11, height=5, state=NORMAL)
    b11.grid(row=pozycja[pomocny[10]][0], column=pozycja[pomocny[10]][1])
    b12 = Button(master, text=" ", command=lambda: click(przyciski, "I am Kuba", lista, 12), background="skyblue", width=11, height=5, state=NORMAL)
    b12.grid(row=pozycja[pomocny[11]][0], column=pozycja[pomocny[11]][1])
    b13 = Button(master, text=" ", command=lambda: click(przyciski, "Good morning", lista, 13), background="skyblue", width=11, height=5, state=NORMAL)
    b13.grid(row=pozycja[pomocny[12]][0], column=pozycja[pomocny[12]][1])
    b14 = Button(master, text=" ", command=lambda: click(przyciski, "Good morning", lista, 14), background="skyblue", width=11, height=5, state=NORMAL)
    b14.grid(row=pozycja[pomocny[13]][0], column=pozycja[pomocny[13]][1])
    b15 = Button(master, text=" ", command=lambda: click(przyciski, "Good night", lista, 15), background="skyblue", width=11, height=5, state=NORMAL)
    b15.grid(row=pozycja[pomocny[14]][0], column=pozycja[pomocny[14]][1])
    b16 = Button(master, text=" ", command=lambda: click(przyciski, "Good night", lista, 16), background="skyblue", width=11, height=5, state=NORMAL)
    b16.grid(row=pozycja[pomocny[15]][0], column=pozycja[pomocny[15]][1])

    # tablica przycisków
    przyciski.append(b1)
    przyciski.append(b2)
    przyciski.append(b3)
    przyciski.append(b4)
    przyciski.append(b5)
    przyciski.append(b6)
    przyciski.append(b7)
    przyciski.append(b8)
    przyciski.append(b9)
    przyciski.append(b10)
    przyciski.append(b11)
    przyciski.append(b12)
    przyciski.append(b13)
    przyciski.append(b14)
    przyciski.append(b15)
    przyciski.append(b16)

    # poniższe trzy linijki zastępują "mainloop()", a po nich następuje kod dodatkowy
    while True:
            master. update_idletasks()
            master. update()
            if przyciski_do_wyczyszczenia:
                    time.sleep(0.5)
                    for przycisk in przyciski_do_wyczyszczenia:
                            przycisk["text"] = " "
                    del przyciski_do_wyczyszczenia[:]

mainloop()