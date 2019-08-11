def A1():
    note_option = int(input("Histoire des arts : "))
    if note_option < 10:
        points_gagnés = 0
    else:
        points_gagnés = note_option-10
    points_gagnés = points_gagnés*2
    return points_gagnés

def A2():
    noms=["Français", "Mathématiques", "Histoire_géographie", "LV1", "LV2", "Physique", "Technologie"]
    notes = []
    coefficients = [3, 3, 2, 2, 1, 2, 1]
    total_des_coefficients = 0
    total_des_notes = 0

    print("Veuillez entrer vos notes.")
    for i in range(len(coefficients)):
        note = int(input(noms[i]+" : "))
        notes.append(note)
        total_des_coefficients = total_des_coefficients+coefficients[i]
        total_des_notes = total_des_notes+(notes[i]*coefficients[i])
        
    note_option = A1()
    total_des_notes = total_des_notes+note_option
    note_final = int(total_des_notes/total_des_coefficients)

    if note_final >= 10 and note_final < 12:
        return "Vous êtes reçu avec "+str(note_final)+" de moyenne et la mention 'Passable'."
    elif note_final >= 12 and note_final < 14:
        return "Vous êtes reçu avec "+str(note_final)+" de moyenne et la mention 'Assez Bien'."
    elif note_final >= 14 and note_final < 16:
        return "Vous êtes reçu avec "+str(note_final)+ "de moyenne et la mention 'Bien'."
    elif note_final >= 16:
        return "Vous êtes reçu avec "+str(note_final)+" de moyenne et la mention 'Très Bien'."
    
print(A2())
    
