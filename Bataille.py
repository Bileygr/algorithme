import random

def mélanger(paquet):
    k = 0
    while k < 49:
        i = random.randint(0,9)
        j = random.randint(0,9)
        temp = paquet[i]
        paquet[i] = paquet[j]
        paquet[j] = temp
        k = k+1
    return paquet

def partager(paquet):
    table = []
    paquetA = []
    paquetB = []
    i = 0
    while i < 10:
        if i % 2 == 0:
            paquetA.append(paquet[i])
        else:
            paquetB.append(paquet[i])
        i = i+1
    table.append(paquetA)
    table.append(paquetB)
    return table

def jouer(paquet):
    scoreA = 0
    scoreB = 0
    i = 0
    while i < 5:
        if paquet[0][i] > paquet[1][i]:
            scoreA = scoreA+1
        else:
            scoreB = scoreB+1
        i = i+1
    return "Score: A:"+str(scoreA)+" B:"+str(scoreB)

paquet = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Les cartes", paquet)
paquet_mélangé = mélanger(paquet)
print("Mélange des cartes", paquet_mélangé)
paquet_partagé = partager(paquet_mélangé)
print("Distribution: Cartes du joueur A", paquet_partagé[0],"Cartes du joueur B", paquet_partagé[1])
résultat = jouer(paquet_partagé)
print(résultat)
