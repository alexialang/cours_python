# Rédiger l’algorithme permettant de compter le nombre de noms saisis avant l’interruption de la
# saisie (lorsque l’on saisit « fin »)

nom=[]
nbNom =0
saisir=""

while saisir !="fin":
  if saisir != "fin":
    saisir=input("Veuillez saisir un nom  (pour arreter ecrivez fin) :")
    nom += [saisir]
  elif saisir == "fin":
    break
  
print(nom)

for i in range (len(nom)):
  nbNom += 1
  
print(f"Vous avez saisis {nbNom - 1} nom(s)")