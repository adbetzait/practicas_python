peso_tierra = float(input("¿cuanto pesas? "))
masa = peso_tierra / 9.81
gravedad = {"luna": "1.62","mercurio": "2.78","venus": "8.87","marte": "3.72","jupiter": "22.88","saturno": "9.05","urano": "7.77","neptuno": "11","pluton": "0.4"}
peso_otro_planeta = (input("¿en que planeta quiere saber su peso? "))
peso = masa * float(gravedad[peso_otro_planeta])

nombre = input("¿cual es tu nombre? ")

print(nombre, "tu pesas en", peso_otro_planeta, peso)