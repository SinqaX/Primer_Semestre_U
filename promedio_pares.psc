Algoritmo promedio_pares
	definir num,sp,cp Como Entero
	definir pp Como Real
	sp=0
	cp=0
	escribir " ingrese el numero "
	leer num
	mientras (num>0)
		si num mod 2==0
			sp=sp+num
			cp=cp+1
		FinSi
		leer num
	FinMientras
	
	si cp>0
		pp=sp/cp
		escribir "el promedio de los numeros pares es ", pp
	sino 
		escribir "no hay numeros pares"
	FinSi
	
FinAlgoritmo
