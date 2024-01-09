n = int(input("Veuillez saisir un nombre : "))

# Calculer le reste de la division euclidienne de n par 2
reste = n %2

# On test la valeur de reste
# Si reste vaut 0 alors n est pair
if reste == 0 :
    print(f"{n} est un nombre pair.")
else: print(f"{n} est un nombre impair.")
# Si reste vaut 1 alors n est impair