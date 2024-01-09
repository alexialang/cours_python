date = input("Saisir la date au formart AAAA/MM/JJ")

tab_mois = ["janvier","février","mars","avril","mai","juin","juillet","aout","septembre","octobre","novembre","décembre"]
tab_jour = ["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]

annee = int(date[0]+ date[1] + date[2]+ date[3])
mois = int(date[5] + date[6])
jour = int(date[8]+ date[9])

if mois == 1 or mois == 2:
  annee -=1 
  mois += 12
    

n = jour + int((13*mois+3)/5) + int(5 * annee /4)- int(annee/100) +int(annee/400)
n = (n%7)

if n == 0:
  print("Lundi")
elif n == 1:
  print("Mardi")
elif n == 2:
  print("Mercredi")
elif n == 3:
  print("Jeudi")
elif n == 4:
  print("Vendredi")
elif n == 5:
  print ("Samedi")
elif n == 6:
  print("Dimanche")

print(f"Le {jour} {tab_mois[mois-1]} {annee} est un {tab_jour[n]}")

