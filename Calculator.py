number1 = number2 = ""

while not number1.isdigit() and number2.isdigit():
    number1 = input("Premier Nombre : ")
    number2 = input("Second Nombre : ")
    if not (number1.isdigit() and number2.isdigit()):
        print("Entrez deux nombres")

        print(
            f"Le résultat de {number1} avec {number2} est égal à {int(number1) + int(number2)}")

#nombres = [1, 21, 5, 45, 68, 2, 3, 98]
#nombres_pairs = [i for i in nombres if i % 2 == 0]
# print(nombres_pairs)

#

#nombres = range(-10, 10)
#nombres_positif = [i for i in nombres if i >= 0]
# print(nombres_positif)

#nombres = range(5)
#nombres_doubles = [i * 2 for i in nombres]
# print(nombres_doubles)

#nombres = range(10)
#nombres_inverse = [i if i % 2 == 0 else -i for i in nombres]
# print(nombres_inverse)
