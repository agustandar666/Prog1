Algoritmo densidad_poblacion
	// Desc.: Lee la población y el área ingresados por el usuario y devuelve un mensaje que informa el nivel de densidad de población.
	// Entradas: pob, area
	// Salidas: baja, media, alta
	baja = "Densidad de población: baja"
	media = "Densidad de población: media"
	alta = "Densidad de población: alta"
	
	Escribir "Ingrese población y luego área (en kilómetros cuadrados)"
	Leer pob, area
	
	dens = pob / area
	
	Si dens <= 100 Entonces
		Escribir baja
	SiNo
		Si dens >= 101 Y dens <= 150 Entonces
			Escribir media
		SiNo
			Escribir alta
		FinSi
	FinSi
FinAlgoritmo
