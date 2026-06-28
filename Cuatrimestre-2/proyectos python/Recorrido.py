#pedir un numero que son la veces que hace el cliclo y en caa interaccion pide uno nuevo
#recorrer el numero del usuariuo, pedir 5 veces el numero
#primero numero 4 segundo numero 2 tercer numero.... quinta vez 8
#la suma de los numeros digitados son :

vueltas = int(input("Ingrese el numero de vueltas que desea realizar: "))
suma = 0
numeros = []

for i in range(vueltas):
    numero = int(input(f"Ingrese el numero de la vuelta {i+1}: "))
    numeros.append(numero)
    suma += numero
    
print(f"La suma total de los numeros {numeros} es {suma}")

#pedir al usauruo que digite una letra de la a ala z
#y independientemente si puso A en minuscula o mayuscula tiene que hacer que sea igual
#cuente la cantidad de ocurrencias que el usuario digito 