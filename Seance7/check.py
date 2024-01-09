while True:
  try:
    note = int(input("Saisir une note (/20) : "))
    
    if 0<= note <= 20:
      break
    print("Votre note doit être comprise entre 0 et 20 ")
  except ValueError:
    print("Votre saisie est invalide")