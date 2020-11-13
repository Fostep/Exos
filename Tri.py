
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
def fusion(gauche,droite):
    resultat = []
    index_gauche, index_droite = 0, 0
    while index_gauche < len(gauche) and index_droite < len(droite):        
        if gauche[index_gauche] <= droite[index_droite]:
            resultat.append(gauche[index_gauche])
            index_gauche += 1
        else:
            resultat.append(droite[index_droite])
            index_droite += 1
    if gauche:
        resultat.extend(gauche[index_gauche:])
    if droite:
        resultat.extend(droite[index_droite:])
    return resultat
     
def tri_fusion(m):
    if len(m) <= 1:
        return m
    milieu = len(m) // 2
    gauche = m[:milieu]
    droite = m[milieu:]
    gauche = tri_fusion(gauche)
    droite = tri_fusion(droite)
    return list(fusion(gauche, droite))
