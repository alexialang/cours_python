nombreA = int(input("Veuillez saisir le nombre de doigts du joueur A: "))
nombreB= int (input("Veuillez saisir le nombre de doigts du joueur B"))
 

a = nombreA +nombreB
nombre = a % 2

if(nombreA>=0 and nombreA<= 5)and(nombreB>=0 and nombreB<=5):
  if nombre == 0: 
   print("Félicitation A vous avez gagné!")
  else:
    print("Félicitation B vous avez gagné!")

 