import random


chiffreMagique = random.randint(1,10)
erreur = "Veuillez saisir un nombre entre 1 et 10"
number=int(input("Essayez de devinez le nombre, ce nombre est compris entre 1 et 10 "))



while number < 1 or number > 10:
  print("Valeur non permises")
  number = int(input("Essayez de devinez le nombre, ce nombre est compris entre 1 et 10 "))
  
while number != chiffreMagique:
  if number== chiffreMagique:
    print("bravo vous avez gagné")
    break
  elif number < chiffreMagique:
    print("Trop petit")
    number = int(input("Essayez de devinez le nombre, ce nombre est compris entre 1 et 10 "))
  elif number > chiffreMagique:
    print("Trop grand")
    number = int(input("Essayez de devinez le nombre, ce nombre est compris entre 1 et 10 "))

