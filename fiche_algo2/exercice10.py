temperature_amb = float(input("Veuillez saisir la température ambiante : "))
temperature_bassins = float( input("Veuillez saisir la température des bassins de refroidissement : "))

a = abs(temperature_amb - temperature_bassins)

if (a < 20 or a > 40) :
  print("Alerte !!!!")
else :
  print("La température est normale")