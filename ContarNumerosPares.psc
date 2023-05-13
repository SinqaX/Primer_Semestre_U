Algoritmo ContarNumerosPares
	// Declarar variables
	Definir num1, num2, num3, num4, cantidadPares Como Entero
	
	// Pedir al usuario que ingrese los datos
	Escribir "Ingrese el primer número:"
	Leer num1
	Escribir "Ingrese el segundo número:"
	Leer num2
	Escribir "Ingrese el tercer número:"
	Leer num3
	Escribir "Ingrese el cuarto número:"
	Leer num4
	
	// Contar la cantidad de números pares
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
	
	// Mostrar la cantidad de números pares encontrados
	Escribir "La cantidad de números pares es:", cantidadPares
FinAlgoritmo
