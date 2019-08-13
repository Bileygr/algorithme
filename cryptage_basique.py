# Cet algorithme permet de crypter des chaines de caractere.

def crypter(chaine_de_caractere):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cle = 11
    chaine_de_caractere = chaine_de_caractere.upper()
    chaine_de_caractere_crypte = ""
    
    for caractere in chaine_de_caractere:
        for i in range (len(alphabet)):
            if caractere == alphabet[i]:
                r = (i*cle)%26
                chaine_de_caractere_crypte += alphabet[r]
    return chaine_de_caractere_crypte

chaine_de_caractere = input("Veuillez saisir la chaine de caractere que vous voulez crypter: ")
print("Chaine de caractere crypte:",crypter(chaine_de_caractere))
