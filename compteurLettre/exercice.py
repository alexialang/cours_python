# lettre = str(input("Veuillez choisir une lettre a chercher : "))
# texte = str(input("Veuillez saisir le texte dans lequel vous voulez recherche cette lettre : \n").lower())

  
# print(texte.lower().count(lettre))

# nombreDeLettre = 0
# for i in (texte):
#   if i == lettre:
#     nombreDeLettre = nombreDeLettre + 1
  
# print(nombreDeLettre)

# lettre la plus présente dans le texte

texte = str(input("Veuillez saisir le texte dans lequel vous voulez recherche cette lettre : \n").lower().replace(" ",""))
dico={}

for i in texte:
  if i in dico:
    dico[i] +=1
  else:
    dico[i]=1

maxValue = 0

for i in dico:
  if maxValue == 0 :
    maxValue = {i:dico[i]}
  for j in maxValue:
    if dico[i]>maxValue[j]:
      maxValue = {i:dico[i]}
      
print(maxValue)