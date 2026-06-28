print("Hello, World!")
#IDE es un ambiente de desarrollo integrado (IDE) que se utiliza para escribir, depurar y ejecutar código.

Nombre = "Fabian"
Apellido = "Solorzano"

# Las variables estan entre "" es un string es una cadena de acracteres, es decir, un texto o numeros pero 
#Python lo interpreta como texto. Los numeros enteros se pueden escribir sin comillas, por ejemplo: Edad = 30
#tenemos float que son numeros con decimales, por ejemplo: Precio = 19.99
#Tenemos int que son numeros enteros, por ejemplo: Cantidad = 5
#tenemos bool que son valores booleanos, es decir, verdadero o falso, por ejemplo: EsMayorDeEdad = True
#tenemos integer que son numeros enteros, por ejemplo: Cantidad = 5

edad = 17
Numero_1 = "12345" #texto no numeros
Numero_2 = "12345" #texto no numeros
print(Numero_1 + Numero_2) #esto va a concatenar los dos numeros como texto, es decir, va a imprimir "1234512345"

numero_3 = 12345 #esto es un numero entero, no un texto
numero_4 = 12345 #esto es un numero entero, no un texto
print(numero_3 + numero_4) #esto va a sumar los dos numeros, es decir, va a imprimir 24690

#conversiones de tipos de datos
#str es para convertir un numero a texto, por ejemplo: str(Edad) va a convertir el numero 30 a "30"
#int es para convertir un texto a numero entero, por ejemplo: int(Numero_1) va a convertir el texto "12345" a 12345
#float es para convertir un texto a numero con decimales, por ejemplo: float(
    
print("Hola mi nombre es " + Nombre + " " + Apellido, "Y mi edad es " + str(edad)) 
#Esto hace una concatenacion de texto, es decir, va a imprimir "Hola mi nombre es Fabian Solorzano Y mi edad es 19"

#comparaciones ( ==, !=, >, <, >=, <=)
# == es para comparar si dos valores son iguales, por ejemplo: edad == 19 va a ser True
# != es para comparar si dos valores son diferentes, por ejemplo: edad != 20 va a ser True
# > es para comparar si un valor es mayor que otro, por ejemplo: edad > 18 va a ser True
# < es para comparar si un valor es menor que otro, por ejemplo: edad < 20 va a ser True
# >= es para comparar si un valor es mayor o igual que otro, por ejemplo: edad >= 19 va a ser True
# <= es para comparar si un valor es menor o igual que otro, por ejemplo: edad <= 20 va a ser True

#Condiciones (if, elif, else)
# if es para ejecutar un bloque de codigo si se cumple una condicion, por ejemplo: if
# elif es para ejecutar un bloque de codigo si se cumple una condicion diferente a la anterior,
# por ejemplo: elif Edad < 18: print("Es menor de edad") va a imprimir "Es menor de edad" si la condicion se cumple
# else es para ejecutar un bloque de codigo si no se cumple ninguna de las condiciones anteriores,
# por ejemplo: else: print("No se cumple ninguna condicion") va a imprimir "No se cumple ninguna condicion" si ninguna de las condiciones anteriores se cumple

if edad == 18:
    print("Es mayor de edad")
elif edad < 18:
    print("Es menor de edad")
elif edad > 18:
    print("Es mayor de edad")
    
#el input es para pedirle al usuario que ingrese un valor, por ejemplo: Nombre = input("Ingrese su nombre: ") 
# va a pedirle al usuario que ingrese su nombre y lo va a almacenar en la variable Nombre