from tkinter import *
import time
import random

master = Tk()
button_switch = True


def close_window(wygrana):
  master.destroy()
  wygrana.destroy()

lista = [0]
przyciski_do_wyczyszczenia = []

def click(przyciski, txt,lista, id):
  lista.append(id)
  for i in range(1, len(przyciski)+1):
    if lista[len(lista)-2] == i:
      poprzedni = przyciski[i-1]

  for i in range(1, len(przyciski)+1):
    if lista[len(lista)-1] == i:
      aktualny = przyciski[i-1]

  aktualny["text"] = txt

  if lista[len(lista)-2] != 0 and poprzedni["text"] != " " and poprzedni["state"] != DISABLED:
      if aktualny["text"] == poprzedni["text"] and aktualny != poprzedni:
          aktualny["state"] = DISABLED
          aktualny["background"] = "lightgray"
          poprzedni["state"] = DISABLED
          poprzedni["background"] = "lightgray"
      elif aktualny["text"] != poprzedni["text"]:
          przyciski_do_wyczyszczenia.append(aktualny)
          przyciski_do_wyczyszczenia.append(poprzedni)

  if all(x["state"] == DISABLED for x in przyciski):
    wygrana = Tk()
    button = Button(wygrana, text="BRAWO", background="yellow", command=lambda: close_window(wygrana))
    button.pack()


#losowanie pozycji
pozycja=[[0,0],[0,1],[0,2],[0,3],[1,0],[1,1],[1,2],[1,3]]
pomocny= [0,1,2,3,4,5,6,7]
pomocny = random.sample(pomocny, k=len(pomocny))

przyciski=[]

b1 = Button(master, text=" ", command=lambda: click(przyciski, "Goodbye", lista, 1), background="skyblue", width=8, height=5, state=NORMAL)
b1.grid(row=pozycja[pomocny[0]][0], column=pozycja[pomocny[0]][1])
b2 = Button(master, text=" ", command=lambda: click(przyciski, "Goodbye", lista, 2), background="skyblue", width=8, height=5, state=NORMAL)
b2.grid(row=pozycja[pomocny[1]][0], column=pozycja[pomocny[1]][1])
b3 = Button(master, text=" ", command=lambda: click(przyciski, "Hello", lista, 3), background="skyblue", width=8, height=5, state=NORMAL)
b3.grid(row=pozycja[pomocny[2]][0], column=pozycja[pomocny[2]][1])
b4 = Button(master, text=" ", command=lambda: click(przyciski, "Hello", lista, 4), background="skyblue", width=8, height=5, state=NORMAL)
b4.grid(row=pozycja[pomocny[3]][0], column=pozycja[pomocny[3]][1])
b5 = Button(master, text=" ", command=lambda: click(przyciski, "Bye", lista, 5), background="skyblue", width=8, height=5, state=NORMAL)
b5.grid(row=pozycja[pomocny[4]][0], column=pozycja[pomocny[4]][1])
b6 = Button(master, text=" ", command=lambda: click(przyciski, "Bye", lista, 6), background="skyblue", width=8, height=5, state=NORMAL)
b6.grid(row=pozycja[pomocny[5]][0], column=pozycja[pomocny[5]][1])
b7 = Button(master, text=" ", command=lambda: click(przyciski, "Hi", lista, 7), background="skyblue", width=8, height=5, state=NORMAL)
b7.grid(row=pozycja[pomocny[6]][0], column=pozycja[pomocny[6]][1])
b8 = Button(master, text=" ", command=lambda: click(przyciski, "Hi", lista, 8), background="skyblue", width=8, height=5, state=NORMAL)
b8.grid(row=pozycja[pomocny[7]][0], column=pozycja[pomocny[7]][1])

przyciski.append(b1)
przyciski.append(b2)
przyciski.append(b3)
przyciski.append(b4)
przyciski.append(b5)
przyciski.append(b6)
przyciski.append(b7)
przyciski.append(b8)





# poniższe trzy linijki zastępują "mainloop()", a po nich następuje kod dodatkowy
while True:
	master. update_idletasks ()
	master. update ()

	if przyciski_do_wyczyszczenia:
		time.sleep(0.5)
		for przycisk in przyciski_do_wyczyszczenia:
			przycisk["text"]=" "
		del przyciski_do_wyczyszczenia[:]

