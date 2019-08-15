# Calcul matriciel 15/08/2019.

def addition(a,b):
    resultat = []
    for i in range(len(a)):
        tuple_du_resultat = []
        for j in range(len(a[i])):
            calcul = a[i][j]+b[i][j]
            tuple_du_resultat.append(calcul)
        resultat.append(tuple_du_resultat)
    return resultat

def soustraction(a,b):
    resultat = []
    for i in range(len(a)):
        tuple_du_resultat = []
        for j in range(len(a[i])):
            calcul = a[i][j]-b[i][j]
            tuple_du_resultat.append(calcul)
        resultat.append(tuple_du_resultat)
    return resultat

def multiplication(a,b):
    resultat = []
    for i in range(len(a)):
        for j in range(len(a[i])):
            tuple_du_resultat = []
            for k in range(len(b)):
                total = 0
                for l in range(len(b[k])):
                    calcul = (a[i][l]*b[k][l])+total
                    total = calcul
                tuple_du_resultat.append(total)
        resultat.append(tuple_du_resultat)
    return resultat

matriceA = [[1,2,0],[4,3,-1]]
matriceB = [[5,2,3],[1,3,4]]
print(multiplication(matriceA,matriceB))
