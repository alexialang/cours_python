stagiaires =[]

for i in range (15):
  nom= input("veuillez saisir le nom : ")
  prenom= input("Veuillez saisir le prénom : ")
  classe = input("Veuillez saisir la classe : ")
  stagiaires += [[nom]+[prenom]+[classe]]
  
print(stagiaires)