Algoritmo promedio_impares
	Definir num1, num2, num3, num4 Como Entero
	Definir sumaImpares, cantidadImpares, promedioImpares Como Real
	
	// Pedir al usuario que ingrese los datos
	Escribir "Ingrese el primer n�mero:"
	Leer num1
	Escribir "Ingrese el segundo n�mero:"
	Leer num2
	Escribir "Ingrese el tercer n�mero:"
	Leer num3
	Escribir "Ingrese el cuarto n�mero:"
	Leer num4
	
	// Calcular el promedio de los n�meros impares
	cantidadImpares = 0
	sumaImpares = 0
	Si num1 % 2 == 1 Entonces
		sumaImpares = sumaImpares + num1
		cantidadImpares = cantidadImpares + 1
	FinSi
	Si num2 % 2 == 1 Entonces
		sumaImpares = sumaImpares + num2
		cantidadImpares = cantidadImpares + 1
	FinSi
	Si num3 % 2 == 1 Entonces
		sumaImpares = sumaImpares + num3
		cantidadImpares = cantidadImpares + 1
	FinSi
	Si num4 % 2 == 1 Entonces
		sumaImpares = sumaImpares + num4
		cantidadImpares = cantidadImpares + 1
	FinSi
	
	// Verificar si se encontraron n�meros impares
	Si cantidadImpares == 0 Entonces
		Escribir "No se encontraron n�meros impares."
	Sino
		// Calcular el promedio de los n�meros impares
		promedioImpares = sumaImpares / cantidadImpares
		Escribir "El promedio de los n�meros impares es:", promedioImpares
  FinSi
	
	
FinAlgoritmo
