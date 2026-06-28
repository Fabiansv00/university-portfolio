#Diccionarios 

from numpy import rint


print ("____________________________________________________________________________________________________________________________________________________")
print ("--Crear un diccionario--")
Datos = {"Nombre":"Juan",  #Key <- : Value
         "Apellido":"Perez",
         "Edad":30,
         "Ciudad":"Alajuela",
         "Deporte Favorito":"Futbol",
         "mayor de edad": True  
         }
print(Datos) #esto va a imprimir el diccionario completo
print ("____________________________________________________________________________________________________________________________________________________")

#seleccionar un valor del diccionario
print ("____________________________________________________________________________________________________________________________________________________")
print ("--Seleccionar un valor del diccionario--")
print(Datos["Nombre"]) #esto va a imprimir el valor de la key "Nombre"
print ("____________________________________________________________________________________________________________________________________________________")

#Agregar

print ("____________________________________________________________________________________________________________________________________________________")
print ("--Agregar una nueva key y valor al diccionario--")
Datos["Genero"] = "Masculino" #esto va a agregar una nueva key "Genero" con el valor "Masculino"
print(Datos) #esto va a imprimir el diccionario completo con la nueva key y valor
print ("____________________________________________________________________________________________________________________________________________________")

#Eliminar una key y valor del diccionario
print ("____________________________________________________________________________________________________________________________________________________")
print ("--Eliminar una key y valor del diccionario--")
Datos.pop("Ciudad") #esto va a eliminar la key "Ciudad" y su valor
print(Datos) #esto va a imprimir el diccionario completo sin la key "Ciudad" y su valor
print ("____________________________________________________________________________________________________________________________________________________")

#frutas: limon, sandía, pera, uvas, kiwui, piña, fresas, arandanos, banana y mango
##1 - AGREGAR UNA NUEVA FRUTA AL FINAL: COCO listo
#2 - AGREGAR UNA NUEVA FRUTA AL INICIO : GUAYABA listo
#3 - AGREGAR UNA NUEVA FURTA AL FINAL: ARANDA listo
#4 - MODIFICAR LA FRUTA ARAND -> ARANDANOS listo
#5 - ELIMINAR LA FRUTA: SANDÍA listo
#6 - ELIMINAR E IMPRIMIR LA FRUTA ELIMINADA EN LA POS 2 LISTO
#7 - IMPRIMIR LA CANTIDAD DE ELEMENTOS DE LA Lista
#8 - SELECCIONAR LA FRUTAS DESDE LA POSIC 2->8 listo
#9 - SELECCIONAR FRUTAS HASTA LA POSIC 5 listo
#10 - SELECCIONAR FRUTAS DESDE LA POSIC 8 listo
#11 - SELECCIONAR FRUTAS DESDE LA POSI 4:6 listo
#12 - SELECCIONAR LA ULTIMA FRUTA DE LA LISTA [DEBE DE UTILIZAR LA FUNCION LEN]

Frutas = ["limon", "sandía", "pera", "uvas", "kiwui", "piña", "fresas", "arandanos", "banana", "mango"]
print(Frutas)
Frutas.append("coco") #agregar al final
print(Frutas)    
Frutas.insert(0, "guayaba") #agregar al inicio
print(Frutas)
Frutas.append("arandano") #agregar al final
print(Frutas)
Frutas[7] = "arandanos" #modificar
print(Frutas)
Frutas.remove("sandía") #eliminar por nombre
print(Frutas)
Frutas.pop(2) #eliminar por posición e imprimir la fruta eliminada
frutas_eliminadas = Frutas.pop(2)
print("Fruta eliminada:", frutas_eliminadas) #imprimir la fruta eliminada
print(Frutas)
print("Cantidad de frutas:", len(Frutas)) #cantidad de elementos
print(Frutas[2:8]) #seleccionar frutas desde la posición 2 hasta la posición 7
print(Frutas[:5]) #seleccionar frutas hasta la posición 4
print(Frutas[8:]) #seleccionar frutas desde la posición 8 hasta el final
print(Frutas[4:6]) #seleccionar frutas desde la posición 4 hasta la posición 5
print(Frutas[len(Frutas)-1]) 

#seleccionar la última fruta de la lista utilizando la función len para obtener la posición de la última fruta
#el -1 es porque las posiciones empiezan desde 0, entonces la última posición es len(Frutas)-1  lo leemos 1-10 pero python lo lee 0-9
# Uso print(Frutas[len(Frutas)-1]) para imprimir la última fruta de la list 
# la funion del -1 es para indicar que queremos la última posición de la lista, ya que len(Frutas) nos da el número total de elementos, 
# pero las posiciones empiezan desde 0, entonces la última posición es len(Frutas)-1.
#si pusiera -2 imprimiría la penúltima fruta de la lista, y así sucesivamente.