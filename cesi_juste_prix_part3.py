# -*- coding: utf8 -*-
import random
import threading
import sys
from tkinter import *
from tkinter import ttk

WELCOME_MESSAGE = "Bienvenue sur le célèbre jeu du juste prix, tu dois deviner le prix auquel je pense, il se situe entre 1 et 100"
TOO_LATE = "Trop tard"
GAME_OVER = "C'est perdu"
LOWER = "C'est moins"
GREATER = "C'est plus"
BINGO = "C'est ça"
ATTEMPTS = "Tentatives restantes : "
MAX_ATTEMPTS_NUMBER = 5
TIMER = "Secondes restantes : "
MAX_TIME = 60


random_number = random.randint(0, 100)


remaining_attempts = MAX_ATTEMPTS_NUMBER
remaining_time = MAX_TIME
countdown_callback = None


def check_user_answer(*args):
	global remaining_attempts
	
	remaining_attempts -= 1
	attempts_string_var.set(ATTEMPTS + str(remaining_attempts))

	value = int(answer.get())

	if value == random_number:
		display_result_and_deactivate(BINGO)
	else:
		if value < random_number:
			result.set(GREATER)
		elif value > random_number:
			result.set(LOWER)
		if remaining_attempts == 0:
			display_result_and_deactivate(GAME_OVER)


def display_result_and_deactivate(message):
	result.set(message)
	deactivate()
	root.after_cancel(countdown_callback)


def countdown():
	global remaining_time
	global countdown_callback

	if remaining_time > 0:
		remaining_time -= 1
		timer.set(TIMER + str(remaining_time))
		countdown_callback = root.after(1000, lambda: countdown())
	else:
		result.set(TOO_LATE)
		deactivate()


def deactivate():
	answer_entry.state(["disabled"])
	button.state(["disabled"])

root = Tk()
root.title("Juste Prix")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, E, S, W))

s = ttk.Style()
s.configure("TFrame", background="#28EB97")
s.configure("TLabel", background="#28EB97")


answer = StringVar()
answer_entry = ttk.Entry(mainframe, width=7, textvariable=answer)
answer_entry.grid(column=1, row=3, sticky=(N, E, S, W))

result = StringVar()
ttk.Label(mainframe, textvariable=result).grid(column=2, row=3, sticky=(N, E, S, W))

button = ttk.Button(mainframe, text="Valider", command=check_user_answer)
button.grid(column=3, row=3, sticky=(N, E, S, W))

ttk.Label(mainframe, text=WELCOME_MESSAGE).grid(column=1, row=2, columnspan=3, sticky=(N, E, S, W))

attempts_string_var = StringVar()
attempts_string_var.set(ATTEMPTS + str(remaining_attempts))
ttk.Label(mainframe, textvariable=attempts_string_var).grid(column=3, row=1, sticky=(N, E, S))

timer = StringVar()
timer.set(TIMER + str(remaining_time))
ttk.Label(mainframe, textvariable=timer).grid(column=1, row=1, sticky=(N, E, S, W))


for child in mainframe.winfo_children():
	child.grid_configure(padx=5, pady=5)
answer_entry.focus()
root.bind("<Return>", check_user_answer)

countdown()

root.mainloop()