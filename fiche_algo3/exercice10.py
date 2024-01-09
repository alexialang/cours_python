# Écrire un algorithme qui demande successivement 20 nombres à l’utilisateur, et qui lui dise ensuite
# quel était le plus grand parmi ces 20 nombres.:

maxValue = 0
for i in range(20):
  number = float(input("Veuillez saisir un nombre : "))
 
  if number > maxValue:
    maxValue = number
    
print(f"Le chiffre le plus grand saisie est :{maxValue}")