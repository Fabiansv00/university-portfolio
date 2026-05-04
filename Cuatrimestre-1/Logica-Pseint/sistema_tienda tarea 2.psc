Algoritmo sistema_tienda
	// Primero anoto qué variables voy a ocupar para guardar los datos ;)
	// Uso "Entero" para cosas que se cuentan y "Real" para precios o kilos que llevan punto decimal
	Definir num_clientes, i Como Entero
	Definir opcion_fruta Como Entero
	Definir kilos, precio_kilo, subtotal, descuento, total_cliente, ingresos_totales Como Real
	Definir nombre_fruta Como Caracter
	
	// Antes de abrir la tienda, me aseguro de que la caja empiece en cero 
	// Si no hago esto, la memoria me puede dar números a lo loco de ayer o asi
	ingresos_totales <- 0
	
	Escribir "=== Caja registradora de ventas - Tienda Don Huevo ==="
	
	// Aquí no dejo que el programa siga hasta que me des un número de clientes de verdad
	// Si metemos un cero o un negativo, voy a volver a preguntar 
	Repetir
		Escribir "Ingrese el número de clientes que realizaron compras hoy: " Sin Saltar
		Leer num_clientes
		Si num_clientes <= 0 Entonces
			Escribir "Ocupo un número positivo, No puedo atender a clientes que no existen."
		FinSi
	Hasta Que num_clientes > 0
	
	// voy a pasar a cada cliente uno por uno, como si estuvieran en una fila =)
	Para i <- 1 Hasta num_clientes Con Paso 1 Hacer
		Escribir ""
		Escribir "--- CLIENTE #", i, " ---"
		
		// Le pregunto al cliente qué quiere, pongo esta lista para que sea más fácil elegir
		Escribir "Seleccione la opcion de la fruta comprada:"
		Escribir "1. Manzana ($5/kg)"
		Escribir "2. Plátano ($3/kg)"
		Escribir "3. Naranja ($4.50/kg)"
		Escribir "Opción: " Sin Saltar
		Leer opcion_fruta
		
		// Aquí reviso qué número se selecciono, dependiendo de eso yo mismo le pongo el precio al kilo
		Segun opcion_fruta Hacer
			1:
				nombre_fruta <- "Manzana"
				precio_kilo <- 5
			2:
				nombre_fruta <- "Plátano"
				precio_kilo <- 3
			3:
				nombre_fruta <- "Naranja"
				precio_kilo <- 4.50
			De Otro Modo:
				// Si se equivocas de tecla, por seguridad te cobro lo de la manzana.
				Escribir "Esa opción no existe, así que voy a asumir que es Manzana."
				nombre_fruta <- "Manzana (Error)"
				precio_kilo <- 5
		FinSegun
		
		Escribir "Ingrese la cantidad de kilos de ", nombre_fruta, ": " Sin Saltar
		Leer kilos
		
		// Multiplico lo que pesa por lo que vale :p
		subtotal <- kilos * precio_kilo
		
		// Si el cliente se lleva más de 5 kilos, le hago un descuentito del 10%.
		// Si lleva poquito osea menos de 5 kilos pues no le descuento nada
		Si kilos > 5 Entonces
			descuento <- subtotal * 0.10
			Escribir "Por su compra le regalamos un 10% de descuento por comprar bastante "
		Sino
			descuento <- 0
		FinSi
		
		// Calculo cuánto tiene que pagar al final
		total_cliente <- subtotal - descuento
		
		// Le muestro el recibo al cliente para que vea que no le estoy estafando :D
		Escribir "Subtotal: $", subtotal
		Escribir "Descuento: $", descuento
		Escribir "Total de este cliente: $", total_cliente
		
		// Sumo lo de este cliente a la bolsa grande de la tienda. 
		// Es como ir metiendo los billetes en la caja registradora uno tras otro y asi
		ingresos_totales <- ingresos_totales + total_cliente
		
	FinPara
	
	// Al final del día, cierro la caja y te digo cuánta plata hicimos en total
	Escribir ""
	Escribir "========================================"
	Escribir " RESUMEN DE VENTAS DEL DÍA "
	Escribir " Total de clientes que atendí: ", num_clientes
	Escribir " PLATA TOTAL EN CAJA: $", ingresos_totales
	Escribir "========================================"
FinAlgoritmo
