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



pozycja=[[0,0],[0,1],[0,2],[0,3],[1,0],[1,1],[1,2],[1,3],[2,0],[2,1],[2,2],[2,3],[3,0],[3,1],[3,2],[3,3]]

pomocny= [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

pomocny = random.sample(pomocny, k=len(pomocny))



przyciski=[]



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



while True:

	master. update_idletasks ()

	master. update ()



	if przyciski_do_wyczyszczenia:

		time.sleep(0.5)

		for przycisk in przyciski_do_wyczyszczenia:

			przycisk["text"]=" "

		del przyciski_do_wyczyszczenia[:]
