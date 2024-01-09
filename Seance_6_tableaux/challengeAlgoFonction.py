# #  fontion verification
# def verif_saisie_note():
#   while True:
#     try:
#       note =float(input("Saisir une note sur 20:"))
      
#       if not (0 <= note <=20):
#         raise Exception
      
#       return note
#     except ValueError:
#       print("Saisi invalide !")
#     except Exception:
#       print("La note doit être comprise entre 0 et 20.")
  

# # Début du programme
# nb_notes = int(input("Combien de notes ?"))
# notes = []
# for i in range (nb_notes):
#   notes += [verif_saisie_note()]


# demander le nombre de matières à saisir
nombreMatiere = int(input("Combien de matière avait vous à saisir : "))
# stocker le nom des matières
tab_matiere = []

for i in range (nombreMatiere):
  matiere = input("Veuillez saisir une matière : ")
  tab_matiere +=  [matiere]
 
  
# demander le nombre d'élève
nombre_eleve = int(input("Combien d'élèves y a t'il : "))

# stocker le nom et prénoms des élèves
# attribué les notes
# moyenne general élèves
tab_nom = []
tab_prenom = []
eleves = {}
moyenne_matiere = {}
note =-1


for i in range (nombre_eleve):
  moyenne = 0
  prenom = input(f"Veuillez saisir le prénom de l'élève {i+1}: ")
  nom = input(f"Veuillez saisir le nom de l'élève {i+1} : ")
  tab_prenom += [prenom]
  tab_nom += [nom]
  eleves[f"{nom}_{prenom}"] = {}


  while note >= 0  and note <= 20:
    for j in range (nombreMatiere):
        if note <0 and note > 20:
          print("Saisie Invalide")
          note = float(input(f"Veuillez saisir la note de {nom} {prenom} pour le cours de {tab_matiere[j]}: "))
        else:
          note = float(input(f"Veuillez saisir la note de {nom} {prenom} pour le cours de {tab_matiere[j]}: "))
          eleves[f"{nom}_{prenom}"][tab_matiere[j]] = note
          moyenne += note

          if i == 0 :
            moyenne_matiere[tab_matiere[j]] = note
          else :
            moyenne_matiere[tab_matiere[j]] += note
  
  eleves[f"{nom}_{prenom}"]["moyenne"] = moyenne/nombreMatiere

# afficher tous les élèves avec leur moyenne générales et leurs notes par matières
# stocker le nom du meilleur élève
# stocker le nom du pire élève
meilleur_eleve = {}
pire_eleve = {}
for i in eleves:
  
  if not meilleur_eleve :
    meilleur_eleve = {i:eleves[i]["moyenne"]}
  elif not pire_eleve :
    pire_eleve = {i:eleves[i]["moyenne"]}
  elif meilleur_eleve != 0:
    key = meilleur_eleve.keys()
    if meilleur_eleve[key[0]] < eleves[i]['moyenne'] :
      meilleur_eleve = {i:eleves[i]["moyenne"]}  
  elif pire_eleve != 0:
    key = pire_eleve.keys()
    if pire_eleve[key[0]] < eleves[i]['moyenne'] :
      pire_eleve = {i:eleves[i]["moyenne"]}  

  print(f'élèves {i} : ', end=" ")
  for j in eleves[i]:
    print(f'{j} = {eleves[i][j]} ', end=" ")

# afficher la moyenne de la classe par matière
for i in moyenne_matiere:
  moyenne_matiere[i] = moyenne_matiere[i]/nombre_eleve
  print(f'moyenne de la classe {i} : {moyenne_matiere[i]}', end=" ")
print()

# donner le nom du meilleur élève
# donner le nom du pire élève
print(f'meilleur elève : {meilleur_eleve} , pire élève : {pire_eleve}')