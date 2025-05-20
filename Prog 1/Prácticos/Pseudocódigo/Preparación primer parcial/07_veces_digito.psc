Algoritmo veces_digito
	// Desc.: Lee un número natural de cualquier extensión y un dígito. Devuelve el número de veces que ese dígito se encuentra en el número natural ingresado
	// Entradas: num, dig
	// Salidas: veces_dig
	
	veces_dig = 0
	
	Escribir "Ingrese un número natural y positivo de cualquier extensión: "
	Leer num
	Escribir "Ingrese un dígito (de 0 a 9): "
	Leer dig
	
	num_ev = num
	
	Mientras num_ev <> 0 Hacer
		
		eval = num_ev MOD 10
		
		Si eval = dig Entonces
			veces_dig = veces_dig + 1
		FinSi
		
		num_ev = trunc(num_ev / 10)
		
	FinMientras
	
	Si veces_dig > 0 Entonces
		Escribir "El dígito ", dig, " aparece ", veces_dig, " veces en el número ", num
	SiNo
		Escribir "El dígito ", dig, " no aparece en el número ", num
	FinSi
	

FinAlgoritmo
