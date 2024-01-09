# Calculer le prix TTC à partir d'un prix HT et d'une TVA de 20%

prixHT = float(input("Veuillez saisir le prix HT: "))
prixTTC = (prixHT*20/100) + prixHT
print (f"le prix TTC est de : {prixTTC}")

