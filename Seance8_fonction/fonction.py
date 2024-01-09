# def est_pair(n):
#   if n%2 == 0:
#     print(f"{n} est pair")
#   else :
#     print(f"{n} est impair")
    
# n= 3
# est_pair()

# def somme (x,y):
#   n=x+y
#   return n
  
# res = somme(3,2)
# print(res)



def somme_liste (tableau):
  n=0
  for i in range (len(tableau)):
    n+= tableau[i] 
  return n 

tableau = [1, 2, 3]
res = somme_liste(tableau)
print(res)


#  fontion verification
# def verif_saisie_note():
#   while True:
#     try:
#       note =float(input("Saisir une note sur 20:"))
      
#       if not (0 <= note <=20):
#         raise Exception
      
#       return note
#     except ValueError:
#       print("Saisi invalide !")
#     except Exception:
#       print("La note doit être comprise entre 0 et 20.")
  

# # Début du programme
# nb_notes = int(input("Combien de notes ?"))
# notes = []
# for i in range (nb_notes):
#   notes += [verif_saisie_note()]
