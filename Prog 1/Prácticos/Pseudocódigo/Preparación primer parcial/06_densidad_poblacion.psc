Algoritmo densidad_poblacion
	// Desc.: Lee la poblaci�n y el �rea ingresados por el usuario y devuelve un mensaje que informa el nivel de densidad de poblaci�n.
	// Entradas: pob, area
	// Salidas: baja, media, alta
	baja = "Densidad de poblaci�n: baja"
	media = "Densidad de poblaci�n: media"
	alta = "Densidad de poblaci�n: alta"
	
	Escribir "Ingrese poblaci�n y luego �rea (en kil�metros cuadrados)"
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
