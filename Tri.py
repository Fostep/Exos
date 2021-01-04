
#Tri par sélection
def selectTri(liste):
  taille = len(liste)

  print(liste)

  for i in range(0, taille):
    min = i

    for j in range(i, taille):
      if(liste[min] > liste[j]):
        min = j

    temp = liste[i]
    liste[i] = liste[j]
    liste[j] = temp

  print(liste)

#Tri par fusion 
def fusion(gauche, droite):
  res = []
  i = 0
  j = 0

  while i < len(gauche) and j < len(droite):
    if(gauche[i] < droite[j]):
      res.append(gauche[i])
      i = i+1
    else:
      res.append(droite[j])
      j = j+1

  if(gauche):
    res.extend(gauche[i:])
  if(droite):
    res.extend(droite[j:])
  
  return res

def tri_fusion(tab, debut, fin):
  if(len(tab) <= 1):
    return tab
  else:
    milieu = (debut + fin)//2
    #Decoupe gauche et droite
    gauche = tab[:milieu]
    droite = tab[milieu:]

    #On continue de decouper ce qu'on à déjà découper
    gauche = tri_fusion(gauche, 0, len(gauche))
    droite = tri_fusion(droite, 0, len(droite))

    return fusion(gauche, droite)
