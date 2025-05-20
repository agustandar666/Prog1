Algoritmo divisibles_2_y_3
	// Desc.: Lee n�meros ingresados por el usuario y devuelve la cantidad de n�meros divisibles entre 2,
	//       la cantidad de n�meros divisibles entre 3 y la cantidad de n�meros que no son divisibles
	//       por ninguno de esos dos n�meros
	// Entradas: n_primero, n
	// Salidas: divisibles_2, divisibles_3, no_divisibles
	Escribir "******************************************"
	Escribir " "
	Escribir "Ingrese un n�mero (ingrese 0 para salir): "
	Leer n_primero
	n = n_primero
	divisibles_2 = 0
	divisibles_3 = 0
	no_divisibles = 0
	
	Mientras n <> 0 Hacer
		Si n <> 0 Entonces
			
			Si n MOD 2 = 0  y n MOD 3 = 0 Entonces
				divisibles_2 = divisibles_2 + 1
				divisibles_3 = divisibles_3 + 1
			SiNo
				Si n MOD 2 = 0 Entonces
					divisibles_2 = divisibles_2 + 1
				SiNo
					Si n MOD 3 = 0 Entonces
						divisibles_3 = divisibles_3 + 1
					SiNo
						no_divisibles = no_divisibles + 1
					FinSi
				FinSi
			FinSi
		FinSi
		
		Escribir " "
		Escribir "******************************************"
		Escribir " "
		Escribir "Ingrese un n�mero (ingrese 0 para salir): "
		
		Leer n
	FinMientras
	
	Escribir " "
	Escribir "******************************************"
	Escribir " "
	Escribir "N�meros divisibles entre 2: ", divisibles_2
	Escribir " "
	Escribir "N�meros divisibles entre 3: ", divisibles_3
	Escribir " "
	Escribir "N�meros no divisibles entre 2 ni 3: ", no_divisibles
	
FinAlgoritmo
