# afficher une liste de 5 à 15

# liste = range(5,16)
# print(list(liste))

# # afficher une liste de 1 a 100 de chiffre pairs

# chiffre = range(2,101,2)
# print (list(chiffre))

# # Compter le nombre d'occurrences d'une lettre dans une phrase
# lettre_a_chercher = "o"
# phrase = "Bonjour tout le monde"

# for i in (phrase):
#   if i ==lettre_a_chercher:
#     compter = phrase.count(lettre_a_chercher)
# print(compter)

# print(phrase.lower().count(lettre_a_chercher))

# # afficher le premier element d'un tableau 
# ma_liste = ["Pierre", "Paul", "Marie"]
# print(ma_liste[0])

# # #afficher plusieur element d'un tableau 
# ma_liste = ["Pierre", "Paul", "Marie"]
# print (ma_liste[0::2])

# ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print (ma_liste[::2])

# ajouter des élement a une liste
# ma_liste = [1, 2, 3]
# ma_liste.extend([4,5,6])
# print(ma_liste)

# afficher des élèments communs a deux listes
# liste_01 = [1, 5, 6, 7, 9, 10, 11]
# liste_02 = [2, 3, 5, 7, 8, 10, 12]

# for i in (liste_01):
#   for j in (liste_02):
#     if i==j:
#       print(i)
#       # insect sec ?

# # afficher des élement dans l'ordre croissant
# liste = [("Harry Potter", 5), ("Wall-E", 3), ("Blade Runner", 4)]

# liste.sort(key=lambda x: x[1]) 
    

# print(liste)

# - Récupérer une valeur dans un dictionnaire

# employes = {"01": {"identite": {"prenom": "Pierre", "nom": "Dupont"}}}

# print(employes["01"]["identite"]["prenom"])
# print(employes.get("01", {}).get("identite", {}).get("prenom", "valeur inconnue"))

# Additionner les valeurs d'un dictionnaire
# employes = {"Pierre": 2500, "Marie": 5000, "Julien": 1200}

# print(sum(employes.values()))

# import random

# mot = "Bonjour"
# liste = list(mot)
# print(liste)
# random.shuffle(liste)
# mot_random = "".join(liste)
# print("".join(mot_random))

# 'Nombre tronqué: 2938.489'.

nombre = 2938.48872
decimales = 3

print(f"Nombre tronqué: {round(nombre,3)}")

# mot = "Python"

# for i in range(mot):
# 	print(mot[i])
	
# def addition(a, b):
# 	c = a + b
# 	return c

# resultat = addition(5, 10)
# print(resultat)

# liste = ["Pierre", "Paul", "Marie"]

# for i,nom in enumerate(liste):
#   print(i,nom)

# nombres = range(50)
# nombres_pairs = [nombres] 
# print(nombres_pairs)

liste = ["Pierre", "Marie", "Julie", "Adrien", "Julie"]
nom_a_chercher = "Julie"
nouveau_nom = "Julien"

nom = list(liste)
print(nom)
# newListe = nom.replace(nom_a_chercher,nouveau_nom)

# print(liste) 