pares = []
suma = 0
#pedir un numero que son la veces que hace el cliclo y en caa interaccion pide uno nuevo
#recorrer el numero del usuariuo, pedir 5 veces el numero
#primero numero 4 segundo numero 2 tercer numero.... quinta vez 8
#la suma de los numeros digitados son :



for numero in range(1, 26):
    if numero % 2 == 0:
        pares.append(numero)
        suma += numero
        
print(f"La cantidad de numeros pares es: {len(pares)}")
print(f"Los numeros pares son: {pares}")
print(f"La suma de todos los pares es: {suma}")

#f-string


#Sin f-string tengo que separar todo con comas:
#print("La cantidad es:", len(pares))

#Con f-string metés la variable directamente dentro del texto con {}:
#pythonprint(f"La cantidad es: {len(pares)}")

#Sin f-string sería:
#pythonprint("Me llamo", nombre, "y tengo", edad, "años")
# Con f-string
#print(f"Me llamo {nombre} y tengo {edad} años")