Algoritmo calcular_tiempo_prueba
	definir a,b,c,ta,tb,tc,t,m como enteros
	definir h como real
	escribir "ingrese la cantidad de pruebas A : "
	leer a
	escribir "ingrese la cantidad de pruebas b : "
	leer b
	escribir "ingrese la cantidad de pruebas c : "
	leer c
	ta=a*12
	tb=b*15
	tc=c*8
	t=ta+tb+tc
	h=t/60
	m=t mod 60
	si t<60
		entonces 
		escribir "el tiempo que se demora en calificar dichas pruebas es ", t, " minutos "
	sino 
		si m==0
			entonces 
			escribir " el tiempo que se demora en calificar dichas pruebas es ", h, " horas"
		sino 
			escribir " el tiempo que se demora en calificar dichas pruebas es ", trunc(h), " horas y ", m, " minutos"
		FinSi
	
	FinSi
	

	
FinAlgoritmo
