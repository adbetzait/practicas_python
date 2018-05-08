# este programa determina si un clienten puede subirse a la medusa o no
#los parametros para que el cliente pueda subir son "que haya comprado boleto y que mida mas de 145 centimetros"

#1. preguntar si el cliente compro boleto o no
boleto = input("¿compro boleto?" "(si/no)= " )

#2. preguntar la estatura del cliente en centimetros
altura = input("¿cuantos centimetros mide?")

#3. verificar que la estatura sea mayor que 145 y que compro boleto

if boleto == "si" and altura >= "145" :
    print("puede pasar")
else:
    print("no puede pasar")
