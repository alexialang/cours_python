print("\nAppelez la personne avec qui vous voudriez etre ami ")
erreur = "Erreur. Veuillez saisir oui ou non"

appel = ""

while  appel != "oui" and appel != "non":
  appel = (input("La personne vous a t'elle repondu : oui ou non ? \n"))
  if appel == "oui":
    print("\nProposez lui un repas.")
  elif appel =="non":
    print("\nMince, Attendez qu'elle vous rapelle et proposez lui un repas")
  else:
    print(erreur)
  
reponse =""
verre = ""
interet= ""

while reponse != "oui" and reponse !="non":
  reponse = (input("La personne accepte t'elle ce repas : oui ou non: \n"))
  if reponse == "oui":
      print("Vous devenez amie \n")
  elif reponse != "oui" and reponse !="non":
    print(erreur)
  elif reponse == "non" : 
    print("\nC'est pas grave, proposez lui plutot d'aller boire un verre.")
    while verre != "oui" and verre !="non":
      verre = (input("Et elle d'accord pour aller boire un verre avec vous: oui ou non ? : \n"))
      if verre == "oui":
        print("\nProposez lui d'aller boire un café un thé ou un coca !")
        print("Vous êtes amie !!!")
      elif verre!="oui" and verre!="non":
        print(erreur)
      elif reponse == "non": 
        activite = ("Choissisez une activité a proposer a notre futur amie :") 
        print(f"\nNotre futur amie aime t'elle l'activité :")
        while interet != "oui" and interet !="non":
          for n in range (6):
            interet= (input("Partagez vous ce nouveau centre d'interet : oui ou non ?"))
            if interet == "non":
              if n == 5:
                print("\nChoissisez l'activité qui vous plait le plus \nPartagez un interet\nDevenez amie\n")
            elif interet == "oui":
              print("\nSuper profitez en pour faire cette activitée ensemble\nVous êtes amie !!")
              break
            else:
              print(erreur)



  

      