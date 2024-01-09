fr = float(input("Veuillez saisir votre note de français : "))
math = float(input("Veuillez saisir votre note de math : "))
geom = float(input("Veuillez saisir votre note de geométrie : "))
info = float(input("Veuillez saisir votre note de informatique: "))

moyenne = (fr + math + geom + info)/4

if moyenne>=16:
  print(f"Votre Moyenne est de {moyenne}/20, Très bien ")
elif(moyenne >= 12 and moyenne <16):
  print(f"Votre moyenne est de {moyenne}/20, Bien")
elif (moyenne >= 8 and moyenne <12):
  print(f"Votre moyenne est de {moyenne}/20, Assez bien")
elif (moyenne >= 4 and moyenne <8):
  print(f"Votre moyenne est de {moyenne}/20, Insuffisant")
elif moyenne < 4 :
  print(f"Votre moyenne est de {moyenne}/20, Nul")