
#  Jeu de dé

print("Jeu de dés \n")

import random
number = (random.randint(1,6))

if number == 1:
  print("Vous avez fait un \n\n \n  0\n")
elif number == 2:
  print("Vous avez fait deux \n\n  0\0 ")
elif number == 3:
  print("Vous avez fait trois \n\n  0\n 0 \n")
elif number == 4:
  print("Vous avez fait quatre \n\n0 0\n0 0")
elif number == 5:
  print("Vous avez fait cinq \n\n0 0\n 0 \n0 0")
else: 
  print("Vous avez fait six \n\n0 0\n0 0\n0 0")


