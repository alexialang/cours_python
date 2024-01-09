# Écrivez un algorithme qui convertisse un nombre de la base 10 vers la base 2 (en binaire).

binaire = ""
quotient=1
number = int(input("Veuillez rentrez un nombre de la base 10 a convertir en binaire : "  ))

while quotient !=0:
  quotient=number //2 
  reste= number%2
  binaire = str(reste) + binaire
  number = quotient

print(binaire)    
