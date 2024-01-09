# contrôler que les notes sont comprises entre 0 et 20 et que les coefficients sont compris
# entre 1 et 10.



erreur = "Veuillez saisir un nombre compris entre 0 et 20"
erreur2 = "Veuillez saisir un coeff compris entre 1 et 10"
fr = -1
math = -1
geom =-1
info = -1
coeff_fr=0 
coeff_geom = 0 
coeff_math = 0 
coeff_info = 0

while fr < 0 or fr > 20:
  fr = float(input("Veuillez saisir votre note de français : "))
  if fr < 0 or  fr > 20:
    print(erreur)
while coeff_fr < 1 or coeff_fr> 10:
  coeff_fr = int(input("Veuillez précisez le coefficient de français : "))
  if coeff_fr <1 or coeff_fr>10:
    print(erreur2)
note_fr = fr*coeff_fr

while math < 0 or math > 20: 
  math = float(input("Veuillez saisir votre note de math : "))
  if math < 0 or math > 20:
    print(erreur)
while coeff_math < 1 or coeff_math> 10:
  coeff_math = int(input("Veuillez préciser le coefficient de math : "))
  if coeff_fr <1 or coeff_fr>10:
    print(erreur2)
note_math = math*coeff_math
 
 
while geom < 0 or geom > 20:
  geom = float(input("Veuillez saisir votre note de geométrie : "))
  if geom < 0 or geom > 20:
    print(erreur)
while coeff_geom < 1 or coeff_geom> 10:
  coeff_geom = int(input("Veuillez préciser le coefficient de géométrie : ")) 
  if coeff_geom < 1 or coeff_geom>10:
    print(erreur2)   
note_geom = geom* coeff_geom

while info < 0 or info > 20:
  info = float(input("Veuillez saisir votre note de informatique: "))
  if info < 0 or info > 20:
    print(erreur)
while coeff_info < 1 or coeff_info> 10:
  coeff_info = int(input("Veuillez préciser le coefficient d'informatique : ")) 
  if coeff_info <1 or coeff_info>10:
    print(erreur2)  
note_info = info*coeff_info

moyenne= (note_fr +  note_math +  note_geom +  note_info) / (coeff_fr + coeff_math + coeff_geom + coeff_info )

if moyenne>=16:
  print(f"Votre Moyenne est de {round(moyenne),2}/20 , Très bien ")
elif(moyenne >= 12 and moyenne <16):
  print(f"Votre moyenne est de {round(moyenne,2)}/20 , Bien")
elif (moyenne >= 8 and moyenne <12):
  print(f"Votre moyenne est de {round(moyenne),2}/20 , Assez bien")
elif (moyenne >= 4 and moyenne <8):
  print(f"Votre moyenne est de {round(moyenne),2}/20 , Insuffisant")
elif moyenne < 4 :
  print(f"Votre moyenne est de {round(moyenne),2}/20 , Nul")

  
  