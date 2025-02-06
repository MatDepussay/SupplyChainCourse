
Ligne = [0,1,0]

for i in range(15):
    print(Ligne)
    nouvelleLigne = [0]
    for j in range(1,len(Ligne)):
        nouvelleLigne.append(Ligne[j-1]+Ligne[j])
    nouvelleLigne.append(0)
    Ligne = nouvelleLigne
