import random

print("**********BIENVENIDO AL ADIVINADOR***********")

limite = int(input("¿cual desea que sea el limite? "))
print("estara jugando entre los numeros del 1 al", limite)
numero = random.randint(1,limite)
print("************************************************************")
for i in range(1, limite + 1):
    intento = int(input("dame un numero"))
    if intento == numero:
        print("adivinaste")
        break
    print("intentalo de nuevo")
    print("intento #",i)

        

