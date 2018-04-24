#1.crea cuantas variavbles quieras de tipo string y asigna el nombre de un amigo tuyo a cada variable
amigo1 = "ivan"
amigo2 = "jesus"
amigo3 = "pepe"
amigo4 = "ximena"
amigo5 = "andrea"

#2. inserta estas variables a una nueva lista que se llame "amigos" 

amigos = []
amigos.append(amigo1)
amigos.append(amigo2)
amigos.append(amigo3)
amigos.append(amigo4)
amigos.append(amigo5)

#3. imprime un mensaje que indique al usuario cuantos elementos contiene la lista de amigos. se debe utilisar la funcion len()

x = len(amigos)
print ("numero de amigos que tengo:", x)

#4. imprime el primer elemento de la liste de amigos todo en mayusculas utilizando funciones de strings de python

mayusculas = amigo1.upper()
print (mayusculas)

#5. almacena en una variable el valor del tercer caracter del segundo elemento de tu lista de amigos

y = amigo2 [2]
print(y)

#6.crea una lista que contenga 5 numeros aleatorios

numeros = [7,5,8,3,9]

#7. en una sola linea de codigo, imprime el reultado de la suma de estos 5 numeros

print(numeros[0]+ numeros[1]+numeros[2]+numeros[3]+numeros[4])

#8. agraga 3 numeros nuevos a la lista de numeros

numeros.append(1)
numeros.append(2)
numeros.append(3)

#9. en una sola linea de codigo imprime el resultado de la multiplicacion de estos 5 numeros

print(numeros[0]*numeros[1]*numeros[2]*numeros[3]*numeros[4])

#utilizando esa misma lista de numeros,experimenta con las funciones sort(), reverse(), pop(), y count()

#sort

numeros.sort()
print(numeros)

#reverse

numeros.reverse()
print(numeros)

#pop

numeros.pop(2)
print(numeros)

#count
numeros.count(3)
print(numeros)

#parte 2
#crea un diccionaria que contenga el nombre de 5 paises como llave, y sus capitales como valor

paises = {"mexico":"cdmx", "españa":"madrid", "francia":"paris", "argentina":"buenos_aires", "peru":"peru"}

#imprime un re sultado de lea "x es la capital de Y" donde x es el valor de la llave y Y es la llave 


print(paises["mexico"], "es la capital de mexico")

#crea un diccionaria que contenga nombres de estados como llaves y sus capitales como valor

estados = {"oaxaca":"oaxaxa_de_juares", "sonora": "hermosillo", "zacatecas":"zacatecas", "puebla":"puebla_de_zaragoza", "colima":"colima"}

#crea un diccionario con el nombre de "diccionario" que tenga como llave un numero entero y por valor cada uno de los dos diccionaris creados anterior mente

diccionario = {1:paises,2:estados}

# imprime todos los valoeres de diccionario como hiciste en el punto 2

print(diccionario[1]["mexico"], "es la capital de mexico")



