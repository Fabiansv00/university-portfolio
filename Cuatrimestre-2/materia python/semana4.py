# =========================================================================================================================================
# MI LISTA - OPERACIONES Y CONVERSIONES
# =========================================================================================================================================
my_lista = ["A", "B", "C", "D", "A", "B", "B", "D", "E", "D"]

print(" ")
print(" ")
print("=========================================================================================================================================")

# 1. Cantidad total de elementos
# Para hacer un print de la cantidad de elementos se ve con len(my_lista) y que diga cuántos elementos hay
print("Cantidad de elementos en la lista:", len(my_lista)) # Me imprime la cantidad de elementos en la lista
print("Mi lista es:", my_lista) # Imprime la lista original

# 2. Cantidad de elementos diferentes
# La cantidad distinta de elementos diferentes se ve con set(my_lista) y que diga cuántos elementos diferentes hay
my_set = set(my_lista) # Convierte la lista a un set para eliminar los elementos
print("La Cantidad de elementos diferentes es:", len(my_set)) # Imprime la cantidad de elementos diferentes en el set

# 3. Eliminar elementos repetidos
# Para remover los repetidos vamos a usar set(my_lista) y que diga la lista sin repetidos
lista_sin_repetidos = list(set(my_lista)) # Convierte el set a una lista para eliminar los elementos repetidos
print("la lista sin elementos repetidos:", lista_sin_repetidos) # Imprime la lista sin elementos repetidos

# El proceso es que la list agarra el set y lo convierte a una lista para eliminar los elementos repetidos, 
# el set elimina los elementos repetidos y luego la lista lo convierte a una lista para imprimirlo sin repetidos
print("=========================================================================================================================================")
print(" ")
print(" ")


# =========================================================================================================================================
# MI DICCIONARIO
# =========================================================================================================================================
my_diccionario = {
    "Nombre" : "Juan",
    "rol" : "Estudiante",
    "nacionalidad" : "Costarricense",
    "mayor_de_edad" : True
}


# =========================================================================================================================================
# MI SET - PROPIEDADES Y CONVERSIÓN A LISTA
# =========================================================================================================================================
# Estructura no ordenada
mi_set = {"1234" , "123" , "999" , '123'}

# print(my_set) # No se pueden imprimir los elementos repetidos
print(mi_set)

# Convertir un set a una lista
setTolist = list(mi_set) 
print(type(setTolist))
print(setTolist)


# =========================================================================================================================================
# RESUMEN DE FUNCIONES DE CONVERSIÓN (MÉTODOS)
# =========================================================================================================================================
# list(argumento)  - Convertir un set a una lista
# tuple(argumento) - Convertir un set a una tupla
# set(argumento)   - Convertir una lista a un set
# dict(argumento)  - Convertir una lista de tuplas a un diccionario

#format strings
#f-strings es una forma de formatear cadenas de texto en Python. Se utiliza para insertar variables dentro de una cadena de texto de manera má
# s legible y concisa. La sintaxis básica es colocar una 'f' antes de la cadena de texto y usar llaves {} para insertar las variables.

print(f"la cantidad de elementos en la lista es: {len(my_lista)}") # Imprime la cantidad de elementos en la lista usando f-string
print(f"la cantidad de elementos diferentes en la lista es: {len(my_set)}") # Imprime la cantidad de elementos diferentes en la lista usando f-string


# ciclo for/while es una estructura de control que se utiliza para repetir un bloque de código un número determinado de veces. La sintaxis básica es:
# la estrutura del for es
# for (variable) in (secuencia):
for elemento in my_lista: # Recorre cada elemento en la lista
    print(elemento) # Imprime cada elemento de la lista