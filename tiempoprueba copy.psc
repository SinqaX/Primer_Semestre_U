Algoritmo sin_titulo
	Definir cantidadA, cantidadB, cantidadC, tiempoTotal Como Entero
    Definir tiempoHoras, tiempoMinutos Como real
	definir tiempoHoras1, tiempoMinutos1 como real
    Escribir "Ingrese la cantidad de pruebas de tipo A: "
    Leer cantidadA
    Escribir "Ingrese la cantidad de pruebas de tipo B: "
    Leer cantidadB
    Escribir "Ingrese la cantidad de pruebas de tipo C: "
    Leer cantidadC
    tiempoTotal <- (cantidadA * 12) + (cantidadB * 15) + (cantidadC * 8)
    tiempoHoras <- tiempoTotal / 60
	tiempoHoras1 <-REDON(TiempoHoras*1)/1
    tiempoMinutos <- tiempoTotal Mod 60
	tiempominutos1 <-REDON(TiempoMinutos*100)/100
    Escribir "El tiempo total para calificar las pruebas es de ", tiempoHoras1, " horas y ", tiempoMinutos1, " minutos."
FinAlgoritmo
