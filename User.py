for i in range(1, 11):
    print(f"User {i}")

mot = "Ban"

for lettre in reversed(mot):
    print(lettre)

next = "Oui"
while next == "Oui":
    print("Slt")
    result = input("Sa continue ? Oui/Non")
    if result != "Oui":
        break
