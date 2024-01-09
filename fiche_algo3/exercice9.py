# Écrire un algorithme affichant p pointes (côte à côte) de dimension d.

number = int(input("Veuillez saisir le nombre de point que vous voulez afficher : "))

dimension = int(input(f"Veuillez saisir le taille de la pointe : "))
  
  
pointe = "_ "* number
  
for i in range(dimension): 
  pointe += "\n" + "| "* number

print(pointe)