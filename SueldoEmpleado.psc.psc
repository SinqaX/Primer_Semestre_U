Algoritmo SueldoEmpleado

	Definir nh,sh,st Como Entero
	Definir ds,scd Como Real
	Escribir 'numero de horas '
	Leer nh
	Escribir 'sueldo por hora '
	Leer sh
	st <- nh*sh
	ds <- st*10/100
	scd <- st-ds
	Escribir 'sueldo a pagar =',scd

FinAlgoritmo
