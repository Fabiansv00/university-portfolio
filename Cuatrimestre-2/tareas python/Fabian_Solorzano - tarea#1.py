Nombre = input("Ingrese su nombre: ")
Apellido = input("Ingrese su apellido: ")
print("Mucho gusto " + Nombre + " " + Apellido + ", que carrera esta llevando?")


Carrera = input("Ingrese su carrera: ")
print("Ingrese su nota de -> " + Carrera + " Para mostrale su clasificacion")
nota = float(input("Ingrese su nota: "))
#float es para convertir un texto a numero con decimales


if nota >= 0 and nota <= 65: #si la norta es mayor o igual a 0 y menor o igual a 65, entonces es reprobado
    print("Estas Reprobado en la materia de " + Carrera)
elif nota > 65 and nota < 90: #si la nota es mayor a 65 y menor a 90, entonces esta aprobado
    print("Estas Aprobado en la materia de " + Carrera)
elif nota >= 90 and nota <= 100: #si la nota es mayor o igual a 90 y menor o igual a 100, entonces es estudiante de honor
    print("Eres un estudiante de honor en la materia de " + Carrera)
else: #si la nota es menor a 0 o mayor a 100, entonces es una nota invalida
    print("Nota invalida, por favor ingrese una nota entre 0 y 100")
          
    
    #Fabian solorzano Barrantes Clase Miercoles