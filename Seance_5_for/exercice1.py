#  ecrire un algo qui demande l'âge et l'informe de sa catégorie

age = int(input("Veuillez saisir votre âge : "))

if age < 10 :
  categorie = "eveil"
elif age == 10 or age == 11:
  categorie = "Poussin"
elif age == 12 or age == 13:
  categorie = "Benjamin"
elif age == 14 or age == 15:
  categorie = "Minime"
elif age == 16 or age == 17:
  categorie = "Cadet"
elif age == 18 or age == 19:
  categorie = "Junior"
elif age >= 20 and age <= 22:
  categorie = "Espoir"
elif age >= 23 and age <= 39 :
  categorie = "Senior"
else:
  categorie = "Vétéran"

print (f"Vous êtes dans la catégorie {categorie}")

# Ecrire un algo qui informe l'utilisateur s'il est Benjamin ou non

age = int(input("Veuillez saisir votre âge : "))


if age == 12 or age == 13:
  print("Vous êtes benjamin")
else:
  print("Vous n'êtes pas benjamin")
