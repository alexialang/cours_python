# Jean a un livret A avec 2000 euros dessus au taux d’intérêt de 2%
# - Ecrire un programme pour savoir combien il aura dans 10 ans
# - Modifier le programme pour pouvoir choisir le taux d’intérêt et le nombre d’années

  
livret = 2000

interet = float(input("Veuillez renseignez le taux d'interet: "))

annee = int(input("Veuillez renseigner le nombre d'années: "))

for i in range (annee):
  livret = livret + livret * interet/100

print(f"La valeur du livret au bout de {annee} ans et de {livret} euros")
  

