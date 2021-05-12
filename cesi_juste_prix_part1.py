# -*- coding: utf8 -*-
import random

print("Bienvenue sur le célèbre jeu du juste prix, tu dois deviner le prix auquel je pense, il se situe entre 1 et 100")

random_number = random.randint(0, 100)
# print(random_number)

result = False


while result == False:
	user_answer = int(input())

	if user_answer == random_number:
		print("c'est ça")
		result = True
	else:
		if user_answer < random_number:
			print("c'est plus")
		elif user_answer > random_number:
			print("c'est moins")