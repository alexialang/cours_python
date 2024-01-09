# demande 10 noms au clavier et les stock dans un tableau

tab_nom = []
tab_prenom = []

for i in range (10):
  tab_prenom += input("Veuillez saisir un prénom : ")
  tab_nom += input("Veuillez saisir un nom : ")
  
for i in range (10):
  print(tab_nom[i],tab_prenom[i])