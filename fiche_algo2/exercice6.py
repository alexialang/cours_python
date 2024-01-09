prixHT = float(input("Veuillez saisir le prix Ht : "))

print("Tva 5.5% tapez 1")
print("Tva 19.6% tapez 2")
print("Tva 33% tapez 3")
tva = int(input("Veuillez rentrer le code pour la tva : "))


if tva == 1:
  print(f"Le prix Ht est de {prixHT}, la tva est de 5,5% et le prix TTC est de {(prixHT *5.5/100)+ prixHT}")
elif tva ==2:
  print(f"Le prix Ht est de {prixHT}, la tva est de 19,6% et le prix TTC est de {(prixHT *19.6/100) + prixHT}")
elif tva == 3:
  print(f"Le prix Ht est de {prixHT}, la tva est de 33% et le prix TTC est de {(prixHT *33/100) + prixHT}")
else: print("Mauvaise saisie")