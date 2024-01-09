# Jeu chiffre qui s'incrémente en mangeant les o
from os import system
from pynput.keyboard import Listener
import keyboard
import msvcrt

map = [[" X "," X "," X "," X "," X "," X "," X "],
       [" X "," 0 ","   ","   ","   ","   "," X "],
       [" X ","   "," o ","   ","   ","   "," X "],
       [" X ","   ","   ","   ","   ","   "," X "],
       [" X ","   ","   "," o ","   ","   "," X "],
       [" X "," o ","   ","   ","   ","   "," X "],
       [" X ","   ","   ","   ","   ","   "," X "],
       [" X ","   ","   ","   ","   ","   "," X "],
       [" X "," X "," X "," X "," X "," X "," X "]]



# affichage de la map

map_print = ""

for ligne in range (len(map)):
  map_print+="\n"
  for box in range (len(map[ligne])):
    map_print += map[ligne][box]
print(map_print)


# touche

def commande():
  while True:
    if msvcrt.kbhit():
      touche = msvcrt.getch()
      return touche.decode('utf-8')


while True:
  touche = commande()
  system("cls")
  print(map_print)
  coordonnees = []
  for x in range (len(map)):
    for y in range (len(map[x])) :
      if map[x][y] == " 0 " :
        coordonnees = [x,y]
        break
    if map[x][y] == " 0 " :
      if touche == "z":
        map[x-1][y] = " 0 "
        map[x][y] = "   "
      # elif touche == "q":

      # elif touche == "s":
        
      elif touche == "d":
        map[x][y+1] = " 0 "
        map[x][y] = "   "
    print(map_print)

  break

    
