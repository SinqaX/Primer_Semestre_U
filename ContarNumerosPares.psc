Algoritmo ContarNumerosPares
	// Declarar variables
	Definir num1, num2, num3, num4, cantidadPares Como Entero
	
	// Pedir al usuario que ingrese los datos
	Escribir "Ingrese el primer n�mero:"
	Leer num1
	Escribir "Ingrese el segundo n�mero:"
	Leer num2
	Escribir "Ingrese el tercer n�mero:"
	Leer num3
	Escribir "Ingrese el cuarto n�mero:"
	Leer num4
	
	// Contar la cantidad de n�meros pares
	cantidadPares = 0
	Si num1 % 2 == 0 Entonces
		cantidadPares = cantidadPares + 1
	FinSi
	Si num2 % 2 == 0 Entonces
		cantidadPares = cantidadPares + 1
	FinSi
	Si num3 % 2 == 0 Entonces
		cantidadPares = cantidadPares + 1
	FinSi
	Si num4 % 2 == 0 Entonces
		cantidadPares = cantidadPares + 1
	FinSi
	
	// Mostrar la cantidad de n�meros pares encontrados
	Escribir "La cantidad de n�meros pares es:", cantidadPares
FinAlgoritmo
