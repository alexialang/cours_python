for i in range(0,5):
  print(i)

mot = "Hello"
for lettre in mot:
  print(lettre)

# 
mot = "Hello"

for i in range (0,len(mot)):
  print(mot[i])

# Exercice
# faire un algo qui permet de dire si un mot est un palindrome (ex kayak)
#  interdit d'utiliser list  mot[::-1 ] string.reverse()

mot = "kayak"
motInverse = ""

for i in range (0,len(mot)):
  motInverse =  mot[i] + motInverse


if mot == motInverse:
  print("Palindrome")
else:
  print(" Non ")
