Algoritmo Accesorios_gamer
	
	// Estas son mis variables para moverme por los menús y hacer los cálculos
	Definir op_menu, op_venta, op_inven, cant_productos, i Como Entero 
	Definir iva_porcentaje, total_factura, unidades, subtotal Como Real
	
	// Mis variables para guardar lo del reporte del día
	Definir total_ventas_dia Como Real
	Definir cant_transacciones Como Entero
	
	// Variables para cuando quiero meter o cambiar productos
	Definir nuevo_nombre Como Caracter
	Definir nuevo_precio, nuevo_stock, cambio_stock Como Real
	
	// Inicio mis contadores en cero y el IVA al 15%
	total_ventas_dia <- 0
	cant_transacciones <- 0
	iva_porcentaje <- 0.15 
	
	// Preparo el espacio en la memoria para poder tener hasta 100 productos, como un estante con varios espacios vacíos
	Dimension nombres[100]
	Dimension precios[100]
	Dimension stocks[100]
	
	// Registro los 3 productos con los que inicio mi tienda
	nombres[1] <- "Mousepad"
	precios[1] <- 3500
	stocks[1] <- 12
	
	nombres[2] <- "Monitor"
	precios[2] <- 39800
	stocks[2] <- 8
	
	nombres[3] <- "GPU"
	precios[3] <- 129000
	stocks[3] <- 6
	
	cant_productos <- 3 // Llevo la cuenta de que ya tengo 3 cosas guardadas
	
	Repetir
		// Mi menú principal
		Escribir "=== TIENDA DE ACCESORIOS GAMER ==="
		Escribir " 1. Registrar venta "
		Escribir " 2. Gestionar inventario "
		Escribir " 3. Ver reporte del día "
		Escribir " 4. Salir "
		Escribir "Elija una opcion:"
		Leer op_menu
		
		Segun op_menu Hacer
			
			1: // REGISTRAR VENTA
				Escribir "--- LISTA DE PRODUCTOS ---"
				// Muestro automáticamente todo lo que tengo guardado
				Para i <- 1 Hasta cant_productos Hacer
					Escribir i, ". ", nombres[i], " - Precio: $", precios[i], " - Disponibles: ", stocks[i]
				FinPara
				
				Escribir "Ingrese el numero del producto a vender:"
				Leer op_venta
				
				Si op_venta >= 1 Y op_venta <= cant_productos Entonces
					Escribir "Cuantas unidades desea llevar de ", nombres[op_venta], "?"
					Leer unidades 
					
					Si unidades <= 0 Entonces
						Escribir "Debe ingresar una cantidad mayor a cero."
					SiNo
						Si unidades > stocks[op_venta] Entonces
							Escribir "Stock insuficiente. Solo hay ", stocks[op_venta], " unidades."
						SiNo
							// Si todo está bien, realizo la venta
							subtotal <- unidades * precios[op_venta]
							total_factura <- subtotal + (subtotal * iva_porcentaje)
							
							// Le resto lo que vendí a mi inventario
							stocks[op_venta] <- stocks[op_venta] - unidades
							
							// Guardo el dinero para mi reporte del final del día
							total_ventas_dia <- total_ventas_dia + total_factura
							cant_transacciones <- cant_transacciones + 1
							
							Escribir "La venta realizada con éxito"  
							Escribir "Subtotal: $", subtotal
							Escribir "Total a pagar: $", total_factura, " (IVA 15% incluido)"
						FinSi
					FinSi
				SiNo
					Escribir "Opcion no valida, intente de nuevo."
				FinSi
				
			2: // GESTIONAR INVENTARIO
				Repetir
					Escribir "--- GESTIÓN DE INVENTARIO ---"
					Escribir " 1. Agregar nuevo accesorio "
					Escribir " 2. Modificar stock de un accesorio existente "
					Escribir " 3. Volver al menú principal "
					Escribir "Elija una opcion:"
					Leer op_inven
					
					Segun op_inven Hacer
						1: // Agrego uno nuevo
							Si cant_productos < 100 Entonces
								cant_productos <- cant_productos + 1
								Escribir "Ingrese el nombre del nuevo accesorio:"
								Leer nombres[cant_productos]
								
								Escribir "Ingrese el precio unitario:"
								Leer nuevo_precio
								Escribir "Ingrese la cantidad inicial en stock:"
								Leer nuevo_stock
								
								// Valido que no me metan números negativos
								Si nuevo_precio > 0 Y nuevo_stock >= 0 Entonces
									precios[cant_productos] <- nuevo_precio
									stocks[cant_productos] <- nuevo_stock
									Escribir "¡Producto agregado correctamente!"
								SiNo
									Escribir "El precio y el stock deben ser valores positivos."
									cant_productos <- cant_productos - 1 // Echo para atrás si hay un error
								FinSi
							SiNo
								Escribir "inventario lleno "
							FinSi
							
						2: // Cambio el stock
							Escribir "--- PRODUCTOS EN SISTEMA ---"
							Para i <- 1 Hasta cant_productos Hacer
								Escribir i, ". ", nombres[i], " - Stock actual: ", stocks[i]
							FinPara
							
							Escribir "Seleccione el numero del producto a modificar:"
							Leer op_venta
							
							Si op_venta >= 1 Y op_venta <= cant_productos Entonces
								Escribir "Ingrese la cantidad a sumar (o usar signo menos para restar):"
								Leer cambio_stock
								
								// Reviso que la resta no nos deje en números negativos
								Si (stocks[op_venta] + cambio_stock) >= 0 Entonces
									stocks[op_venta] <- stocks[op_venta] + cambio_stock
									Escribir "Stock actualizado. Nuevo inventario de ", nombres[op_venta], " es: ", stocks[op_venta]
								SiNo
									Escribir "La operacion resultaria en un stock negativo."
								FinSi
							SiNo
								Escribir "El producto seleccionado no existe."
							FinSi
							
						3:
							Escribir "Regresando al menú principal..."
						De Otro Modo:
							Escribir "Opcion no valida."
					FinSegun
				Hasta Que op_inven = 3
				
			3: // REPORTE DEL DÍA
				Escribir "--- REPORTE DE VENTAS DEL DÍA ---"
				Si cant_transacciones = 0 Entonces
					Escribir "No hay ventas registradas el día de hoy."
				SiNo
					Escribir "Ventas totales: $", total_ventas_dia
					Escribir "Compras realizadas: ", cant_transacciones
					// Evito el error de dividir por cero, porque ya comprobé que sí hay ventas arriba
					Escribir "Promedio de las ventas: $", (total_ventas_dia / cant_transacciones)
				FinSi
				
			4: // SALIR
				Escribir "Saliendo del sistema... ¡Vuelva Pronto!"
				
			De Otro Modo:
				Escribir "Opcion incorrecta. Por favor elija un numero del 1 al 4."
		FinSegun
		
		Escribir "" // Dejo un espacio en blanco para que no se vea todo pegado
		
	Hasta Que op_menu = 4
	
FinAlgoritmo
