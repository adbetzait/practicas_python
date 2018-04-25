pregunta = input("¿que area desea sacar, cuadrado, circulo o trinagulo?")

if pregunta == "cuadrado":
    print("deme los datos por favor")
    lado = float(input("lado: "))
    print("esta es su area: ", lado * lado)
elif pregunta == "circulo":
    print("deme los datos por favor")
    radio = float(input("radio: "))
    print("esta es su area: ", radio * radio * 3.1416)
elif pregunta == "triangulo":
    print("deme los datos por favor")
    base = float(input("base: "))
    altura = float(input("altura: "))
    print("esta es su area: ", base * altura / 2)
    




    