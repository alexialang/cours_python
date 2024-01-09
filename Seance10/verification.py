# Écrire un algorithme qui demande un nombre compris entre 10 et 20, jusqu’à ce que la réponse
# convienne. En cas de réponse supérieure à 20, on fera apparaître un message : « Plus petit ! », et
# # inversement, « Plus grand ! » si le nombre est inférieur à 10.

note = int(input("Saisir une note entre 10 et 20 : "))
while note < 10 or note >20 :
  if note < 10:
    print("Plus grand !")
    note = int(input("Saisir une note entre 10 et 20 : "))
  elif note > 20:
    print("Plus petit !")
    note = int(input("Saisir une note entre 10 et 20 : "))
    
    
print(f"la note est {note}")
