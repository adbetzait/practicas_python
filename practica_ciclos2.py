contactos = ["beto|9513582566","martin|951234757"]
accion = 0
while accion !=3:
    print("************MENU***********")
    print("si quiere crear nuevo contacto oprima la tecla 1")
    print("si quiere ver sus contactos oprima la tecla 2")
    print("si quiere salir oprima la tecla 3")
    accion= int(input())
    if accion == 1:
        nombre = input("nombre?")
        numero = input("numero?")
        dato = nombre + "|" + numero
        contactos.append(dato)
    elif accion == 2:
        print(contactos)
    else:
        print("ADIOS")
        