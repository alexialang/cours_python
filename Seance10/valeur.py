# Une voiture coûte 56 000 e et perd 7% de sa valeur chaque année.
# Rédiger le programme qui calcule et affiche la valeur de cette voiture au bout de 18 ans.

prix =int(input("Veuillez saisir le prix de votre voiture : "))
annee =int(input("Dans combien d'années souhaitez vous la vendre : "))

for i in range(annee):
  perteValeur = prix -( prix *7/100 )
  prix = perteValeur
  
print(f"{round(prix,2)} euros")


 