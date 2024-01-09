# Calculer une moyenne

francais = float(input("Veuillez rentrer votre note de français (/20) : "))
math = float(input("Veuillez rentrer votre note de math (/20) : "  ))
geometrie = float(input ("Veuillez rentrer votre note de géométrie (/20) : "))
informatique = float(input("Veuillez rentrer votre note d'informatique (/20) : "))
moyenne = ( francais+math+geometrie+informatique ) / 4
print(f"Votre moyenne est de : {moyenne} /20")
