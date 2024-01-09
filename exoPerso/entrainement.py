
 #EXERCICE 1  déterminer si une chaine de caractère contient une lettre

mot= str(input("choisissez un mot : ")) 
lettre = str(input("choisissez une lettre : "))

for i in (mot):
  if i== lettre :
    count = mot.count(lettre)

# print(count)

# EXERCICE 2 variable qui transforme "gaston" en "g*a*s*t*o*n"

var1 = str(input("Veuillez rentrer un mot : "))

i= 0

for i in (var1):
  print (i,"*",end="")

# EXERCICE 3 inverser l'ordre de la chaine de caractère

mot = str(input("Veuillez choisir un mot"))
lc = len(mot)
mot2 = print(mot, "=>", mot[lc::-1]) 


binaire =  int(input("Veuillez rentrer un message en binaire : "))
