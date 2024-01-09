# Calculez le montant HT de la commande, appliquez une remise de 15% et calculez le prix TTC

prix_ht = float(input("Veuillez saisir le prix de l'article a l'unité HT : "))
quantite_commande = int(input("Veuillez saisir le nombre d'article commandé : "))
prix_commande_ht = prix_ht * quantite_commande
prix_apres_remise = prix_commande_ht - (prix_commande_ht *15/100)
tva = float(input("Saisir le taux de TVA (en %)"))
prix_total_ttc = prix_apres_remise + prix_apres_remise * (tva/100)

print(f"le prix est de {prix_total_ttc}")
