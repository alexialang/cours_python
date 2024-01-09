

maxValue = 0
number = float(input("Veuillez saisir un nombre : "))
while number !=0 :
  if number!=0:
    number = float(input("Veuillez saisir un nombre : "))
    if number > maxValue:
      maxValue = number
  else:
    print(number)
    
print(f"Le chiffre le plus grand saisie est :{maxValue}")