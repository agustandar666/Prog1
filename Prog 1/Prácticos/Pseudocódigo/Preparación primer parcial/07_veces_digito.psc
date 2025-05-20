Algoritmo veces_digito
	// Desc.: Lee un n�mero natural de cualquier extensi�n y un d�gito. Devuelve el n�mero de veces que ese d�gito se encuentra en el n�mero natural ingresado
	// Entradas: num, dig
	// Salidas: veces_dig
	
	veces_dig = 0
	
	Escribir "Ingrese un n�mero natural y positivo de cualquier extensi�n: "
	Leer num
	Escribir "Ingrese un d�gito (de 0 a 9): "
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
		Escribir "El d�gito ", dig, " aparece ", veces_dig, " veces en el n�mero ", num
	SiNo
		Escribir "El d�gito ", dig, " no aparece en el n�mero ", num
	FinSi
	

FinAlgoritmo
