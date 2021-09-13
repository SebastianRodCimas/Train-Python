import random

enemie_vie = 50
joueur_vie = 50
nombre_potions = 3
skip_tour = False

while True:
    if skip_tour:
        print("Tu passes ton tour")
        skip_tour = False
    else:
        choix = ""
        while choix not in ["1", "2"]:
            choix = input("Attaque ou Potion ?")
        if choix == "1":
            joueur_attaque = random.randint(5, 10)
            enemie_vie -= joueur_attaque
            print(f"Tu as mis {joueur_attaque} a l'enemi ")
        elif choix == "2":
            if nombre_potions > 0:
                potion_vie = random.randint(15, 50)
                joueur_vie += potion_vie
                nombre_potions -= 1
                skip_tour = True
                print(
                    f"Tu reçois {potion_vie} points de vie , il te reste {nombre_potions}")
            else:
                print("Tu n'as plus aucune potions !")
                continue

    if enemie_vie <= 0:
        print("Tu as gagné l'octogone")
        break

    enemie_attaque = random.randint(5, 15)
    joueur_vie -= enemie_attaque
    print(f"On vous a infligé {enemie_attaque} points de dégats ")

    if joueur_vie <= 0:
        print("T'as perdu, sad")
        break

    print(f"Il vous reste {joueur_vie} points de vie.")
    print(f"Il lui reste {enemie_vie}")
    print("-" * 100)


print("Fin du jeu")
