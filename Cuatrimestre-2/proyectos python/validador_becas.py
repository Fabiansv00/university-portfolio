

#1.	El Filtro de Datos Imposibles: Antes de revisar si gana la beca o no, el programa debe rechazar datos incoherentes. 
# Si la edad es menor o igual a 0, si las materias son negativas, o si el promedio está fuera del rango real (menor a 0.0 O mayor a 10.0), 
# debe mostrar un mensaje de [ERROR] con f-strings detallando el dato inválido y frenar el programa.
#2.	La Regla de Aprobación (and): Un estudiante SOLO gana la beca si cumple con tres condiciones obligatorias a la vez:
#o	Tener entre 17 y 25 años inclusive.
#o	Llevar un promedio mayor o igual a 8.5.
#o	Tener matriculadas 4 o más materias.
#o	Si cumple todo, imprime un mensaje personalizado celebrando su beca.
#3.	El Rechazo: Si no cumple con los requisitos mínimos de aprobación, el programa debe decirle amablemente que no califica en este cuatrimestre.

print("╔══════════════════════════════════════════╗")
print("║         VALIDADOR DE BECAS               ║")
print("╠══════════════════════════════════════════╣")
print("║  Ingrese los datos para verificar si     ║")
print("║  usted es apto para recibir una beca.    ║")
print("╚══════════════════════════════════════════╝")
print()

edad = int(input("  📅 Edad                      : "))
promedio = float(input("  📊 Promedio                   : "))
materias = int(input("  📚 Cantidad de materias       : "))

print()
print("══════════════════════════════════════════════")
print("  ✅  Datos ingresados correctamente.")
print("══════════════════════════════════════════════")

if edad <= 0 or materias < 0 or promedio < 0.0 or promedio > 10.0:
    print()
    print("╔══════════════════════════════════════════╗")
    print("║           !! DATOS INVALIDOS !!          ║")
    print("╠══════════════════════════════════════════╣")
    print("║  Los datos ingresados no son correctos.  ║")
    print("║  Por favor verifique e intente de nuevo. ║")
    print("╚══════════════════════════════════════════╝")
else:
    if edad >= 17 and edad <= 25 and promedio >= 8.5 and materias >= 4:
        print()
        print("╔══════════════════════════════════════════╗")
        print("║            *** FELICIDADES ***           ║")
        print("╠══════════════════════════════════════════╣")
        print(f"║  Edad     : {edad} años{' ' * (24 - len(str(edad)))}║")
        print(f"║  Promedio : {promedio}{' ' * (29 - len(str(promedio)))}║")
        print(f"║  Materias : {materias}{' ' * (29 - len(str(materias)))}║")
        print("╠══════════════════════════════════════════╣")
        print("║  Calificas para recibir una beca.        ║")
        print("╚══════════════════════════════════════════╝")
        #el len(str(variable)) es para calcular la cantidad de caracteres que tiene el texto de la variable, 
        # y así poder agregar espacios para que el formato del cuadro quede alineado.
        #la estreutura print(f"║  Promedio : {promedio}{' ' * (28 - len(str(promedio)))}║") es para 
        #imprimir el promedio y luego agregar espacios para que el cuadro quede alineado, 
        # el número 28 es porque el espacio total para esa línea es de 30 caracteres,
    else:
        print()
        print("╔══════════════════════════════════════════╗")
        print("║              LO SENTIMOS...              ║")
        print("╠══════════════════════════════════════════╣")
        print("║  No calificas para recibir una beca      ║")
        print("║  en este cuatrimestre.                   ║")
        print("╚══════════════════════════════════════════╝")