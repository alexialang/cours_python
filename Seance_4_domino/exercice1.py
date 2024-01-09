# Alain et Catherine organisent une soirée pour des membres de leur club informatique.
# Ils décident que pour être invité il faut :

# - être ami d’Alain et de Catherine ;
# - ou ne pas être ami d’Alain, mais être ami de Catherine ;
# - ou ne pas être ami de Catherine, mais jouer au bridge.

# Pour un membre quelconque, on définit les variables booléennes suivantes par :
# a = 1 s’il est un ami d’Alain,
# b = 1 s’il joue au bridge,
# c = 1 s’il est un ami de Catherine.

print(" Quel est votre situation, Veuillez rentrez 0 pour Non et 1 pour oui")

a = int(input(" Etes vous amis avec Alain, oui= 1 non = 0 : "))
b = int(input("Jouez vous au bridge oui = 1 non = 0 : "))
c = int(input("Etes vous un ami de catherine oui= 1  non = 0 : "))

if (a == 1 and c==1) or (a!= 1 and b== 1) or (c!=1 and b == 1) : 
  print(" Vous êtes invité")
else : print("Vous n'etes pas invité")

  
