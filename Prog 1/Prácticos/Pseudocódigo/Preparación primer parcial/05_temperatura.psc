Algoritmo temperatura
	// Desc.: Lee la temperatura en grados Celsius y devuelve un mensaje que informa cómo está el clima según la temperatura.
	// Entradas: grados
	// Salidas: muy_frio, frio, templado, calido, muy_caliente
	muy_frio = "El clima es muy frío"
	frio = "El clima es frío"
	templado = "El clima es templado"
	calido = "El clima es cálido"
	muy_caliente = "El clima es muy caliente"
	
	Escribir "Ingrese temperatura en grados Celsius"
	Leer grados
	
	Si grados < 0 Entonces
		Escribir "Hay ", grados, "°C. ", muy_frio
	SiNo
		Si grados >= 0 Y grados <= 14 Entonces
			Escribir "Hay ", grados, "°C. ", frio
		SiNo
			Si grados > 14 Y grados <= 24 Entonces
				Escribir "Hay ", grados, "°C. ", templado
			SiNo
				Si grados > 24 y grados <= 30 Entonces
					Escribir "Hay ", grados, "°C. ", calido
				SiNo
					Escribir "Hay ", grados, "°C. ", muy_caliente
				FinSi
			FinSi
		FinSi
	FinSi
FinAlgoritmo
