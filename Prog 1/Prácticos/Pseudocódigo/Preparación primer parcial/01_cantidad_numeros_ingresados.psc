Algoritmo cantidad_numeros_ingresados
	// Desc.: Lee números ingresados por el usuario, devuelve la cantidad de números que se introdujeron, el número menor, el mayor
	//		  y el promedio.
	// Entradas: numeros, n_mayor, n_menor, promedio
	// Salidas: cantidad_numeros
	Escribir "******************************************"
	Escribir " "
	Escribir "Ingrese un número (ingrese 0 para salir): "
	Leer n_primero
	n = n_primero
	n_mayor = n_primero
	n_menor = n_primero
	suma = n_primero
	cantidad_numeros = 1
	
	Mientras n <> 0 Hacer
		Escribir " "
		Escribir "******************************************"
		Escribir " "
		Escribir "Ingrese un número (ingrese 0 para salir): "
		Leer n
		Si n <> 0 Entonces
			
			cantidad_numeros = cantidad_numeros + 1
			
			suma = suma + n
			
			Si n < n_menor Entonces
				n_menor = n
			SiNo
				Si n > n_mayor Entonces
					n_mayor = n
				FinSi
			FinSi
			
		FinSi
	FinMientras
	
	promedio = suma / cantidad_numeros
	Escribir "*********************************************"
	Escribir " "
	Escribir "Se ingresaron ", cantidad_numeros, " números."
	Escribir " "
	Escribir "El menor fue: ", n_menor
	Escribir "El mayor fue: ", n_mayor
	Escribir "El promedio es: ", promedio
	Escribir " "
	Escribir "*********************************************"
FinAlgoritmo
