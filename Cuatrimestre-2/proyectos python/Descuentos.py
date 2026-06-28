#Sistema de Descuentos por Antigüedad
#•	El contexto: Una plataforma de streaming quiere premiar a sus usuarios según los años que llevan suscritos.
#•	Tu misión: Pregúntale al usuario cuántos años lleva usando el servicio (usa int()).
#•	La lógica:
#	o	Si lleva 3 años o más, imprime: ¡Felicidades! Clasificas para un 25% de descuento en tu próxima mensualidad.
#	o	Si lleva menos de 3 años, imprime: Gracias por ser parte de nosotros. Sigue acumulando tiempo para ganar beneficios.


print("¿Cuántos años llevas usando nuestro servicio de streaming?")
años = int(input("Años de suscripción: "))
#el int() es para convertir el texto que el usuario ingresa a un numero entero, por ejemplo: int("5") va a convertir el texto "5" a el numero 5
if años >= 3:
    print(f"Gracias por tus {años} años de suscripción. ¡Felicidades! Clasificas para un 25% de descuento en tu próxima mensualidad.")
    #la f es para convertir todo a texto de forma automática por detrás, y las llaves {} son para meter la variable directamente adentro.
    #las {} se pueden usar para meter cualquier variable, por ejemplo: {años} va a meter el numero de años que el usuario ingresó.
else:
    print(f"Gracias por ser parte de nosotros durante {años} años. Sigue acumulando tiempo para ganar beneficios.")
    #la f es para convertir todo a texto de forma automática por detrás, y las llaves {} son para meter la variable directamente adentro.
    #las {} se pueden usar para meter cualquier variable, por ejemplo: {años} va a meter el numero de años que el usuario ingresó.