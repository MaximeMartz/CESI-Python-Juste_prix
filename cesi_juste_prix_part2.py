# -*- coding: utf8 -*-
import random
import threading
import sys


def game(timer):
	print("Bienvenue sur le célèbre jeu du juste prix, tu dois deviner le prix auquel je pense, il se situe entre 1 et 100")

	random_number = random.randint(0, 100)
	# print(random_number)

	result = False

	attempts = 5


	while result == False and attempts > 0:
		user_answer = int(input())
		# print(attempts)

		if user_answer == random_number:
			print("c'est ça")
			result = True
		else:
			if user_answer < random_number:
				print("c'est plus")
			elif user_answer > random_number:
				print("c'est moins")
			attempts -= 1
			if attempts == 0:
				print("c'est perdu")

	timer.cancel()

def too_late():
	print("Trop tard")
	sys.exit()

t1 = threading.Timer(60.0, too_late)
t2 = threading.Thread(target=game, args=[t1], daemon = True)

t1.start()
t2.start()