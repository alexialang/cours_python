# Écrivez un algorithme qui calcule l’épaisseur du pliage final à partir du nombre 
# de plis et de l’épaisseur initiale de la feuille.

epaisseur_feuille = float(input("Veuillez saisir l'épaisseur de la feuille : "))
nombre_plis = int(input("Veuillez saisir le nombre de fois que vous voulez plier la feuille : "))


for i in range (nombre_plis):
  epaisseur_feuille *=2
  
print(epaisseur_feuille)