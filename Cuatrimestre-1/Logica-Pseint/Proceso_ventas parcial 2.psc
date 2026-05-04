Algoritmo Proceso_ventas
	//La sala tiene una capacidad máxima fija de 60 personas. 
	//La aplicación debe llevar un registro constante de los asientos vendidos y disponibles.
	
	Definir Asientos_disp, precio_entra, dinero_recaudado, cant_entrada como entero
	
	Definir opcion_menu Como entero
	
	Definir boleto_usua_cant, cant_devoluc Como Entero
	
	Definir opcion_peli Como entero
	
	Definir bolet_open Como Logico // open para ahorrar espacio
	
precio_entra = 5000	//Este valor debe utilizarse para todos los cálculos de ventas y devoluciones.
Asientos_disp <- 60
cant_entrada <- 0
dinero_recaudado <- 0
bolet_open <- Verdadero

Mientras opcion_menu <> 7 Hacer //Mientras que la opcion del menu sea difetente a 7
	
	Escribir " Bienvenido a la Boletería de FabiMarck "
	Escribir " "
	Escribir "Escriba la opcion que desea consultar"
	Escribir " "
	Escribir " 1.Vender boletos"
	Escribir " 2.Devolver entrada"
	Escribir " 3.Ver disponibilidad de espacios "
	Escribir " 4.ver información de la película "
	Escribir " 5.Cerrar boletería"
	Escribir " 6.Ver total recaudado "
	Escribir " 7.Salir"
	leer opcion_menu
	
	Segun opcion_menu Hacer
		1 :
			Si bolet_open == Verdadero Entonces
			Escribir "============================================="
			Escribir "Cantidad de asientos disponibles : ", Asientos_disp
			Escribir "Cuantos boletos desea comparar? : "
			Leer cant_entrada
			Si cant_entrada > 0 Y cant_entrada <= Asientos_disp Entonces
				Asientos_disp <- Asientos_disp - cant_entrada
				boleto_usua_cant <- boleto_usua_cant + cant_entrada
				dinero_recaudado <- dinero_recaudado + (cant_entrada * precio_entra)
				Escribir "Las entradas seria para un total de : $", (cant_entrada * precio_entra)
				Escribir " Entradas compradas!! "
			sino
				Escribir "La cantidad es incorrecta o supera el maximo de la sala"
			FinSi
		SiNo
			Escribir " La boleteria esta cerrada!, solo se permite las opciones 6 y 7 "
		FinSi
			Escribir "=============================================="
		2: 
			Si bolet_open == Verdadero Entonces
				Escribir "=========================================="
				Escribir ""
				Escribir " ======= Apartado de devolucion ==========" // tiene algo que devolver?
				Escribir ""
				Escribir "=========================================="
				
				Si boleto_usua_cant == 0 Entonces
					Escribir ""
					Escribir " Usted no cuenta con boletos! "
				SiNo
					Repetir
						Escribir "Usted tiene un total de ", boleto_usua_cant " boletos "
						Escribir "Ingrese la cantidad para devolver!" "Para cancelar escriba 0"
						Leer cant_devoluc
						
						Si cant_devoluc > 0 y cant_devoluc <= boleto_usua_cant Entonces // si la cantidad es mayor a 0 o menor e igual a los boletos del usaurio
							Asientos_disp <- Asientos_disp + cant_devoluc // devolver los espacios
							boleto_usua_cant <- boleto_usua_cant - cant_devoluc
							dinero_recaudado <- dinero_recaudado - (cant_devoluc * precio_entra)
							Escribir " Su devolución se completada con éxito "
						SiNo
							Si cant_devoluc <> 0 Entonces// si la cantidad es diferente a 0
								Escribir "la cantidad no es correcta, no puede devolver mas entradas de las que tiene! o entradas negativas!"
							FinSi
						FinSi
						
			Hasta Que cant_devoluc >= 0 Y cant_devoluc <= boleto_usua_cant
				FinSi
			SiNo
				Escribir " La boleteria esta cerrada!, solo se permite las opciones 6 y 7 "
			FinSi
			
			    Escribir ""
			    Escribir "=========================================="
			3:
				Si bolet_open == Verdadero Entonces
				Escribir "=========================================="
				Escribir ""
				Escribir "El total de espacios disponible es : ", Asientos_disp
				Escribir ''
				Escribir "=========================================="
			SiNo
				Escribir " La boleteria esta cerrada!, solo se permite las opciones 6 y 7 "
			FinSi
		4:
			Si bolet_open == Verdadero Entonces
				Escribir "=========================================="
				Escribir ""
				Escribir " ====== Cartelera ====== "
				Escribir "1. La sirenita 3 "
				Escribir "2. Interestelar "
				Escribir "3. Los 4 rufianes "
				Escribir "4. Cumbres borrascosas "
				Escribir "5. Salir de la cartelera"
				Escribir ""
				Escribir "=========================================="
				
				leer opcion_peli
				
				si opcion_peli == 5 Entonces
					Escribir "Saliendo de la cartelera..."
				sino
					Segun opcion_peli hacer 
						1:
							Escribir " ===== La sirenita 3 ===== "
							Escribir "La historia de la infancia de Ariel antes de conocer a los humanos y por qué su padre, el Rey Tritón, prohibió la música en el reino "
							Escribir "Duración: 100 minutos"
							Escribir "Clasificación: TDP"
							Escribir "Horarios: 10:30am, 1:45pm, 4:15pm, 7:30pm"
						2:
							Escribir " ===== Interestelar ===== "
							Escribir "Un grupo de astronautas viaja a través de un agujero de gusano en busca de un nuevo refugio"
							Escribir "Duración: 150 minutos"
							Escribir "Clasificación: TDP"
							Escribir "Horarios: 2:00pm, 5:00pm, 8:00pm, 11:00pm"
						3:
							Escribir " ===== Los 4 rufianes ===== "
							Escribir "Cuenta la historia sobre cuatro delincuentes con pensamientos muy distintos que terminan involucrados en una misión o aventuras peligrosas"
							Escribir "Duración: 80 minutos"
							Escribir "Clasificación: +15"
							Escribir "Horarios: 12:00pm, 3:30pm, 6:45pm, 9:15pm"
						4: 
							Escribir " ===== Cumbres borrascosas ===== "
							Escribir "Es una historia de amor obsesivo y venganza, sigue la relación entre Heathcliff y Catherine"
							Escribir "Duración: 120 minutos"
							Escribir "Clasificación: +18"
							Escribir "Horarios: 11:00am, 2:30pm, 5:45pm, 10:00pm"
							Escribir ""
							Escribir "=========================================="
					FinSegun
				FinSi
			SiNo
				Escribir " La boleteria esta cerrada!, solo se permite las opciones 6 y 7 "
			FinSi
				Escribir ""
				Escribir "=========================================="
				
			5:
				
					Escribir "=========================================="
					Escribir ""
					Escribir "========= Cerrando boleteria... =========="
					Escribir ""
					Escribir "=========================================="
					Escribir ""
					bolet_open <- Falso
					Escribir " la venta y la devolución han sido desactivadas! "
					Escribir "Solo puede ingresar a las siguientes opciones : "
					Escribir "6. Ver total recaudado"
					Escribir "7. Salir"
				    Escribir ""
				    Escribir "=========================================="
				
			6:	
				Escribir "============================================================"
				Escribir ""
				Escribir " =========== $Total recaudado$ ============================="
				
				cant_entrada <- boleto_usua_cant
				
				Escribir " ==== Total de boletos vendidos : ", cant_entrada, " ========"
				Escribir " ==== Cantidad de ganancias : ", dinero_recaudado, "$ ==========="
				Escribir "=== Cantidad de devoluciones : ", cant_devoluc, " ============"
				Escribir ""
				Escribir "============================================================"
			7:	
				Escribir "==================================================================="
				Escribir ""
				Escribir " Muchas gracias por usar la boleteria de FabiMarck! Vuelva pronto! "
				Escribir ""
				Escribir "==================================================================="
				
	FinSegun
	
Fin Mientras

FinAlgoritmo
