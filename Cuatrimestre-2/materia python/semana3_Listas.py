
# LISTAS EN PYTHON
# Almacenan colecciones de datos, permiten elementos repetidos y usan corchetes [].

nombreuniversidad = "Universidad Central"
universidades = ["UCR", "UNA", "UNED", "UTN", "TEC"] 

# 1. MEDIR LA LISTA (len)
# len() cuenta el número total de elementos en la lista. 
sizelist = len(universidades) 

# CORRECCIÓN: Imprime el número 5 (la cantidad de elementos), NO "UCR".
print(sizelist) 

# 2. AGREGAR ELEMENTOS (.append y .insert)

# .append() agrega el nuevo elemento al puro FINAL de la lista.
universidades.append("UH") 
universidades.append("U latina") 

# CORRECCIÓN: Imprime el número 7 (la nueva cantidad de elementos). 
# Para ver los nombres de la lista completa usarías: print(universidades)
print(len(universidades)) 

# .insert(posición, elemento) agrega un elemento en el índice indicado.
universidades.insert(3, "UNIBE") # Inserta "UNIBE" en la posición 3
print(universidades) 

# 3. ELIMINAR ELEMENTOS (.remove y .pop)

# .remove() busca por el NOMBRE exacto del elemento y lo borra.
universidades.remove("UH") 
print(universidades) 

# .pop() borra el elemento según su POSICIÓN o ÍNDICE numérico.
universidades.pop(3) # Elimina lo que esté en la posición 3
print(universidades)

#Actualizar elementos de la lista

universidades[1] = "Tecnologico" # Actualiza el elemento en la posición 2 a "Tecnologico"
print(universidades) # Imprime la lista actualizada

#seleccionar elementos de la lista

print(universidades[2]) # imprime el [0,1,2,3,4] elemento de la lista, es decir, "UNED"
#para imprimir un rango de elemntos 
print(universidades[1:4]) # imprime los elementos desde la posición 1 hasta la posición 3, es decir, ["Tecnologico", "UNED", "UTN"]
#siempre es uno menos el numero que se pone al final del rango, es decir, si se pone 4, se imprime hasta la posición 3

#Demas listas con .

# .index() devuelve la posición del primer elemento que coincide con el valor dado.
posicion = universidades.index("UNED")
print(posicion) # Imprime la posición de "UNED", que es 2


# .count() cuenta cuántas veces aparece un elemento específico en la lista.
conteo = universidades.count("UNED")        
print(conteo) # Imprime cuántas veces aparece "UNED", que es 1


# .sort() ordena los elementos de la lista alfabéticamente o numéricamente.
universidades.sort()
print(universidades) # Imprime la lista ordenada


# .reverse() invierte el orden de los elementos en la lista.
universidades.reverse()
print(universidades) # Imprime la lista en orden inverso al orden alfabético    


# .clear() elimina todos los elementos de la lista, dejándola vacía.
universidades.clear()
print(universidades) # Imprime una lista vacía    

  
# .copy() crea una copia de la lista original.
universidades = ["UCR", "UNA", "UNED", "UTN", "TEC"]
universidades_copia = universidades.copy()
print(universidades_copia) # Imprime una copia de la lista original 


# .extend() agrega los elementos de una lista a otra lista.
nuevas_universidades = ["UNIBE", "UH"]                  
universidades.extend(nuevas_universidades)
print(universidades) # Imprime la lista original con las nuevas universidades agregadas 

    
# .count() cuenta cuántas veces aparece un elemento específico en la lista.
conteo_uned = universidades.count("UNED")           
print(conteo_uned) # Imprime cuántas veces aparece "UNED", que es 1 
