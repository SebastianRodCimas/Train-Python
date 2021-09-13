import random
nombre_trouver = random.randint(0, 100)
nombre_essaie = 5

print("Petit jeu sympatoche")

while nombre_essaie > 0:
    print(
        f"Il te reste {nombre_essaie} essaie {'s' if nombre_essaie > 1 else ''}")

    choix = input("Devine le bon nombre ")
    if not choix.isdigit():
        print("Entrer un nombre entuer")
        continue

    choix = int(choix)

    if nombre_trouver > choix:
        print(f"Le bon nombre est plus grand que {choix}")
    elif nombre_trouver < choix:
        print(f"Le bon nombre est plus petit que {choix}")
    else:
        break
    nombre_essaie -= 1


if nombre_essaie == 0:
    print("T'as perdu, le nombre était {nombre_trouver}")
else:
    print("Bien joué, le nombre est bien {nombre_trouver}")
    print(f"Tu l'as trouvé en {6 - nombre_essaie} essaie")

print("Fin de la partie")
