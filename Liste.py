import sys

LISTE = ["YES HI", "NOP"]

MENU = """Faites un choix :
1: Ajouter
2 :Retier
3: Afficher la liste
4: Clear la liste
5: Quitter
Ton choix :"""

menu = ["1", "2", "3", "4", "5"]

while True:
    choix = ""
    while choix not in menu:
        choix = input(MENU)
        if choix not in menu:
            print("Choissis entre 1 et 5")

    if choix == "1":
        element = input("Entre une nouvelle valeur : ")
        LISTE.append(element)
        print(f"L'element {element} a bien été ajouté")

    elif choix == "2":
        element = input("Retirer une valeur : ")
        if element in LISTE:
            LISTE.remove(element)
            print(f"L'element {element} a bien été retirer")
        else:
            print(f"L'element {element} n'existe pas")

    elif choix == "3":
        if LISTE:
            print("Tema la quichta")
            for i, element in enumerate(LISTE, 1):
                print(f"{i}. {element}")
        else:
            print("Il y a rien dans ta liste de mort")

    elif choix == "4":
        LISTE.clear()
        print("La liste est bien effacé")

    elif choix == "5":

        print("C'est Tchao")
        sys.exit()

    print("-" * 100)
