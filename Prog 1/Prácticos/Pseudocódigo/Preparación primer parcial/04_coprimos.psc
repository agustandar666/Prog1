Algoritmo coprimos
	// Desc.: Lee dos números ingresados por el usuario y devtermina si son coprimos.
	// Entradas: a, b
	// Salidas: son_coprimos, no_son_coprimos
	
	son_coprimos = "Son coprimos"
	no_son_coprimos = "No son coprimos"
	
	Escribir "Ingrese dos números: "
	Leer a, b
	
	valor_a = a
	valor_b = b
	
	Mientras valor_b <> 0 Hacer       // Algoritmo de Euclides
		resto = valor_a MOD valor_b
		valor_a = valor_b
		valor_b = resto
	FinMientras
	
	mcd = valor_a
	
	son_coprimos = "Son coprimos"
	no_son_coprimos = "No son coprimos"
	
	Si mcd = 1 Entonces
		Escribir son_coprimos
	SiNo
		Escribir no_son_coprimos
	FinSi
	
FinAlgoritmo
