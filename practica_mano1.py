nombre = input("cual es tu nombre? ")
sexo = input("cual es tu sexo? ")
nacimiento = float(input("año de nacimoento"))

if nacimiento <=2000:
    print("puede votar")
else:
    print("no puede votar")