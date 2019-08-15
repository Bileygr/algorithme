from cryptage_basique import crypter
import os

def obtenir_le_contenu_du_fichier(nom_du_fichier):
  if os.path.exists(nom_du_fichier):
    fp = open(nom_du_fichier, "r")
    contenu = fp.read()
    fp.close()
    return contenu

contenu = obtenir_le_contenu_du_fichier("The laws of robotics.txt")
print(contenu, '\n', '\n', crypter(contenu))
