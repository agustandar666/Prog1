Algoritmo medidor_formula1
	// Desc.: Lee los tiempos de vueltas de una carrea hasta completar 30 vueltas o sobrepasar los 50min de carrera,
	//		  devuelve el tiempo total de carrera y el promedio de vuelta.
	// Entradas: minutos, segundos
	// Salidas: tiempo_total, promedio_vuelta
	
	vueltas = 0
	minutos_totales = 0
	segundos_totales = 0
	
	Mientras vueltas < 30 y minutos_totales < 50 Hacer
		Escribir "**********************"
		Escribir "Vuelta ", vueltas + 1  // Muestra la cuenta de vueltas en la consola
		
		Escribir "Minutos de vuelta: " // Se piden los minutos de la vuelta
		Leer minutos_vuelta
		
		Escribir "Segundos de vuelta: " // Se piden los segundos de la vuelta
		Leer segundos_vuelta
		
		segundos_totales = segundos_totales + segundos_vuelta // se suman los segundos totales
		
		Si segundos_totales >= 60 Entonces  	// si los segundos totales son 60 o más, se hace la división entera entre 60 y el resultado se suma a los minutos
			
			segundos_a_minutos = trunc(segundos_totales / 60)
			
			minutos_totales = minutos_totales + minutos_vuelta + segundos_a_minutos
			
			segundos_totales = segundos_totales - 60 // se resta 60 a los segundos totales para obtener el sobrante de la división truncada
			
		SiNo
			
			minutos_totales = minutos_totales + minutos_vuelta
			
		FinSi
		
		tiempo_vuelta_segundos = minutos_vuelta * 60 + segundos_vuelta
		
		Si vueltas = 0 Entonces
			mejor_vuelta_seg = tiempo_vuelta_segundos
		SiNo
			Si tiempo_vuelta_segundos < mejor_vuelta_seg Entonces
				mejor_vuelta_seg = tiempo_vuelta_segundos
				mejor_vuelta = vueltas + 1
			FinSi
		FinSi
		
		vueltas = vueltas + 1
		
	FinMientras
	
	tiempo_total_segundos = minutos_totales * 60 + segundos_totales  // tiempo total de carrera en segundos
	promedio_segundos = redon(tiempo_total_segundos / vueltas)		 // promedio de segundos por vuelta
	min_promedio = trunc(promedio_segundos / 60)				
	seg_promedio = promedio_segundos MOD 60
	
	mejor_min = trunc(mejor_vuelta_seg / 60)
	mejor_seg = mejor_vuelta_seg MOD 60
	
	Escribir "***************************************"
	Escribir " "
	Escribir "Vueltas: ", vueltas
	Escribir "Tiempo total de carrera: ", minutos_totales, ":", segundos_totales
	Escribir "Tiempo promedio por vuelta: ", min_promedio, ":", seg_promedio
	Escribir "Mejor vuelta: ", mejor_vuelta
	Escribir "Mejor tiempo de vuelta: ", mejor_min, ":", mejor_seg
	Escribir " "
	Escribir "***************************************"
	
FinAlgoritmo
