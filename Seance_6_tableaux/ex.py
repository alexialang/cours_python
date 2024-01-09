tab_matiere = ["math","geo"]
tab = [[15,8],[12,11]]
tab_moyenne = []

for i in range (len(tab)):
  for j in range (len(tab[i])):
      note = tab[i][j]
      if j == 0:
        tab_moyenne = [note]
      else :
        tab_moyenne += [note]
    
print(tab_moyenne)