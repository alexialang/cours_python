francais = float(input("Veuillez rentrer votre note de francais : "))
coeff_fr = int(input("Veuillez précisez le coefficient de français : "))
note_fr = francais*coeff_fr

math = float(input("Veuillez rentrer votre note de Math : "))
coeff_math = int(input("Veuillez préciser le coefficient de math : "))
note_math = math*coeff_math

geom = float(input("Veuillez rentrer votre note de géométrie : "))
coeff_geom = int(input("Veuillez préciser le coefficient de géométrie : "))
note_geom = geom* coeff_geom

info = float(input("Veuiller rentrer votre note d'informatique : "))
coeff_info = int(input("Veuillez préciser le coefficient d'informatique : "))
note_info = info*coeff_info

# Calcule de la moyenne en fonction de coefficients
moyenne= (note_fr +  note_math +  note_geom +  note_info) / (coeff_fr + coeff_math + coeff_geom + coeff_info )

print(f"Votre moyenne est de {round(moyenne,1)}, /20")
