a = int(input("Veuillez saisir un premier nombre : "))
b= int(input("Veuillez saisir un second nombre : "))

if (a== 0 and b==0):
  print("L'ensemble des solutions est l'ensemble R.")
elif(a==0 and b!=0):
  print("L'ensemble des solutions est l'ensemble vide.")
elif(a!=0):
  print(f"x=-{b}/{a}")

