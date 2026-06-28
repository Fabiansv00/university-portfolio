#Control de Luces Inteligentes (Domótica)
#•	El contexto: Una casa inteligente enciende o apaga las luces exteriores según la claridad del día.
#•	Tu misión: Pide al usuario que digite el porcentaje de luz solar actual (un número entero de 0 al 100).
#•	La lógica:
#	o	Primero valida el rango: si mete un número menor a 0 o mayor a 100, debe decir [ERROR] Porcentaje inválido.
#	o	Si el porcentaje de luz es menor a 30, imprime: Poca luz detectada. Encendiendo focos exteriores de la casa.
#	o	Si es 30 o más, imprime: Luz solar suficiente. Mantener luces apagadas para ahorrar energía.
print("Ingrese el porcentaje de luz solar actual (0-100):")
luz_solar = int(input("Porcentaje de luz solar: "))

if luz_solar < 0 or luz_solar > 100:
        print("ERROR: Porcentaje inválido.")
elif luz_solar < 30:
    print("Poca luz detectada. Encendiendo focos exteriores de la casa.")
else:
    print("Luz solar suficiente. Mantener luces apagadas para ahorrar energía.")