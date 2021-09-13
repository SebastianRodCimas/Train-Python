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
    
    if enemie_vie <= 0:
    
    enemie_attaque = random.randint(5, 15)
    joueur_vie -= enemie_attaque
    print(f"On vous a infligé {enemie_attaque} points de dégats ")
    
    if joueur_vie <= 0:
    
    
    
    print(f"Il vous reste {joueur_vie} points de vie.")
    print(f"Il lui reste {enemie_vie}")
    print("-" * 100)
    
    
    
        
print("Fin du jeu")