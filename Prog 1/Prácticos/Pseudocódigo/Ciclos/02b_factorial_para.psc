Algoritmo factorial_para
	Leer n
	resultado = n
	contador = n
	
	Para Num = 1 Hasta n - 1 Hacer
		resultado = resultado * (contador - 1)
		contador = contador - 1
		Escribir resultado
	FinPara
FinAlgoritmo
