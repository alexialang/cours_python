age = int(input("Quel âge avez-vous ?"))
statut =""

tarif = 0
forfait = ""

typeForfait = int(input("Voulez-vous un forfait à la journée(tapez 1) ou à la saison(tapez 2)"))
if age > 12 and age < 60:
  statut ="adulte"
elif age < 12:
  statut ="enfant"
else:
  statut = "senior"
  
if statut =="enfant" and typeForfait ==1:
  tarif=18.70
elif statut == "enfant" and typeForfait ==2:
  tarif = 300
elif statut == "adulte" and typeForfait == 1:
  tarif= 25.80
elif statut == "adulte" and typeForfait == 2:
  tarif = 510
elif statut =="senior" and typeForfait ==1:
  tarif = 21.40
elif statut == "senior" and typeForfait ==2:
  tarif = 340
  
if typeForfait == 1:
  forfait = "1 journéee"
elif typeForfait ==2:
  forfait = "saison"
   
  
print (f"Le prix pour un {statut} est de {tarif} euros pour {forfait}")

