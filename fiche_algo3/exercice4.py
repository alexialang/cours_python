
borneDepart = int(input("Veuillez saisir un nombre pour la borne de départ : "))
borneArrivee = int(input("Veuillez saisir un nombre pour la borne d'arrivée : "))
pas = int(input("Veuillez saisir un nombre de pas"))


for i in range (borneDepart,borneArrivee+1,pas):
  print(i,end=" ")
  