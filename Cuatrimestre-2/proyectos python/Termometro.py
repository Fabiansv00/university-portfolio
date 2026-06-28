#El Termómetro de Motores
#•	El contexto: Un sistema industrial monitorea la temperatura de la maquinaria pesada para evitar que explote.
#•	Tu misión: Solicita al usuario la temperatura actual del motor en grados Celsius (usa float()).
#•	La lógica:
#	o	Si la temperatura es mayor a 95.5, debe dar una alerta: [ALERTA] El motor está sobrecalentado. Apagar inmediatamente.
#	o	Si no, debe decir: Temperatura bajo control. Operación segura.


print("Ingrese la temperatura actual del motor en grados Celsius:")
temperatura = float(input("Temperatura: "))

if temperatura > 105:
    print("ALERTA: El motor está sobrecalentado. Apagar inmediatamente.")
elif temperatura < 45:
    print("Temperatura muy baja por favor llamar a ingenieria.")
else:
    print("Temperatura bajo control. Operación segura.")