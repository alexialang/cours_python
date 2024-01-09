prixTTC = float(input("Veuillez saisir le prix de votre article : "))

remise =0

if (prixTTC >= 500 and prixTTC <1000):
  remise = 2
elif(prixTTC >= 1000 and prixTTC <2000):
  remise = 5
elif(prixTTC >= 2000):
  remise = 10
else : print("Vous n'avez pas le droit a une remise")

print(f"Vous avez le droit a une remise de {remise} % , votre article a {prixTTC} euros passe a {(prixTTC-prixTTC*10/100)}")