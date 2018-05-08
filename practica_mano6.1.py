n1 = float(input("pon un numero: "))
n2 = float(input("pon un numero: "))
n3 = float(input("pon un numero: "))
n4 = float(input("pon un numero: "))
n5 = float(input("pon un numero: "))

lista=[n1,n2,n3,n4,n5]

for i in range(len(lista) - 1):
    if lista[i] >= lista[i + 1]:
        mayor = lista[i]
    else:
        mayor = lista[i+1]
        if lista[i] <= lista[i - 1]:
            minimo = lista[i]
        else:
            minimo = lista[i-1]
            
        
print(mayor)
print(minimo)